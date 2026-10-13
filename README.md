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

9. **Đa dạng Phong cách chủ đề (5 Theme Styles) & Đa dạng Bố cục (6 Layout Patterns chuẩn STEM_MHHTH_v6)**:
   - Cho phép giáo viên chọn hoặc trợ lý tự động phối hợp **5 phong cách bảng màu chủ đề** khác nhau.
   - Luân chuyển linh hoạt **6 kiểu bố cục hiện đại** trong cùng một bài giảng và dùng ký hiệu `▸` cho mọi danh sách.

---

## 🎨 5 PHONG CÁCH CHỦ ĐỀ MÀU SẮC (5 THEME STYLES)

| Mã Phong Cách | Tên Phong Cách | Nền Slide | Màu Header & Footer | Chỉ Điểm Nhấn (6px) | 4 Màu Thẻ Phân Nhóm | Phù Hợp Nhất Cho |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| **Style 1** | **STEM Modern Navy & Gold** *(Chuẩn STEM_v6)* | `#F0F5FB` | `#1B3A6B` | `#E8941A` | Đỏ `#C0392B`, Cam `#E8941A`, Ngọc `#16A085`, Lam `#1B3A6B` | Toán, Vật lí, Hoạt động STEM, Báo cáo |
| **Style 2** | **Bio-Nature Emerald** *(Xanh Sinh Học)* | `#F2F9F6` | `#0F5132` | `#F59E0B` | Lá `#198754`, Cam `#D97706`, Biển `#0284C7`, Tím `#7C3AED` | Sinh học, KHTN (Tế bào, Sinh thái) |
| **Style 3** | **Chem-Lab Royal Purple** *(Tím Hoá Học)* | `#F5F3FF` | `#3B0764` | `#06B6D4` | Tím `#6D28D9`, Cyan `#0891B2`, Hồng `#BE185D`, Cam `#EA580C` | Hóa học, KHTN (Chất, Nguyên tử) |
| **Style 4** | **Classic Academic Light** *(Học Thuật Sáng)* | `#F8FAFC` | Badge `#EBF3FA` | `#3B82F6` | Xanh `#1F4E79`, Vàng `#F59E0B`, Lục `#10B981`, Tím `#6366F1` | Bài giảng lý thuyết truyền thống |
| **Style 5** | **Warm Terracotta** *(Năng Động Ấm Áp)* | `#FFFDF9` | `#7C2D12` | `#FBBF24` | Cam `#EA580C`, Rêu `#15803D`, Lam `#1D4ED8`, Đỏ `#B91C1C` | Khởi động, Trò chơi, Lịch sử, Địa lí |

---

## 📐 6 KIỂU BỐ CỤC HIỆN ĐẠI (6 LAYOUT PATTERNS TỪ STEM_MHHTH_v6)

1. **Layout 1 (`Split Visual-Pedagogy`)**: Trái Kênh hình lớn (45%) – Phải Hộp Câu hỏi thảo luận & Khung Em cần ghi nhớ (55%).
2. **Layout 2 (`2x2 Color-Coded Grid`)**: Lưới 4 ô vuông/chữ nhật với 4 màu tiêu đề khác nhau (`#C0392B`, `#E8941A`, `#16A085`, `#1B3A6B`) và nền pastel dịu mắt.
3. **Layout 3 (`3-Row Numbered Cards`)**: 3 dải thẻ ngang xếp tầng, có ô số thứ tự lớn (`1`, `2`, `3`) in đậm trên nền màu đặc bên trái.
4. **Layout 4 (`Horizontal Process Flow`)**: Sơ đồ quy trình chuỗi hộp ngang nối nhau bằng mũi tên `▶` chuyển màu trực quan.
5. **Layout 5 (`Concept Label Stripes`)**: Bảng dải băng nhãn màu bên trái + hộp trắng giải thích chức năng/vai trò bên phải.
6. **Layout 6 (`Comparison Table & Big Stat Cards`)**: Bảng đối chiếu 3 cột (tô nền xanh lá `#D4EDDA` cột kết quả) hoặc Thẻ số liệu lớn (`44pt`).

---

## 📸 3 NGUỒN HÌNH ẢNH ĐƯỢC HỖ TRỢ VÀ TỐI ƯU

