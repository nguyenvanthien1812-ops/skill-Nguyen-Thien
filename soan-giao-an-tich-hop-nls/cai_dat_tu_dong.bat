@echo off
chcp 65001 >nul
title Cai Dat Tu Dong 1-Click - Skill Soan Giao An NLS

echo.
echo ====================================================================
echo    HỆ THỐNG CÀI ĐẶT TỰ ĐỘNG 1-CLICK - SKILL SOẠN GIÁO ÁN NLS & AI
echo              Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe
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
    echo [!] May tinh chua co Python. Dang tu dong tai Python ve cai dat...
    set "PY_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe"
    set "PY_INSTALLER=%TEMP%\python-installer.exe"
    powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; (New-Object Net.WebClient).DownloadFile('%PY_URL%', '%PY_INSTALLER%')"
    if exist "%PY_INSTALLER%" (
        echo [*] Dang cai dat Python che do am tham...
        start /wait "" "%PY_INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
        del /f /q "%PY_INSTALLER%" >nul 2>nul
    )
    set "PYTHON_EXE=python"
)

echo [OK] Python da san sang!
echo [*] Dang cai dat cac thu vien can thiet (python-docx, lxml)...
%PYTHON_EXE% -m pip install --upgrade pip --quiet
%PYTHON_EXE% -m pip install python-docx lxml --quiet

echo.
echo ====================================================================
echo   🎉 [CHÚC MỪNG] CÀI ĐẶT MÔI TRƯỜNG THÀNH CÔNG!
echo ====================================================================
echo.
echo   Thầy/Cô nhấp đúp tiếp vào "NAP_VAO_ANTIGRAVITY.bat" để sử dụng!
echo.
pause
