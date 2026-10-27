@echo off
chcp 65001 >nul
title CAI DAT BO CONG CU TRO LY GIAO VIEN AI - THAY THIEN

echo.
echo ====================================================================
echo     CÀI ĐẶT BỘ CÔNG CỤ TRỢ LÝ GIÁO VIÊN AI (SOẠN GIÁO ÁN + SLIDE)
echo               Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe
echo ====================================================================
echo.
echo [*] Dang cai dat Skill 1: Soan Giao An NLS & AI...
set "DIR1=%USERPROFILE%\.gemini\config\skills\soan-giao-an-tich-hop-nls"
if not exist "%DIR1%" mkdir "%DIR1%"
xcopy "%~dp0soan-giao-an-tich-hop-nls\*" "%DIR1%\" /E /I /Y /Q >nul

echo [*] Dang cai dat Skill 2: Soan Slide Bai Giang PPTX...
set "DIR2=%USERPROFILE%\.gemini\config\skills\tao-slide-bai-giang"
if not exist "%DIR2%" mkdir "%DIR2%"
xcopy "%~dp0tao-slide-bai-giang\*" "%DIR2%\" /E /I /Y /Q >nul

echo.
echo ====================================================================
echo   🎉 [HOÀN TẤT] ĐÃ CÀI ĐẶT THÀNH CÔNG CẢ 2 SKILL VÀO ANTIGRAVITY!
echo.
echo   1. Soạn giáo án: Mở Antigravity gõ "Tôi muốn soạn giáo án..."
echo   2. Tạo slide: Mở Antigravity gõ "Tôi muốn tạo slide bài giảng..."
echo ====================================================================
echo.
pause
