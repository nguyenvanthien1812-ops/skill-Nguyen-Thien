@echo off
chcp 65001 >nul
title CAP NHAT TU DONG TRON BO TRO LY GIAO VIEN AI - THAY THIEN

echo.
echo ====================================================================
echo    CẬP NHẬT TỰ ĐỘNG BỘ CÔNG CỤ TRỢ LÝ GIÁO VIÊN AI - CHUẨN GDPT 2018
echo              Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe
echo ====================================================================
echo.

echo [*] Dang ket noi may chu GitHub kiem tra ban cap nhat moi nhat...
where git >nul 2>nul
if not errorlevel 1 (
    if exist "%~dp0.git" (
        git -C "%~dp0" pull origin main
    )
)

echo [*] Dang nap dong bo vao he thong Google Antigravity...
set "DIR1=%USERPROFILE%\.gemini\config\skills\tao-de-toan-tuong-tu"
if not exist "%DIR1%" mkdir "%DIR1%"
if exist "%~dp0tao-de-toan-tuong-tu" xcopy "%~dp0tao-de-toan-tuong-tu\*" "%DIR1%\" /E /I /Y /Q >nul

set "DIR2=%USERPROFILE%\.gemini\config\skills\soan-giao-an-tich-hop-nls"
if not exist "%DIR2%" mkdir "%DIR2%"
if exist "%~dp0soan-giao-an-tich-hop-nls" xcopy "%~dp0soan-giao-an-tich-hop-nls\*" "%DIR2%\" /E /I /Y /Q >nul

set "DIR3=%USERPROFILE%\.gemini\config\skills\tao-slide-bai-giang"
if not exist "%DIR3%" mkdir "%DIR3%"
if exist "%~dp0tao-slide-bai-giang" xcopy "%~dp0tao-slide-bai-giang\*" "%DIR3%\" /E /I /Y /Q >nul

set "DIR4=%USERPROFILE%\.gemini\config\skills\tao-video-khoi-dong-bai-hoc"
if not exist "%DIR4%" mkdir "%DIR4%"
if exist "%~dp0tao-video-khoi-dong-bai-hoc" xcopy "%~dp0tao-video-khoi-dong-bai-hoc\*" "%DIR4%\" /E /I /Y /Q >nul

echo.
echo ====================================================================
echo   🎉 [HOÀN TẤT] ĐÃ CẬP NHẬT TOÀN BỘ TÍNH NĂNG MỚI NHẤT THÀNH CÔNG!
echo.
echo   Mở Google Antigravity lên là Thầy/Cô sử dụng được ngay tính năng mới!
echo ====================================================================
echo.
pause
