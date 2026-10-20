# -*- coding: utf-8 -*-
r"""
Công cụ Cấp Key Bản Quyền Nhanh Cho Giáo Viên (Dành Riêng Cho Thầy Thiện)
Vị trí: D:\skill-Nguyen-Thien\
- Nhập/Dán Machine ID của giáo viên
- Tự động sinh Key chuẩn kép (hợp lệ cho cả Soạn slide và Tạo đề toán)
- Tự động lưu vào sổ quản lý tác quyền
- Tự động copy Key vào Clipboard để gửi Zalo ngay
"""
import sys, os, json, uuid, base64, subprocess
from pathlib import Path
from datetime import datetime, timedelta, timezone

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
except Exception:
    pass

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

SCRIPT_DIR = Path(__file__).parent.resolve()
PRIVATE_KEY_PATH = SCRIPT_DIR / "private_key.pem"
DB_PATH = SCRIPT_DIR / "danh_sach_license_da_cap.json"

if not PRIVATE_KEY_PATH.exists():
    fallback_key = Path(r"D:\skill-quan-trong\QUAN_LY_BAN_QUYEN_TAC_GIA\private_key.pem")
    if fallback_key.exists():
        PRIVATE_KEY_PATH = fallback_key

def main():
    print("=" * 65)
    print("   HỆ THỐNG CẤP LICENSE KEY BẢN QUYỀN - THẦY NGUYỄN THIỆN")
    print("=" * 65)

    if not PRIVATE_KEY_PATH.exists():
        print(f"[!] Không tìm thấy khóa gốc private_key.pem!")
        input("\nBấm Enter để thoát...")
        return

    private_key = serialization.load_pem_private_key(
        PRIVATE_KEY_PATH.read_bytes(),
        password=None,
        backend=default_backend()
    )

    machine_id = ""
    if len(sys.argv) > 1:
        machine_id = sys.argv[1].strip()

    if not machine_id:
        machine_id = input("\n👉 Nhập hoặc Dán Mã Máy (Machine ID) do Giáo viên gửi:\n> ").strip()

    if not machine_id:
        print("[!] Mã máy không được để trống!")
        input("\nBấm Enter để thoát...")
        return

    name = input("\nTên Giáo viên / Trường [Mặc định: Giao Vien VIP]: ").strip()
    if not name:
        name = "Giao Vien VIP"

    now = datetime.now(timezone.utc)
    expiry = now + timedelta(days=365)
    license_id = str(uuid.uuid4())

    # Cấu hình chuẩn tương thích kép: Cả tạo slide lẫn tạo đề đều mở FULL VIP
    payload = {
        "skill": "tao-de-toan-tuong-tu",
        "name": name,
        "email": "giaovien@school.edu.vn",
        "machine_id": machine_id,
        "issued": now.strftime("%Y-%m-%d"),
        "expiry": expiry.strftime("%Y-%m-%d"),
        "license_id": license_id,
        "features": ["ALL"]
    }

    payload_bytes = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode('utf-8')
    signature = private_key.sign(
        payload_bytes,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    license_key = f"{base64.urlsafe_b64encode(payload_bytes).decode('utf-8')}.{base64.urlsafe_b64encode(signature).decode('utf-8')}"

    # Lưu database
    db = []
    if DB_PATH.exists():
        try:
            db = json.loads(DB_PATH.read_text(encoding='utf-8'))
        except Exception:
            db = []

    db.append({
        **payload,
        "license_key": license_key,
        "created_at": now.isoformat()
    })
    DB_PATH.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding='utf-8')

    root_db = Path(r"D:\skill-quan-trong\QUAN_LY_BAN_QUYEN_TAC_GIA\danh_sach_license_da_cap.json")
    if root_db.exists() and root_db != DB_PATH:
        try:
            root_db.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding='utf-8')
        except Exception:
            pass

    print("\n" + "=" * 65)
    print("  🎉 ĐÃ CẤP LICENSE KEY THÀNH CÔNG!")
    print("=" * 65)
    print(f"  • Người nhận : {name}")
    print(f"  • Mã máy     : {machine_id}")
    print(f"  • Hạn dùng   : {payload['expiry']} (1 năm)")
    print(f"  • Quyền hạn  : FULL VIP (Tất cả tính năng Slide + Đề thi)")
    print("-" * 65)
    print("MÃ LICENSE KEY:")
    print(license_key)
    print("=" * 65)

    try:
        subprocess.run(f'powershell -Command "Set-Clipboard -Value \'{license_key}\'"', shell=True, check=True)
        print("📋 [ĐÃ TỰ ĐỘNG COPY VÀO BỘ NHỚ TẠM / CLIPBOARD!]")
        print("👉 Thầy chỉ cần mở Zalo gửi cho giáo viên và bấm Ctrl + V.")
    except Exception:
        pass

    if len(sys.argv) <= 1:
        input("\nBấm Enter để đóng cửa sổ...")

if __name__ == "__main__":
    main()
