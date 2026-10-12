# 🎓 SKILL-NGUYEN-THIEN: Bộ Skill Chuẩn Mực Sư Phạm Của Thầy Nguyễn Văn Thiện
> **Tác giả:** Thầy Nguyễn Văn Thiện — Trường THCS Ứng Hòe  
> **Dành cho:** Trợ lý AI Antigravity / Gemini / Claude Code  
> **Định dạng xuất:** 100% Native DrawingML PowerPoint (`.pptx`) chỉnh sửa trực tiếp, không đè chữ, chuẩn mực sư phạm GDPT 2018.

---

## 🌟 TỔNG QUAN

Kho lưu trữ các Skill chuyên biệt dành cho giáo viên và trợ lý AI Antigravity / Gemini / Claude:

1. **`tao-slide-bai-giang`**: Soạn slide PowerPoint (PPTX) bài giảng chuẩn mực sư phạm từ file Giáo án (Word, PDF) hoặc Sách giáo khoa (SGK). 100% Native DrawingML không đè chữ, chuẩn GDPT 2018, bắt buộc duyệt bản phác thảo Storyboard trước khi tạo PPTX, hỗ trợ 3 nguồn hình ảnh.
2. **`tao-video-khoi-dong-bai-hoc`**: Lên kịch bản và trọn bộ Prompt Veo 3 cho video khởi động bài học (warm-up video) 60–80 giây. Đồng nhất nhân vật thầy/cô giáo, loại bỏ hoàn toàn chữ trong video tránh lỗi font AI, an toàn chính sách kiểm duyệt 100% và không spoil đáp án trước.

---

## 🎬 1. SKILL: TẠO VIDEO KHỞI ĐỘNG BÀI HỌC VỚI VEO 3 (`tao-video-khoi-dong-bai-hoc`)

### 🚀 Tính năng nổi bật:
- **Tự động kích hoạt khi giáo viên yêu cầu**: Khi thầy cô nói *"tôi muốn làm video"*, *"tôi muốn viết kịch bản video..."*, trợ lý lập tức gửi form mẫu điền thông tin bài học hoặc tiếp nhận ảnh chụp SGK.
- **Quy trình sư phạm 3 bước**:
  1. Tiếp nhận bài học $\to$ Gợi ý 3–5 ý tưởng kịch bản độc đáo (thực tế, kịch tính, gamification...).
  2. Thầy cô chọn ý tưởng $\to$ AI xuất trọn bộ Character Seed + 6–8 Prompt Veo 3 (mỗi clip 10s).
  3. Lời thoại tiếng Việt chuẩn thời lượng ($\le$ 38 từ/clip) $\to$ Dựng hoàn thiện trên CapCut.
- **Mẹo vàng Veo 3 tích hợp sẵn**:
  - *No-Text Prompting*: Loại bỏ toàn bộ chữ trong background video để tránh AI sinh chữ rác/méo mó; chèn chữ chuẩn tiếng Việt qua CapCut.
  - *Character Consistency*: Khóa ngoại hình nhân vật (Thầy giáo 35 tuổi / Thầy giáo 28 tuổi / Cô giáo 25 tuổi) kèm kỹ thuật Reference Image.
  - *Safety Policy Bypass*: Tự động thay thế từ nhạy cảm (cắt, dao, kéo, bạo lực) bằng cử chỉ sư phạm an toàn.
  - *Không Spoil đáp án*: Giữ trọn sự tò mò của học sinh cho đến khi bước vào tiết học.

---

## 🎓 2. SKILL: SOẠN SLIDE BÀI GIẢNG CHUẨN MỰC SƯ PHẠM (`tao-slide-bai-giang`)

### 💎 8 NGUYÊN TẮC VÀNG CỦA BÀI GIẢNG

1. **Loại bỏ 100% slide hành chính rườm rà**:
   - Tuyệt đối không đưa các phần: *"Mục tiêu bài học", "Năng lực số và AI", "Phẩm chất và năng lực", "Tiến trình dạy học", "Yêu cầu cần đạt"* vào slide.
   - Bài giảng đi thẳng vào tiến trình dạy học thực tế trên lớp: `Trang bìa` $\to$ `Khởi động` $\to$ `Hình thành kiến thức mới` $\to$ `Luyện tập` $\to$ `Vận dụng & Dặn dò`.