| Nguồn hình ảnh | Cách thức cung cấp | Cách AI xử lý | Ưu điểm |
|:---|:---|:---|:---|
| **1. Bóc tách từ SGK (PDF) / Word / Ảnh chụp** | Đính kèm file PDF SGK, Word giáo án hoặc ảnh chụp điện thoại | Dùng `source_to_md.py` trích xuất ảnh gốc, khóa tỉ lệ chống méo | Chuẩn 100% SGK học sinh đang học, quen thuộc |
| **2. Kho ảnh thư mục máy tính** | Nhắn đường dẫn thư mục ảnh trên máy (ví dụ `D:\anh_tebao\`) | Tự động quét file ảnh, đối chiếu và gán vào slide phù hợp | Tận dụng tối đa ảnh thí nghiệm thực tế của trường |
| **3. Ảnh thực tế / Hiển vi từ Web** | Nhờ AI tìm ảnh thực tế/hiển vi của đối tượng | Dùng `image_search.py` tải ảnh CC mở từ Openverse/Wikimedia | Ảnh chụp thật siêu nét (2000px–4000px), an toàn bản quyền |

---

## 📂 HƯỚNG DẪN CHI TIẾT 3 CÁCH ĐƯA FILE GIÁO ÁN / SGK / ẢNH VÀO CHO AI

Khi bắt đầu gõ *"Tôi muốn làm pptx"*, trợ lý sẽ tự động hướng dẫn thầy cô **3 cách đưa tài liệu cực dễ**:

1. **Cách A — Kéo thả trực tiếp vào ô chat:**
   - Mở thư mục máy tính, giữ chuột trái vào file **Giáo án (`.docx`, `.pdf`)**, **SGK (`.pdf`)** hoặc **Ảnh chụp** rồi **kéo thả thẳng vào ô nhập tin nhắn** (hoặc bấm nút đính kèm `📎` / `+`).
2. **Cách B — Copy đường dẫn file trên máy tính (Nhanh nhất với file PDF/Word nặng):**
   - **Bước 1:** Mở thư mục chứa file trên máy tính (ví dụ trong `Downloads` hoặc `Ổ D:`).
   - **Bước 2:** Nhấp **Chuột phải** vào file cần dùng $\to$ chọn **"Copy as path"** *(Sao chép dưới dạng đường dẫn)* — hoặc bấm vào file rồi nhấn phím tắt `Ctrl + Shift + C`.
   - **Bước 3:** Quay lại ô chat, nhấn `Ctrl + V` để dán đường dẫn vào câu lệnh (Ví dụ: `"D:\GiaoAn\KHTN6_Bai17.docx"`).
3. **Cách C — Gom ảnh vào 1 thư mục riêng trên máy tính:**
   - **Bước 1:** Tạo 1 thư mục mới trên ổ D (ví dụ: `D:\anh_bai17`).
   - **Bước 2:** Copy (`Ctrl + C`) các ảnh chụp thí nghiệm, ảnh cắt từ SGK rồi dán (`Ctrl + V`) vào thư mục `D:\anh_bai17`.
   - **Bước 3:** Nhắn đường dẫn `D:\anh_bai17` vào câu lệnh để AI tự động quét và chèn vào slide.

---

## ✨ HIỆU ỨNG SƯ PHẠM BẤM CHUỘT, NÚT ĐÁP ÁN & MORPH (`animations.json`)

- **Mức `Vừa` (Mặc định chuẩn sư phạm)**: Mở trang chỉ hiện **Kênh hình** $\to$ Bấm chuột lần 1 hiện **Câu hỏi thảo luận** (`on-click`) $\to$ Bấm chuột lần 2 hiện **Em cần ghi nhớ**; ở phần Luyện tập có nút bấm **"Xem đáp án"** (`trigger_shape`).
- **Mức `Nhiều` (Có hiệu ứng `Morph` biến hình)**: Tự động thiết kế 2 slide liên tiếp có định danh ghép cặp `!!<tên_nhóm>` để **phóng to (Zoom-in) chi tiết sơ đồ/tế bào** hoặc **biến đổi trước–sau thí nghiệm** cực kỳ mượt mà.

---

## 🇬🇧 CHẾ ĐỘ CHUYÊN BIỆT CHO MÔN TIẾNG ANH (ENGLISH MODE)

Hỗ trợ trọn vẹn các bộ sách *Global Success, i-Learn Smart World, Friends Plus...*:
- Hiển thị chuẩn 100% ký tự **Phiên âm Quốc tế IPA (`/ˈnætʃ.ər.əl/`, `/θɪŋk/`)** bằng font `Times New Roman` kèm ảnh **Visual Flashcard**.
- Tự động dùng tiến trình & nhãn tiêu đề chuẩn Tiếng Anh: `Warm-up` $\to$ `🔤 NEW VOCABULARY` $\to$ `📐 GRAMMAR FOCUS (+)/(-)/(?)` $\to$ `🎯 PRACTICE (TASK 1, 2, 3)` $\to$ `💬 LET'S TALK / WORK IN PAIRS` $\to$ `💡 REMEMBER!`.

---

## 💬 CẨM NANG MẪU CÂU LỆNH GỢI Ý TỪNG BƯỚC (COPY DÙNG NGAY)

### 📌 Mẫu 1: Làm từ File Giáo án / PDF SGK (Bóc tách ảnh gốc + Hiệu ứng Morph)
```text
Làm cho tôi slide từ file "D:\GiaoAn\Bai17_CauTaoTeBao.pdf" (hoặc file đính kèm). Môn KHTN 6, bộ Kết nối tri thức, 1 tiết, Trường THCS Ứng Hòe, GV: Nguyễn Văn Thiện, Phong cách Style 2 (Xanh Sinh học), Hiệu ứng mức Nhiều (có Morph phóng to tế bào). Nhớ bóc tách đúng các hình 17.1, 17.2 trong file vào slide và lên Bản phác thảo Storyboard chi tiết cho tôi duyệt trước nhé!
```

### 📌 Mẫu 2: Kết hợp Giáo án + Thư mục ảnh riêng đã copy trên máy tính
```text
Soạn slide bài Cấu tạo tế bào, KHTN 6 bộ Cánh Diều, Trường THCS Ứng Hòe, GV: Nguyễn Văn Thiện, Phong cách Style 1 (STEM Navy), Hiệu ứng mức Vừa. Nội dung lấy từ file "D:\GiaoAn\Bai17.docx", còn hình ảnh minh hoạ em lấy toàn bộ trong thư mục "D:\anh_bai17" đưa vào các slide tương ứng. Lên bản phác thảo cho tôi xem trước nhé!
```

### 📌 Mẫu 3: Nhờ AI tự tìm ảnh thực tế / hiển vi siêu nét từ Web
```text
Soạn slide bài 17 Cấu tạo tế bào, KHTN 6 Kết nối tri thức, Trường THCS Ứng Hòe, GV: Nguyễn Văn Thiện, Phong cách Style 1, Hiệu ứng mức Vừa. Ở các slide quan sát, em tự tìm giúp tôi ảnh chụp tế bào vảy hành thật và tế bào biểu bì dưới kính hiển vi độ nét cao từ trên mạng nhé. Lập bản phác thảo Storyboard cho tôi duyệt trước!
```

### 📌 Mẫu 4: Dành cho môn Tiếng Anh (Global Success / Smart World / Friends Plus)
```text
Soạn slide Tiếng Anh lớp 7 Unit 4: Music and Arts - Lesson Getting Started, từ file SGK "D:\English7_GlobalSuccess.pdf" trang 40-41. Trường THCS Ứng Hòe, GV: Nguyễn Văn Thiện, Phong cách Style 5. Nhớ lập bảng Vocabulary có phiên âm quốc tế IPA /.../ kèm ảnh Flashcard, khung Grammar rõ ràng và hiệu ứng bấm nút hiện đáp án cho các Task nhé!
```

### 📌 Mẫu 5: Dành cho môn có Công thức (Toán – Vật Lí – Hóa Học – KHTN)
```text
Soạn slide Vật Lí 9 bài 1 "Sự phụ thuộc của điện trở vào chiều dài dây dẫn", từ file "D:\VatLi9_Bai1.pdf". Trường THCS Ứng Hòe, GV: Nguyễn Văn Thiện, Phong cách Style 1 (STEM Navy), Hiệu ứng mức Vừa. Các công thức như R = ρl/A, U = I·R cần hiển thị đẹp và rõ ràng trong khung Em cần ghi nhớ nhé! Lên Storyboard cho tôi duyệt trước!
```

---

## 🔢 HIỂN THỊ CÔNG THỨC TOÁN HỌC & KHOA HỌC (Toán – Lí – Hóa – KHTN)

Bộ skill hỗ trợ **3 cấp độ hiển thị công thức**, tự động áp dụng theo độ phức tạp:

| Cấp độ | Loại công thức | Ví dụ | Chất lượng |
| :---: | :--- | :--- | :---: |
| **Cấp 1** ⚡ | Công thức đơn giản — ký tự Unicode toán học | `F = ma`, `v₀`, `H₂SO₄`, `CO₂`, `E = mc²`, `Δ`, `α`, `β`, `°C`, `Ω` | ✅ Hoàn hảo |
| **Cấp 2** ✏️ | Phân số đơn giản, căn thức ngắn, chỉ số phức hợp | `v̄ = Δs/Δt`, `√(b²−4ac)`, `x = (−b ± √Δ)/2a` | ✅ Đủ đẹp |
| **Cấp 3** ⭐ | Tích phân, ma trận, Sigma lồng nhau, hóa hữu cơ chuỗi dài | `∫f(x)dx`, `∑ᵢ₌₁ⁿ`, `lim_{x→∞}`, Cơ chế phản ứng hóa hữu cơ | ✅ Đẹp như LaTeX |

**Cấp 3** dùng thư viện `matplotlib` (có sẵn, không cần cài thêm) để render công thức LaTeX thành ảnh PNG 300 DPI siêu nét rồi nhúng thẳng vào slide — đảm bảo mọi công thức đều đẹp hoàn hảo dù phức tạp đến mức nào.

> ⚠️ **Lưu ý**: Công thức Cấp 3 (ảnh PNG) không thể click-to-edit trong PowerPoint, nhưng hiển thị hoàn hảo khi trình chiếu. Hãy giữ nội dung LaTeX nguồn để render lại khi cần chỉnh sửa.

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
