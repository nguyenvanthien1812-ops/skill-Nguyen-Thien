#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔐 License Manager – Kiểm Tra & Kích Hoạt License Key
Tích hợp vào Skill Soạn Slide Bài Giảng Chuẩn Mực Sư Phạm (tao-slide-bai-giang)

Cách dùng (giáo viên):
  python scripts/license_manager.py --machine-id     → Lấy Machine ID để gửi tác giả
  python scripts/license_manager.py --activate <KEY> → Kích hoạt license
  python scripts/license_manager.py --check          → Kiểm tra trạng thái license
"""

import sys, os, json, base64, hashlib, socket, platform, uuid
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

try:
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.backends import default_backend
    HAS_CRYPTO = True
except ImportError:
    try:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "cryptography", "-q"], check=True)
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.backends import default_backend
        HAS_CRYPTO = True
    except Exception:
        HAS_CRYPTO = False

# ─── CẤU HÌNH ────────────────────────────────────────────────────────────────
SKILL_DIR    = Path(__file__).resolve().parent.parent  # Thư mục gốc của skill
SKILL_NAME   = "tao-slide-bai-giang"

# ─── DANH MỤC CÁC TIỆN ÍCH CỐT LÕI (MODULAR FEATURE LICENSING) ────────────────
FEATURE_CATALOG = {
    "slide_bai_giang": {
        "index": "1",
        "name": "Soạn slide bài giảng 3 bước chuẩn GDPT 2018",
        "short": "Slide bài giảng chuẩn mực",
        "desc": "Soạn slide từ giáo án/SGK, lọc sạch mục tiêu rườm rà, đi thẳng tiến trình 3 bước"
    },
    "so_do_tu_duy": {
        "index": "2",
        "name": "Sơ đồ tư duy Infographic Radial tỏa tròn",
        "short": "Sơ đồ tư duy tỏa tròn",
        "desc": "Mô hình tư duy tâm điểm tỏa tròn 360°, màu sắc phân nhánh đối xứng, có hiệu ứng bung tỏa"
    },
    "bai_tap_tuong_tac": {
        "index": "3",
        "name": "Slide bài tập điền từ & Trò chơi tương tác",
        "short": "Bài tập tương tác / Điền từ",
        "desc": "Slide bài tập khuyết từ chia cột, click đáp án nhảy lên đúng vị trí"
    },
    "cong_thuc_omml": {
        "index": "4",
        "name": "Công thức Toán học Native OMML chuẩn SGK",
        "short": "Công thức OMML (Toán/Lí/Hóa)",
        "desc": "Công thức vector sắc nét, click đúp chuột sửa trực tiếp 100% trong PowerPoint không cần MathType"
    },
    "tim_anh_web": {
        "index": "5",
        "name": "Tự động tìm kiếm ảnh thực tế khoa học từ Web",
        "short": "Tìm ảnh thực tế bản quyền mở",
        "desc": "Tự động tìm kiếm và chèn ảnh minh họa thực tế, hiển vi khoa học chất lượng cao"
    },
    "video_bai_giang": {
        "index": "6",
        "name": "Hỗ trợ xuất PPTX lồng tiếng & Dựng video bài giảng",
        "short": "Hỗ trợ video bài giảng",
        "desc": "Tự động đồng bộ animation tự chạy, hỗ trợ lồng tiếng xuất video MP4"
    }
}

def get_unlocked_features(payload: dict) -> list[str]:
    """Lấy danh sách các mã tiện ích được mở khóa trong payload (Mặc định: ['ALL'])."""
    if not payload:
        return []
    feats = payload.get("features")
    if not feats:
        return ["ALL"]
    if isinstance(feats, str):
        feats = [f.strip() for f in feats.split(",") if f.strip()]
    if "ALL" in feats or "*" in feats:
        return ["ALL"]
    return list(feats)

def has_feature_permission(payload: dict, required_feature: str | list[str] | None = None) -> bool:
    """Kiểm tra xem payload bản quyền có quyền sử dụng tiện ích required_feature hay không."""
    if not payload:
        return False
    if not required_feature:
        return True
    unlocked = get_unlocked_features(payload)
    if "ALL" in unlocked:
        return True
    if isinstance(required_feature, str):
        return required_feature in unlocked
    if isinstance(required_feature, (list, tuple, set)):
        return any(f in unlocked for f in required_feature)
    return False

def format_features_summary(payload: dict) -> str:
    """Trả về chuỗi mô tả gói tiện ích đã mở khóa."""
    unlocked = get_unlocked_features(payload)
    if "ALL" in unlocked:
        return "🌟 TRỌN BỘ TẤT CẢ TIỆN ÍCH (FULL VIP)"
    names = []
    for code in unlocked:
        info = FEATURE_CATALOG.get(code)
        if info:
            names.append(f"[{info['index']}] {info['name']}")
        else:
            names.append(code)
    return ", ".join(names) if names else "Chưa có tiện ích nào"

def get_all_license_paths() -> list[Path]:
    """Trả về danh sách tất cả các vị trí có thể lưu hoặc kiểm tra license.key."""
    paths = []
    paths.append(SKILL_DIR / "license.key")
    try:
        user_home = Path.home()
        paths.append(user_home / ".gemini" / "config" / "skills" / SKILL_NAME / "license.key")
        paths.append(user_home / ".gemini" / "antigravity" / "skills" / SKILL_NAME / "license.key")
        paths.append(user_home / ".gemini" / "license.key")
    except Exception:
        pass
    try:
        cwd = Path.cwd().resolve()
        paths.append(cwd / "license.key")
        paths.append(cwd / SKILL_NAME / "license.key")
        paths.append(cwd / ".agents" / "skills" / SKILL_NAME / "license.key")
        if cwd != cwd.parent:
            paths.append(cwd.parent / "license.key")
            paths.append(cwd.parent / SKILL_NAME / "license.key")
    except Exception:
        pass

    unique_paths = []
    seen = set()
    for p in paths:
        try:
            resolved = p.resolve()
            if resolved not in seen:
                seen.add(resolved)
                unique_paths.append(p)
        except Exception:
            if p not in unique_paths:
                unique_paths.append(p)
    return unique_paths

# ⚠️ PUBLIC KEY RSA CỦA TÁC GIẢ (Dùng để xác thực chữ ký bản quyền)
PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsykVJf8gHugg+wgotDfK
zUlDcpW09tl/medCzkzfI/1l19nwEqbiJoNBgbroCtu2fU38Jw+saRMusXbMys3a
aCPrHKkg0ui/59jTQx82T5a3VX+fPLe+aiMwe13b/oLGur/pPU6dqr2eoYeNUt3T
9hw+jl2XHYdDgytPeRmGUE8fN/q0VQLaCuKZcXgxugc9JnGZrkZyvoiz2cmNp2mt
Sq+mLFWvPxhbx9gTlHxX7AZCIRjTSJeq9bOL7sHiuSNClRXHAQiYUppoWiumPOV7
fjegRJweRxtBVRmC/zxxL+xz6/Hgazwivog1pRE6tr4gE0xyqjGFgyOca+dW+33H
EQIDAQAB
-----END PUBLIC KEY-----"""