2. **Không để dòng chữ bé dưới đề mục**:
   - Tiêu đề slide to rõ, trang trọng, có đường phân cách thanh mảnh, để không gian thoáng đãng cho bài học phía dưới. Không chèn dòng subtitle chữ nhỏ gây rối mắt.

3. **Ngôn ngữ lớp học tự nhiên (Chuẩn SGK GDPT 2018)**:
   - Thay thế hoàn toàn các thuật ngữ lý luận nội bộ:
     - ❌ *Kênh hình 11.1* $\to$ ✅ `HÌNH 11.1: [TÊN HÌNH]` hoặc `QUAN SÁT HÌNH 11.1 (SGK)`.
     - ❌ *Câu hỏi phát vấn* $\to$ ✅ `CÂU HỎI THẢO LUẬN` hoặc `❓ THẢO LUẬN NHÓM/CẶP ĐÔI`.
     - ❌ *Kết luận ghi vở* $\to$ ✅ `💡 EM CẦN GHI NHỚ` hoặc `💡 KIẾN THỨC TRỌNG TÂM`.

4. **Trục sư phạm trực quan 3 bước trong từng hoạt động**:
   - **Bước 1: Kênh hình trực quan**: Hình ảnh thực tế đời sống, biểu đồ khoa học, sơ đồ diễn biến thí nghiệm SGK (nửa bên trái slide).
   - **Bước 2: Câu hỏi thảo luận gợi mở**: Các câu hỏi phát vấn xung quanh kênh hình để học sinh tự tìm ra kiến thức (hộp trên bên phải).
   - **Bước 3: Khung Em cần ghi nhớ**: Hộp kiến thức nổi bật, chốt 2–3 ý cốt lõi học sinh cần chép vào vở (hộp dưới bên phải).

5. **Kỹ thuật chống lỗi đè chữ DrawingML**:
   - Hợp nhất cấu trúc inline label + value vào thẻ `<text>` chứa các `<tspan>` tuần tự, đảm bảo không bao giờ bị đè chữ trong PowerPoint.

6. **Khóa chuẩn Font chữ & Cỡ chữ bắt buộc**:
   - **Font chữ toàn bài**: **Times New Roman** (100% các đoạn chữ, master và theme).
   - **Tiêu đề của tiết, bài (Slide Title)**: **22 pt** (in đậm).
   - **Tiêu đề các phần / khung nội dung (Section Header)**: **20 pt** (in đậm).
   - **Nội dung bài học / thảo luận / ghi nhớ (Body text)**: **18 pt** (học sinh ngồi cuối lớp nhìn rõ mồn một).
   - **Chú thích ảnh, số trang, tag trường (Footer/Tag)**: **14 pt**.

7. **Bắt buộc lập Bản phác thảo chi tiết (Storyboard) từng slide duyệt trước khi tạo PPTX**:
   - Khi có file giáo án, file SGK hoặc tài liệu giảng dạy, trợ lý **bắt buộc** phải lập bản phác thảo chi tiết từng slide (mô tả rõ Kênh hình, Câu hỏi phát vấn, Khung ghi nhớ, Lời giảng GV) để giáo viên duyệt.
   - Dừng lại chờ giáo viên bấm duyệt (OK / Đồng ý) thì mới khởi tạo và xuất file PPTX.

8. **Cơ chế linh hoạt tiếp nhận & xử lý 3 nguồn hình ảnh**:
   - Slide không làm toàn chữ, nhưng không chèn ảnh hoạt hình vô nghĩa.
   - Hỗ trợ mượt mà 3 nguồn ảnh: (1) Bóc tách trực tiếp từ PDF SGK/ảnh chụp điện thoại; (2) Lấy ảnh từ thư mục riêng trên máy tính; (3) Tự động tìm kiếm ảnh thực tế/hiển vi khoa học chất lượng cao từ Web (Openverse & Wikimedia).

