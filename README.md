# 🎓 SKILL: Soạn Slide Bài Giảng Chuẩn Mực Sư Phạm Từ Giáo Án & SGK
> **Tác giả:** Thầy Nguyễn Văn Thiện  
> **Dành cho:** Trợ lý AI Antigravity / Gemini / Claude Code  
> **Định dạng xuất:** 100% Native DrawingML PowerPoint (`.pptx`) chỉnh sửa trực tiếp, không đè chữ, chuẩn mực sư phạm GDPT 2018.

---

## 🌟 TỔNG QUAN

Skill **`tao-slide-bai-giang`** hỗ trợ thầy cô giáo chuyển đổi nhanh chóng bất kỳ file **Giáo án (Word, PDF)**, **Sách giáo khoa (SGK)** hoặc **Kịch bản tự soạn** thành một bộ slide PowerPoint bài giảng trình chiếu chuyên nghiệp, chuẩn mực sư phạm và tối ưu cho học sinh tiếp thu trên lớp.

---

## 💎 6 NGUYÊN TẮC VÀNG CỦA BÀI GIẢNG

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

---

## 🚀 3 LUỒNG HOẠT ĐỘNG THÔNG MINH

### 📌 Luồng tương tác mở đầu:
Khi giáo viên gõ: *"Tôi muốn làm pptx"*, *"Tôi muốn tạo slide"*...  
Trợ lý sẽ tự động gửi lời chào, **4 lưu ý quan trọng** và hỏi giáo viên chọn:
- **[Phím 1]** Có File Giáo án (Word / PDF)
- **[Phím 2]** Có File Sách giáo khoa (PDF / ảnh chụp SGK)
- **[Phím 3]** Đã có kịch bản/nội dung từng slide cụ thể

---

### 🔹 Luồng 1: Từ File Giáo Án (Word / PDF)
- **Quy trình**: Đọc giáo án $\to$ Tự động lọc bỏ phần hành chính $\to$ Lập **Bảng kế hoạch chi tiết từng slide** gửi giáo viên duyệt $\to$ Giáo viên duyệt **OK** mới tạo slide.

### 🔹 Luồng 2: Từ File Sách Giáo Khoa (SGK)
- **Quy trình**: Đọc SGK $\to$ Bóc tách ảnh, biểu đồ, thí nghiệm $\to$ Lên kịch bản sư phạm 3 bước $\to$ Lập **Bảng kế hoạch slide** gửi giáo viên duyệt $\to$ Giáo viên duyệt **OK** mới tạo slide.

### 🔹 Luồng 3: Từ Kịch bản Có Sẵn
- **Quy trình**: Giáo viên gửi kịch bản (chat hoặc file text/Word) $\to$ Trợ lý làm đúng 100% nội dung, tự tìm ảnh nét / vẽ sơ đồ vector và **xuất thẳng file PPTX luôn** (không qua bước duyệt kế hoạch).

---

## 📦 CÁCH CÀI ĐẶT SKILL

Sao chép thư mục `tao-slide-bai-giang` vào thư mục kỹ năng của Antigravity hoặc Gemini:

```bash
# Trên Windows:
copy tao-slide-bai-giang C:\Users\<Username>\.gemini\config\skills\tao-slide-bai-giang
```

---

## 🛠️ CÔNG CỤ ĐI KÈM

- `patch_fonts.py`: Công cụ tự động vá theme và XML DrawingML sau khi xuất file, đảm bảo thanh ribbon của mọi phiên bản PowerPoint đều hiển thị chuẩn xác **Times New Roman** ở đúng các cỡ **22pt, 20pt, 18pt**.

---

© 2026 Thầy Nguyễn Văn Thiện. All rights reserved.
