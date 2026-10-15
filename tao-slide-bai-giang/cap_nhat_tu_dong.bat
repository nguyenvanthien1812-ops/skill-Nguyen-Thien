@echo off
chcp 65001 >nul
title Cap Nhat Tu Dong - Skill Soan Slide Bai Giang - Thay Thien

echo.
echo ====================================================================
echo        CẬP NHẬT TỰ ĐỘNG - SKILL SOẠN SLIDE BÀI GIẢNG
echo           Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe
echo ====================================================================
echo.

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
    echo     Vui long chay file "cai_dat_tu_dong.bat" truoc de cai dat Python.
    echo.
    pause
    exit /b 1
)

set "UP_SCRIPT="
if exist "%~dp0scripts\updater.py" (
    set "UP_SCRIPT=%~dp0scripts\updater.py"
) else if exist "%USERPROFILE%\.gemini\config\skills\tao-slide-bai-giang\scripts\updater.py" (
    set "UP_SCRIPT=%USERPROFILE%\.gemini\config\skills\tao-slide-bai-giang\scripts\updater.py"
)

if "%UP_SCRIPT%"=="" (
    echo [X] Khong tim thay file kich ban updater.py!
    pause
    exit /b 1
)

echo [*] Dang ket noi may chu kiem tra tinh nang moi...
"%PYTHON_EXE%" "%UP_SCRIPT%"

echo.
pause