---

## 📸 3 NGUỒN HÌNH ẢNH ĐƯỢC HỖ TRỢ VÀ TỐI ƯU

| Nguồn hình ảnh | Cách thức cung cấp | Cách AI xử lý | Ưu điểm |
|:---|:---|:---|:---|
| **1. Bóc tách từ SGK (PDF) / Word / Ảnh chụp** | Đính kèm file PDF SGK, Word giáo án hoặc ảnh chụp điện thoại | Dùng `source_to_md.py` trích xuất ảnh gốc, khóa tỉ lệ chống méo | Chuẩn 100% SGK học sinh đang học, quen thuộc |
| **2. Kho ảnh thư mục máy tính** | Nhắn đường dẫn thư mục ảnh trên máy (ví dụ `D:\anh_tebao\`) | Tự động quét file ảnh, đối chiếu và gán vào slide phù hợp | Tận dụng tối đa ảnh thí nghiệm thực tế của trường |
| **3. Ảnh thực tế / Hiển vi từ Web** | Nhờ AI tìm ảnh thực tế/hiển vi của đối tượng | Dùng `image_search.py` tải ảnh CC mở từ Openverse/Wikimedia | Ảnh chụp thật siêu nét (2000px–4000px), an toàn bản quyền |

---

## 💬 CẨM NANG MẪU CÂU LỆNH GỢI Ý THẦY CÔ CÓ THỂ DÙNG NGAY

Khi mở đầu với: *"Tôi muốn làm pptx"*, *"Tạo slide cho tôi"*..., trợ lý sẽ gợi ý sẵn các mẫu câu lệnh sau:

### 📌 Mẫu 1: Dùng ảnh bóc tách từ SGK
```
Soạn slide bài 17 Cấu tạo tế bào, SGK KHTN 6 Kết nối tri thức từ trang 60 đến 63. Trường THCS Ứng Hoè, GV: Nguyễn Văn Thiện, Tiết 1. Nhớ bóc tách đúng các hình 17.1, 17.2 trong sách vào slide cho tôi nhé!
```

### 📌 Mẫu 2: Dùng ảnh trong thư mục máy tính
```
Soạn slide bài Cấu tạo tế bào KHTN 6 Cánh Diều. Trường THCS Ứng Hoè, GV: Nguyễn Văn Thiện. Ảnh minh hoạ lấy từ thư mục D:\anh_tebao\ đưa vào các slide tương ứng giúp tôi nhé!
```

### 📌 Mẫu 3: Nhờ AI tìm ảnh thực tế / hiển vi nét cao từ Web
```
Soạn slide bài Cấu tạo tế bào KHTN 6. Ở phần thực hành quan sát, tìm giúp tôi ảnh chụp tế bào vảy hành thật và tế bào biểu bì dưới kính hiển vi độ nét cao nhé!
```

---

## 📦 CÁCH CÀI ĐẶT & SỬ DỤNG BỘ SKILL

### Cách 1: Sử dụng trực tiếp trong Antigravity / Gemini CLI
Sao chép thư mục `tao-slide-bai-giang` vào thư mục kỹ năng của hệ thống:

```bash
# Trên Windows:
xcopy /E /I tao-slide-bai-giang C:\Users\<Username>\.gemini\config\skills\tao-slide-bai-giang
```

### Cách 2: Đồng bộ tự động qua Git
```bash
git clone https://github.com/nguyenvanthien1812-ops/skill-Nguyen-Thien.git
```

---

## 🛠️ CÔNG CỤ ĐI KÈM

- `patch_fonts.py`: Công cụ tự động vá theme và XML DrawingML sau khi xuất file, đảm bảo thanh ribbon của mọi phiên bản PowerPoint đều hiển thị chuẩn xác **Times New Roman** ở đúng các cỡ **22pt, 20pt, 18pt**.

---

© 2026 Thầy Nguyễn Văn Thiện — Trường THCS Ứng Hòe. All rights reserved.
