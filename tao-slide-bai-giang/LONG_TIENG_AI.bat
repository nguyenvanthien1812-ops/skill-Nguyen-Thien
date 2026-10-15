@echo off
chcp 65001 >nul
title Long Tieng AI Cho Slide PowerPoint - Thay Thien

echo.
echo ====================================================================
echo      TỰ ĐỘNG LỒNG TIẾNG AI CHO SLIDE POWERPOINT TỪ LỜI BÌNH (NOTES)
echo           Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe
echo ====================================================================
echo.

set "PPTX_FILE=%~1"

if "%PPTX_FILE%"=="" (
    echo 👉 HƯỚNG DẪN DÙNG RẤT ĐƠN GIẢN:
    echo    1. KÉO THẢ file PowerPoint (.pptx đã có lời bình ở Notes) vào file bat này.
    echo    2. Hoặc dán đường dẫn file PowerPoint vào đây rồi nhấn Enter:
    echo.
    set /p "PPTX_FILE=👉 Nhập đường dẫn file .pptx: "
)

if "%PPTX_FILE%"=="" (
    echo [!] Chưa có file PowerPoint để lồng tiếng.
    pause
    exit /b 1
)

echo.
echo 🎙️ CHỌN GIỌNG ĐỌC PHÁT THANH VIÊN AI:
echo    [1] Cô Hoài My  (Giọng nữ miền Bắc - Nhẹ nhàng, truyền cảm, chuẩn cô giáo)
echo    [2] Thầy Nam Minh (Giọng nam miền Bắc - Dõng dạc, trầm ấm, chuẩn thầy giáo)
echo.
set "VOICE_OPT=1"
set /p "VOICE_OPT=👉 Thầy/Cô chọn số [1 hoặc 2, nhấn Enter để mặc định chọn 1]: "

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
    echo [!] Khong tim thay Python tren may tinh! Chay cai_dat_tu_dong.bat truoc.
    pause
    exit /b 1
)

set "SCRIPT_FILE="
if exist "%~dp0scripts\long_tieng_pptx.py" (
    set "SCRIPT_FILE=%~dp0scripts\long_tieng_pptx.py"
) else if exist "%USERPROFILE%\.gemini\config\skills\tao-slide-bai-giang\scripts\long_tieng_pptx.py" (
    set "SCRIPT_FILE=%USERPROFILE%\.gemini\config\skills\tao-slide-bai-giang\scripts\long_tieng_pptx.py"
)

if "%SCRIPT_FILE%"=="" (
    echo [X] Khong tim thay script long_tieng_pptx.py!
    pause
    exit /b 1
)

echo.
echo [*] Dang tien hanh doc loi giang va long tieng vao slide...
echo.

"%PYTHON_EXE%" "%SCRIPT_FILE%" "%PPTX_FILE%" --voice "%VOICE_OPT%"

echo.
pause
