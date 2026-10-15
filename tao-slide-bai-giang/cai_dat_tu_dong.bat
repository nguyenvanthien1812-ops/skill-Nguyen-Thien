@echo off
chcp 65001 >nul
title Cai Dat Tu Dong 1-Click - Skill Soan Slide Bai Giang

echo.
echo ====================================================================
echo      HỆ THỐNG CÀI ĐẶT TỰ ĐỘNG 1-CLICK - SKILL SOẠN SLIDE BÀI GIẢNG
echo ====================================================================
echo.

set "PYTHON_EXE="

:: ─── BƯỚC 1: KIỂM TRA PYTHON CÓ SẴN KHÔNG ───────────────────────────
echo [*] Buoc 1/2: Kiem tra moi truong Python...

py -c "import sys" >nul 2>nul
if not errorlevel 1 (
    set "PYTHON_EXE=py"
    goto :PYTHON_READY
)

python -c "import sys" >nul 2>nul
if not errorlevel 1 (
    set "PYTHON_EXE=python"
    goto :PYTHON_READY
)

for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python3*") do (
    if exist "%%D\python.exe" (
        "%%D\python.exe" -c "import sys" >nul 2>nul
        if not errorlevel 1 (
            set "PYTHON_EXE=%%D\python.exe"
            set "PATH=%%D;%%D\Scripts;%PATH%"
            goto :PYTHON_READY
        )
    )
)

for /d %%D in ("C:\Program Files\Python3*") do (
    if exist "%%D\python.exe" (
        "%%D\python.exe" -c "import sys" >nul 2>nul
        if not errorlevel 1 (
            set "PYTHON_EXE=%%D\python.exe"
            set "PATH=%%D;%%D\Scripts;%PATH%"
            goto :PYTHON_READY
        )
    )
)

for /d %%D in ("C:\Python3*") do (
    if exist "%%D\python.exe" (
        "%%D\python.exe" -c "import sys" >nul 2>nul
        if not errorlevel 1 (
            set "PYTHON_EXE=%%D\python.exe"
            set "PATH=%%D;%%D\Scripts;%PATH%"
            goto :PYTHON_READY
        )
    )
)

:: Neu hoan toan chua co Python -> Tu dong tai ve
echo [!] May tinh chua co Python. Dang tu dong tai Python 3.11 ve cai dat...
set "PY_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe"
set "PY_INSTALLER=%TEMP%\python-installer.exe"

powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; (New-Object Net.WebClient).DownloadFile('%PY_URL%', '%PY_INSTALLER%')"
if exist "%PY_INSTALLER%" (
    echo [*] Dang cai dat Python che do am tham...
    start /wait "" "%PY_INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
    del /f /q "%PY_INSTALLER%" >nul 2>nul
)

set "PYTHON_EXE=python"

:PYTHON_READY
echo [OK] Python da san sang!

:: ─── BƯỚC 2: CÀI ĐẶT CÁC THƯ VIỆN BỔ TRỢ ───────────────────────────
echo.
echo [*] Buoc 2/2: Cai dat cac thu vien can thiet (cryptography, python-pptx, edge-tts, pillow, lxml)...
%PYTHON_EXE% -m pip install --upgrade pip --quiet
%PYTHON_EXE% -m pip install cryptography python-pptx edge-tts pillow lxml requests --quiet

echo.
echo ====================================================================
echo  🎉 CHÚC MỪNG: CÀI ĐẶT MÔI TRƯỜNG THÀNH CÔNG!
echo ====================================================================
echo.
echo 👉 Thầy/Cô có thể:
echo    1. Nhấp đúp vào 'LAY_MA_MAY.bat' để lấy mã máy gửi Thầy Thiện.
echo    2. Sau khi có Key, nhấp đúp vào 'KICH_HOAT_BAN_QUYEN.bat' để kích hoạt.
echo.
pause
