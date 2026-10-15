#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hệ Thống Tự Động Cập Nhật Skill "tao-slide-bai-giang" từ GitHub
Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe
- Kiểm tra phiên bản mới nhất trên kho GitHub
- Tải và cập nhật toàn bộ tính năng mới, tài liệu, kịch bản
- BẢO TOÀN TUYỆT ĐỐI file license.key và mã máy của giáo viên (không bao giờ bị mất bản quyền)
- Tự động nạp bản mới vào Google Antigravity nếu đã cài đặt
"""

import sys
import os
import json
import urllib.request
import urllib.error
import shutil
import tempfile
import zipfile
import argparse

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# ─── CẤU HÌNH THƯ MỤC & GITHUB ──────────────────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR   = os.path.dirname(SCRIPT_DIR)
LOCAL_VER   = os.path.join(SKILL_DIR, "version.json")
CONFIG_FILE = os.path.join(SKILL_DIR, "github_config.json")

# Danh sách tệp TUYỆT ĐỐI BẢO VỆ không được ghi đè
PROTECTED_FILES = {
    "license.key",
    "machine_id.txt",
    "MA_MAY_CUA_BAN.txt",
    "config.json",
    "github_config.json"
}

# Cấu hình GitHub của Thầy Nguyễn Văn Thiện
GITHUB_USER   = "nguyenvanthien1812-ops"
GITHUB_REPO   = "skill-Nguyen-Thien"
SKILL_SUBDIR  = "tao-slide-bai-giang"

# Cho phép ghi đè cấu hình qua file nếu cần
if os.path.exists(CONFIG_FILE):
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            cfg = json.load(f)
            GITHUB_USER  = cfg.get("github_user", GITHUB_USER)
            GITHUB_REPO  = cfg.get("github_repo", GITHUB_REPO)
            SKILL_SUBDIR = cfg.get("skill_subdir", SKILL_SUBDIR)
    except Exception:
        pass


def get_github_urls():
    api_base    = f"https://api.github.com/repos/{GITHUB_USER}/{GITHUB_REPO}"
    raw_base    = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main"
    zip_url     = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/archive/refs/heads/main.zip"
    version_url = f"{raw_base}/{SKILL_SUBDIR}/version.json" if SKILL_SUBDIR else f"{raw_base}/version.json"
    return api_base, raw_base, zip_url, version_url


def fetch_json(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": "tao-slide-bai-giang-updater/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def read_local_version():
    if not os.path.exists(LOCAL_VER):
        return "0.0.0", {}
    try:
        with open(LOCAL_VER, encoding="utf-8") as f:
            data = json.load(f)
        return data.get("version", "0.0.0"), data
    except Exception:
        return "0.0.0", {}


def compare_versions(v1, v2):
    """Trả về True nếu v2 > v1"""
    def parse(v):
        parts = []
        for x in str(v).split("."):
            try:
                parts.append(int(x))
            except ValueError:
                parts.append(0)
        return tuple(parts)
    return parse(v2) > parse(v1)


def download_zip_and_update(zip_url, dest_dir, target_subpath=SKILL_SUBDIR):
    """
    Tải toàn bộ repo ZIP từ GitHub và giải nén đúng thư mục con của skill.
    Bỏ qua các file thuộc PROTECTED_FILES để bảo toàn bản quyền.
    """
    print(f"[*] Đang tải bản nâng cấp mới nhất từ GitHub...")
    tmp_zip = tempfile.mktemp(suffix=".zip")
    try:
        req = urllib.request.Request(zip_url, headers={"User-Agent": "tao-slide-bai-giang-updater/1.0"})
        with urllib.request.urlopen(req, timeout=90) as resp, open(tmp_zip, "wb") as f:
            f.write(resp.read())
        print(f"[✓] Tải thành công! Bắt đầu trích xuất và bảo vệ bản quyền...")

        with zipfile.ZipFile(tmp_zip, "r") as z:
            namelist = z.namelist()
            # Tìm prefix gốc (ví dụ: skill-Nguyen-Thien-main/)
            root_prefix = ""
            for n in namelist:
                if n.endswith("/") and n.count("/") == 1:
                    root_prefix = n
                    break

            match_prefix = f"{root_prefix}{target_subpath}/" if target_subpath else root_prefix

            updated = []
            skipped = []

            for member in namelist:
                if not member.startswith(match_prefix) or member == match_prefix:
                    continue

                rel_path = member[len(match_prefix):]
                if not rel_path:
                    continue

                basename = os.path.basename(rel_path.rstrip("/"))
                if basename in PROTECTED_FILES:
                    skipped.append(rel_path)
                    continue

                target = os.path.join(dest_dir, rel_path)
                if member.endswith("/"):
                    os.makedirs(target, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(target), exist_ok=True)
                    with z.open(member) as src, open(target, "wb") as dst:
                        dst.write(src.read())
                    updated.append(rel_path)

        return updated, skipped
    finally:
        if os.path.exists(tmp_zip):
            try:
                os.remove(tmp_zip)
            except Exception:
                pass


def sync_to_antigravity(src_dir):
    """Đồng bộ cập nhật sang thư mục Antigravity nếu đã có trên máy"""
    user_home = os.path.expanduser("~")
    antigravity_dir = os.path.join(user_home, ".gemini", "config", "skills", "tao-slide-bai-giang")

    # Nếu thư mục hiện tại chính là thư mục Antigravity thì không cần sync lại
    if os.path.abspath(src_dir).lower() == os.path.abspath(antigravity_dir).lower():
        return True

    if not os.path.exists(antigravity_dir):
        return False

    print(f"\n[*] Đang tự động nạp tính năng mới vào Google Antigravity...")
    try:
        for root, dirs, files in os.walk(src_dir):
            rel_path = os.path.relpath(root, src_dir)
            target_dir = os.path.join(antigravity_dir, rel_path)
            os.makedirs(target_dir, exist_ok=True)

            for file in files:
                if file in PROTECTED_FILES:
                    continue
                src_file = os.path.join(root, file)
                dst_file = os.path.join(target_dir, file)
                shutil.copy2(src_file, dst_file)
        print(f"[✓] Đã nạp thành công vào Google Antigravity!")
        return True
    except Exception as e:
        print(f"[!] Cảnh báo khi đồng bộ vào Antigravity: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Cập nhật Skill Soạn Slide Bài Giảng từ GitHub")
    parser.add_argument("--check-only", action="store_true", help="Chỉ kiểm tra phiên bản, không cập nhật")
    parser.add_argument("--force",      action="store_true", help="Buộc cập nhật dù đang là phiên bản mới nhất")
    args = parser.parse_args()

    print("=" * 70)
    print("      HỆ THỐNG CẬP NHẬT TỰ ĐỘNG - SKILL SOẠN SLIDE BÀI GIẢNG")
    print("        Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe")
    print("=" * 70)

    local_ver, local_data = read_local_version()
    print(f"\n[i] Phiên bản máy của Thầy/Cô đang dùng : v{local_ver}")

    api_base, raw_base, zip_url, version_url = get_github_urls()

    try:
        print(f"[*] Đang kết nối máy chủ GitHub ({GITHUB_USER}/{GITHUB_REPO})...")
        remote_data = fetch_json(version_url, timeout=12)
        remote_ver  = remote_data.get("version", "0.0.0")
        print(f"[i] Phiên bản mới nhất trên máy chủ   : v{remote_ver}")
    except (urllib.error.URLError, Exception) as e:
        print(f"\n[!] Không thể kết nối với máy chủ cập nhật: {e}")
        print("    • Vui lòng kiểm tra lại kết nối mạng Internet của máy tính.")
        print("    • Skill trên máy tính của Thầy/Cô vẫn hoạt động bình thường.")
        return

    is_newer = compare_versions(local_ver, remote_ver)

    if not is_newer and not args.force:
        print(f"\n[✓] Tuyệt vời! Thầy/Cô đang sử dụng PHIÊN BẢN MỚI NHẤT (v{local_ver}).")
        changelog = remote_data.get("changelog", {}).get(remote_ver, [])
        if changelog:
            print(f"\n  Các tính năng hiện có trong v{remote_ver}:")
            for item in changelog:
                print(f"    • {item}")
        return

    if args.check_only:
        print(f"\n[!] Đã có phiên bản nâng cấp: v{remote_ver} (phiên bản hiện tại: v{local_ver})")
        changelog = remote_data.get("changelog", {}).get(remote_ver, [])
        print("  Tính năng mới:")
        for item in changelog:
            print(f"    • {item}")
        print("\n  → Nhấp đúp vào file cap_nhat_tu_dong.bat để tiến hành cập nhật.")
        return

    # Hiển thị thông tin phiên bản mới
    print("\n" + "=" * 70)
    print(f"  🔔 PHÁT HIỆN BẢN NÂNG CẤP MỚI: v{local_ver} ──▶ v{remote_ver}")
    print("=" * 70)
    changelog = remote_data.get("changelog", {}).get(remote_ver, [])
    if changelog:
        print("  Các cải tiến & tính năng mới:")
        for item in changelog:
            print(f"    ⭐ {item}")

    confirm = input("\n  Cập nhật tính năng mới ngay bây giờ? [Y/n] (Nhấn Enter để đồng ý): ").strip().upper()
    if confirm and confirm not in ("Y", "YES"):
        print("  Đã dừng tiến trình cập nhật.")
        return

    # Tiến hành tải và cập nhật
    updated_files, skipped_files = download_zip_and_update(zip_url, SKILL_DIR)
    print(f"\n[✓] Đã cập nhật thành công {len(updated_files)} tệp mã nguồn và tài liệu.")

    if skipped_files:
        print(f"[i] Bảo toàn an toàn các tệp bản quyền cá nhân:")
        for f in set(skipped_files):
            print(f"    🛡️  {f} (giữ nguyên bản quyền, không bị thay đổi)")

    # Đồng bộ sang Google Antigravity
    sync_to_antigravity(SKILL_DIR)

    print("\n" + "=" * 70)
    print(f"  🎉 [HOÀN TẤT] BẠN ĐÃ CẬP NHẬT LÊN PHIÊN BẢN v{remote_ver} THÀNH CÔNG!")
    print("  Toàn bộ tính năng mới đã sẵn sàng cho bài giảng tiếp theo của Thầy/Cô.")
    print("=" * 70)


if __name__ == "__main__":
    main()
