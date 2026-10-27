@echo off
chcp 65001 >nul
title CAI DAT TRON BO TRO LY GIAO VIEN AI GDPT 2018 - THAY NGUYEN THIEN

echo.
echo ====================================================================
echo      CÀI ĐẶT TRỌN BỘ SIÊU TRỢ LÝ GIÁO VIÊN AI - CHUẨN GDPT 2018
echo              Tác giả: Thầy Nguyễn Văn Thiện - THCS Ứng Hòe
echo ====================================================================
echo.

echo [*] Dang cai dat Skill 1: Tao De Thi, Ma Tran & Tham Dinh De (tao-de-toan-tuong-tu)...
set "DIR1=%USERPROFILE%\.gemini\config\skills\tao-de-toan-tuong-tu"
if not exist "%DIR1%" mkdir "%DIR1%"
xcopy "%~dp0tao-de-toan-tuong-tu\*" "%DIR1%\" /E /I /Y /Q >nul

echo [*] Dang cai dat Skill 2: Soan Giao An Tich Hop NLS & AI (soan-giao-an-tich-hop-nls)...
set "DIR2=%USERPROFILE%\.gemini\config\skills\soan-giao-an-tich-hop-nls"
if not exist "%DIR2%" mkdir "%DIR2%"
xcopy "%~dp0soan-giao-an-tich-hop-nls\*" "%DIR2%\" /E /I /Y /Q >nul

echo [*] Dang cai dat Skill 3: Soan Slide Bai Giang PPTX 16:9 (tao-slide-bai-giang)...
set "DIR3=%USERPROFILE%\.gemini\config\skills\tao-slide-bai-giang"
if not exist "%DIR3%" mkdir "%DIR3%"
xcopy "%~dp0tao-slide-bai-giang\*" "%DIR3%\" /E /I /Y /Q >nul

echo [*] Dang cai dat Skill 4: Tao Video Khoi Dong Bai Hoc Veo 3 (tao-video-khoi-dong-bai-hoc)...
set "DIR4=%USERPROFILE%\.gemini\config\skills\tao-video-khoi-dong-bai-hoc"
if not exist "%DIR4%" mkdir "%DIR4%"
xcopy "%~dp0tao-video-khoi-dong-bai-hoc\*" "%DIR4%\" /E /I /Y /Q >nul

echo.
echo ====================================================================
echo   🎉 [HOÀN TẤT] ĐÃ CÀI ĐẶT THÀNH CÔNG TRỌN BỘ 4 SKILL VÀO ANTIGRAVITY!
echo.
echo   Mở Google Antigravity lên và trải nghiệm ngay:
echo   1. Tạo đề / Thẩm định đề: Nhắn "Tạo đề tương tự..." hoặc "Thẩm định đề thi..."
echo   2. Soạn giáo án NLS:     Nhắn "Tôi muốn soạn giáo án..." hoặc kéo thả file Word
echo   3. Tạo slide bài giảng:  Nhắn "Tạo slide bài giảng..." hoặc kéo thả SGK
echo   4. Video khởi động:      Nhắn "Tôi muốn tạo video khởi động..."
echo ====================================================================
echo.
pause
