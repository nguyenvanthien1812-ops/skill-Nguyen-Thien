@echo off
chcp 65001 >nul
title NAP SKILL SOAN GIAO AN TICH HOP NLS VAO ANTIGRAVITY

echo.
echo ====================================================================
echo   TỰ ĐỘNG NẠP SKILL SOẠN GIÁO ÁN NLS & AI VÀO GOOGLE ANTIGRAVITY
echo               Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe
echo ====================================================================
echo.

set "TARGET_DIR=%USERPROFILE%\.gemini\config\skills\soan-giao-an-tich-hop-nls"

echo [*] Dang tao thu muc skill tren may tinh...
if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"

echo [*] Dang sao chep toan bo file skill vao Antigravity...
xcopy "%~dp0*" "%TARGET_DIR%\" /E /I /Y /Q >nul

echo.
echo ====================================================================
echo   🎉 [HOÀN TẤT] ĐÃ NẠP SKILL VÀO ANTIGRAVITY THÀNH CÔNG!
echo.
echo   Bây giờ Thầy/Cô chỉ cần mở Google Antigravity lên
echo   và nhắn tin: "Tôi muốn soạn giáo án..." là dùng được ngay!
echo ====================================================================
echo.
pause
