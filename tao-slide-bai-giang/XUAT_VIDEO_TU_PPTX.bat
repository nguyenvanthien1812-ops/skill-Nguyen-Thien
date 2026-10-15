@echo off
chcp 65001 >nul
title Xuat Video Bai Giang MP4 Tu Slide PowerPoint

echo.
echo ====================================================================
echo      XUẤT VIDEO BÀI GIẢNG MP4 TỪ FILE POWERPOINT (.PPTX)
echo           Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe
echo ====================================================================
echo.

set "PPTX_FILE=%~1"

if "%PPTX_FILE%"=="" (
    echo 👉 HƯỚNG DẪN DÙNG RẤT ĐƠN GIẢN:
    echo    1. Thầy/Cô hãy KÉO THẢ file PowerPoint (.pptx) vào trực tiếp file bat này.
    echo    2. Hoặc dán đường dẫn file PowerPoint vào đây rồi nhấn Enter:
    echo.
    set /p "PPTX_FILE=👉 Nhập đường dẫn file .pptx: "
)

if "%PPTX_FILE%"=="" (
    echo [!] Chưa có file PowerPoint để xuất video.
    pause
    exit /b 1
)

set "PYTHON_EXE="
py -c "import sys" >nul 2>nul && set "PYTHON_EXE=py"
if "%PYTHON_EXE%"=="" python -c "import sys" >nul 2>nul && set "PYTHON_EXE=python"
if "%PYTHON_EXE%"=="" (
    for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python3*") do if exist "%%D\python.exe" set "PYTHON_EXE=%%D\python.exe"
)
if "%PYTHON_EXE%"=="" (
    for /d %%D in ("C:\Program Files\Python3*") do if exist "%%D\python.exe" set "PYTHON_EXE=%%D\python.exe"
)
if "%PYTHON_EXE%"=="" (
    for /d %%D in ("C:\Python3*") do if exist "%%D\python.exe" set "PYTHON_EXE=%%D\python.exe"
)

if "%PYTHON_EXE%"=="" (
    echo [!] Khong tim thay Python tren may tinh!
    echo     Vui long chay file "cai_dat_tu_dong.bat" truoc de cai dat.
    pause
    exit /b 1
)

set "SCRIPT_FILE="
if exist "%~dp0scripts\xuat_video_pptx.py" (
    set "SCRIPT_FILE=%~dp0scripts\xuat_video_pptx.py"
) else if exist "%USERPROFILE%\.gemini\config\skills\tao-slide-bai-giang\scripts\xuat_video_pptx.py" (
    set "SCRIPT_FILE=%USERPROFILE%\.gemini\config\skills\tao-slide-bai-giang\scripts\xuat_video_pptx.py"
)

if "%SCRIPT_FILE%"=="" (
    echo [X] Khong tim thay script xuat_video_pptx.py!
    pause
    exit /b 1
)

echo [*] Dang tien hanh xuat video tu file: %PPTX_FILE%
echo [*] Vui long cho trong giay lat de PowerPoint tao video...
echo.

"%PYTHON_EXE%" "%SCRIPT_FILE%" %PPTX_FILE%

echo.
pause