def get_machine_id() -> str:
    """Tạo Machine ID duy nhất cho máy tính này."""
    parts = []
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    parts.append(mac)
    parts.append(socket.gethostname().lower())
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Cryptography")
        guid, _ = winreg.QueryValueEx(key, "MachineGuid")
        parts.append(guid)
    except Exception:
        parts.append(platform.node())

    raw = "|".join(parts)
    return hashlib.sha256(raw.encode()).hexdigest()[:32]

def verify_license_key(license_key: str) -> tuple[bool, dict, str]:
    """Xác minh license key bằng RSA Public Key."""
    if not HAS_CRYPTO:
        return False, {}, "Cần cài thư viện cryptography: pip install cryptography"

    try:
        parts = license_key.strip().split(".")
        if len(parts) != 2:
            return False, {}, "Định dạng license key không hợp lệ"

        payload_bytes = base64.urlsafe_b64decode(parts[0] + "==")
        signature     = base64.urlsafe_b64decode(parts[1] + "==")
        payload       = json.loads(payload_bytes.decode("utf-8"))

        public_key = serialization.load_pem_public_key(
            PUBLIC_KEY_PEM.strip().encode(), backend=default_backend()
        )
        public_key.verify(
            signature, payload_bytes,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )

        # Cho phép key dùng chung hệ sinh thái hoặc dành riêng cho skill này
        target_skill = payload.get("skill", "")
        if target_skill not in {SKILL_NAME, "ALL", "tao-de-toan-tuong-tu"}:
            return False, payload, "License key không dành cho skill này"

        # Kiểm tra machine_id
        machine_id = payload.get("machine_id", "ANY")
        if machine_id != "ANY":
            current_mid = get_machine_id()
            if current_mid != machine_id:
                return False, payload, (
                    f"License key này được cấp cho máy khác!\n"
                    f"  Mã máy hiện tại : {current_mid}\n"
                    f"  Mã máy trong key : {machine_id}\n"
                    f"  → Vui lòng gửi mã máy hiện tại cho Thầy Thiện để nhận key mới."
                )

        # Kiểm tra hạn sử dụng
        expiry = datetime.strptime(payload["expiry"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        if datetime.now(timezone.utc) > expiry:
            days_overdue = (datetime.now(timezone.utc) - expiry).days
            return False, payload, f"License key đã hết hạn {days_overdue} ngày (hết hạn: {payload['expiry']})."

        return True, payload, ""

    except Exception as e:
        return False, {}, f"Lỗi xác minh: {e}"

def get_license_token() -> str:
    """Lấy chuỗi license key từ bất kỳ file nào khả dụng."""
    for p in get_all_license_paths():
        if p.exists():
            try:
                t = p.read_text(encoding="utf-8").strip()
                if t:
                    return t
            except Exception:
                continue
    return ""

def activate(license_key: str) -> bool:
    """Xác minh và lưu license key vào máy ở tất cả các vị trí cần thiết."""
    print("[*] Đang xác minh license key...")
    is_valid, payload, error = verify_license_key(license_key)

    if not is_valid:
        print(f"[✗] License key KHÔNG HỢP LỆ:\n    {error}")
        return False

    clean_key = license_key.strip()
    saved_count = 0
    for p in get_all_license_paths():
        try:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(clean_key, encoding="utf-8")
            saved_count += 1
        except Exception:
            pass

    print("\n" + "=" * 60)
    print("  🎉 KÍCH HOẠT BẢN QUYỀN THÀNH CÔNG!")
    print("=" * 60)
    print(f"  • Người dùng : {payload.get('name', 'Giáo viên')}")
    print(f"  • Hạn dùng   : {payload.get('expiry', 'Vĩnh viễn')}")
    print(f"  • Gói tiện ích: {format_features_summary(payload)}")
    print("=" * 60)
    return True

def check_current_license() -> tuple[bool, dict, str]:
    """Kiểm tra license hiện tại trên máy."""
    token = get_license_token()
    if not token:
        return False, {}, "Chưa tìm thấy file license.key nào trên máy."
    return verify_license_key(token)

def copy_to_clipboard(text: str):
    """Copy text vào Clipboard trên Windows."""
    try:
        import subprocess
        cmd = f'powershell -Command "Set-Clipboard -Value \'{text}\'"'
        subprocess.run(cmd, shell=True, check=True)
        return True
    except Exception:
        try:
            p = subprocess.Popen(['clip'], stdin=subprocess.PIPE, shell=True)
            p.communicate(text.encode('utf-8'))
            return True
        except Exception:
            return False

def main():
    import argparse
    p = argparse.ArgumentParser(description="License Manager – Skill Soạn Slide Bài Giảng")
    g = p.add_mutually_exclusive_group(required=False)
    g.add_argument("--machine-id", action="store_true", help="Lấy Machine ID của máy này")
    g.add_argument("--activate",   nargs="?", const="PROMPT", metavar="LICENSE_KEY", help="Kích hoạt license key")
    g.add_argument("--check",      action="store_true",   help="Kiểm tra trạng thái license")
    p.add_argument("--feature",    metavar="FEATURE_CODE", help="Kiểm tra quyền sử dụng một tiện ích cụ thể")
    args = p.parse_args()

    if not (args.machine_id or args.activate or args.check):
        args.check = True

    if args.machine_id:
        mid = get_machine_id()
        copied = copy_to_clipboard(mid)
        print("=" * 60)
        print("         MÃ ĐỊNH DANH MÁY TÍNH (MACHINE ID)")
        print("=" * 60)
        print(f"\n   Mã máy của bạn:  {mid}\n")
        print("-" * 60)
        if copied:
            print("📋 [ĐÃ TỰ ĐỘNG COPY VÀO BỘ NHỚ TẠM / CLIPBOARD!]")
            print("👉 Thầy/Cô chỉ cần mở Zalo gửi cho Thầy Thiện và bấm Ctrl + V.")
        else:
            print("👉 Vui lòng bôi đen dòng mã máy ở trên rồi bấm Ctrl + C để gửi.")
        print("=" * 60)

    elif args.activate:
        key = args.activate
        if key == "PROMPT":
            print("=" * 60)
            print("       KÍCH HOẠT BẢN QUYỀN SKILL SOẠN SLIDE BÀI GIẢNG")
            print("=" * 60)
            key = input("\n👉 Dán mã License Key bạn nhận được rồi Enter:\n\n> ").strip()

        if not key:
            print("[!] Mã License Key không được để trống!")
            sys.exit(1)

        ok = activate(key)
        sys.exit(0 if ok else 1)

    elif args.check:
        is_valid, payload, error = check_current_license()
        print("\n" + "=" * 65)
        if is_valid:
            days_left = (datetime.strptime(payload["expiry"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
                         - datetime.now(timezone.utc)).days
            status = "✅ HỢP LỆ" if days_left > 7 else f"⚠️  CÒN {days_left} NGÀY"
            unlocked = get_unlocked_features(payload)
            print(f"  Trạng thái  : {status}")
            print(f"  Tên         : {payload.get('name', '')}")
            print(f"  Hết hạn     : {payload['expiry']} (còn {days_left} ngày)")
            print(f"  Khóa máy    : {'Khóa theo máy này' if payload.get('machine_id') != 'ANY' else 'Không giới hạn máy'}")
            print(f"  Gói mở khóa : {format_features_summary(payload)}")
            print(f"  UNLOCKED_FEATURES : {','.join(unlocked)}")
            print("=" * 65)
            sys.exit(0)
        else:
            print(f"  Trạng thái  : ❌ CHƯA HỢP LỆ")
            print(f"  Chi tiết    : {error}")
            print("=" * 65)
            sys.exit(1)

if __name__ == "__main__":
    main()
