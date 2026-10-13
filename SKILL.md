---
name: tao-slide-bai-giang
description: >-
  Soạn slide PowerPoint (PPTX) bài giảng dạy học chuẩn mực sư phạm từ file Giáo án (Word, PDF) hoặc Sách giáo khoa (SGK).
  Tự động lọc bỏ các slide hành chính rườm rà (Mục tiêu, Năng lực số, Yêu cầu cần đạt), đi thẳng vào tiến trình dạy học trực quan 3 bước:
  Quan sát hình ảnh/SGK → Câu hỏi thảo luận phát vấn → Khung Em cần ghi nhớ (chốt kiến thức ghi vở).
  Đảm bảo ngôn ngữ lớp học chuẩn mực (không dùng từ lý luận như "kênh hình", "câu hỏi phát vấn", "học sinh ghi vào vở"),
  không để dòng chữ bé rườm rà dưới đề mục, chống triệt để lỗi đè chữ DrawingML trong PowerPoint và xuất file 100% Native DrawingML chỉnh sửa trực tiếp được.
  Kích hoạt khi giáo viên yêu cầu: "tôi muốn làm pptx", "tôi muốn tạo pptx", "tôi muốn làm slide", "tôi muốn tạo slide",
  "làm pptx", "tạo pptx", "làm slide", "tạo slide", "soạn slide", "tạo slide bài giảng", "làm pptx từ giáo án",
  "soạn slide khtn", "làm slide bài dạy", "tạo bài giảng pptx", "làm slide từ pdf", "tạo slide chuẩn sư phạm",
  "soạn pptx bài giảng", "làm pptx từ sách giáo khoa", "soạn bài giảng powerpoint", "tôi có kịch bản slide rồi",
  "làm theo kịch bản của tôi", "tôi đã soạn sẵn nội dung", "chỉ cần chèn ảnh vào slide".
---

# 🎓 SKILL: Soạn Slide Bài Giảng Chuẩn Mực Sư Phạm Từ Giáo Án & SGK

## I. MỤC TIÊU & NGUYÊN TẮC CỐT LÕI

Skill này được thiết kế chuyên biệt để hỗ trợ giáo viên chuyển đổi bất kỳ giáo án (Word, PDF), nội dung Sách giáo khoa (SGK) hoặc kịch bản tự soạn thành một bộ slide PowerPoint bài giảng trình chiếu chuyên nghiệp, chuẩn mực sư phạm và tối ưu cho học sinh tiếp thu trên lớp.

### 9 Nguyên tắc vàng:
1. **Loại bỏ 100% slide hành chính rườm rà**:
   - Tuyệt đối **không** tạo các slide: "Mục tiêu bài học", "Năng lực số và AI", "Phẩm chất và năng lực", "Tiến trình dạy học", "Yêu cầu cần đạt".
   - Bộ slide trình chiếu chỉ phục vụ học sinh trên lớp, đi thẳng từ:
     `Trang bìa` $\to$ `Khởi động` $\to$ `Hình thành kiến thức` $\to$ `Luyện tập` $\to$ `Vận dụng & Dặn dò`.
2. **Không để dòng chữ bé dưới đề mục slide**:
   - Dưới tiêu đề slide/đề mục **không thêm bất kỳ dòng chữ phụ nhỏ (subtitle)** nào.
   - Tiêu đề slide phải to rõ (22pt), đậm nét, trang trọng, có đường phân cách thanh mảnh và để không gian thoáng đãng cho bài học phía dưới.
3. **Ngôn ngữ sư phạm lớp học tự nhiên (Chuẩn SGK GDPT 2018)**:
   - **Cấm dùng** các từ ngữ lý luận sư phạm nội bộ giáo viên:
     - ❌ *Kênh hình 11.1* $\to$ Thay bằng: ✅ `HÌNH 11.1: [TÊN HÌNH]` hoặc `QUAN SÁT HÌNH 11.1 (SGK)`.
     - ❌ *Câu hỏi phát vấn học sinh* $\to$ Thay bằng: ✅ `CÂU HỎI THẢO LUẬN` hoặc `❓ THẢO LUẬN NHÓM/CẶP ĐÔI`.
     - ❌ *Kết luận học sinh ghi vào vở / Kết luận chốt bài* $\to$ Thay bằng: ✅ `💡 EM CẦN GHI NHỚ` hoặc `💡 KIẾN THỨC TRỌNG TÂM`.
4. **Trục sư phạm trực quan 3 bước trong từng hoạt động**:
   - **Bước 1: Kênh hình trực quan**: Hình ảnh thực tế đời sống, biểu đồ khoa học, hoặc sơ đồ thí nghiệm SGK (có chú thích rõ ràng).
   - **Bước 2: Câu hỏi thảo luận gợi mở**: Các câu hỏi phát vấn gắn chặt với hình ảnh/thí nghiệm vừa quan sát để dẫn dắt học sinh tự tìm ra kiến thức.
   - **Bước 3: Khung Em cần ghi nhớ**: Hộp nội dung nổi bật, chốt ngắn gọn 2–3 ý cốt lõi học sinh cần ghi nhớ và chép vào vở.
5. **Kỹ thuật chống lỗi đè chữ DrawingML (PowerPoint Engine)**:
   - Trong định dạng DrawingML PPTX, **không bao giờ** đặt 2 thẻ `<text>` ở tọa độ cố định cạnh nhau để giả lập inline label + value.
   - **Bắt buộc** hợp nhất vào 1 thẻ `<text>` chứa các `<tspan>` tuần tự.
6. **Quy chuẩn Font chữ & Cỡ chữ bắt buộc (Chuẩn giảng dạy THCS/THPT)**:
   - **Font chữ toàn bài**: **Times New Roman** (`Times New Roman, serif`).
   - **Quy đổi DPI bắt buộc (PowerPoint Display Engine)**:
     - PowerPoint hiển thị cỡ chữ theo đơn vị Point (`pt`), trong khi SVG định nghĩa theo pixel (`px`).
     - Tỉ lệ chuẩn của bộ chuyển đổi: `1 px = 0.75 pt` $\implies$ `px = pt / 0.75`.
     - **Tiêu đề của tiết, bài (Slide Title)**: Hiển thị **22pt** $\to$ SVG ghi `font-size="29.33"` (`sz="2200"`).
     - **Tiêu đề các phần / thẻ / khung nội dung (Section Header)**: Hiển thị **20pt** $\to$ SVG ghi `font-size="26.67"` (`sz="2000"`).
     - **Nội dung bài học / câu hỏi thảo luận / ghi nhớ (Body text)**: Hiển thị **18pt** $\to$ SVG ghi `font-size="24.0"` (`sz="1800"`).
     - **Chú thích ảnh, số trang, tag trường (Caption/Footer)**: Hiển thị **14pt** $\to$ SVG ghi `font-size="18.67"` (`sz="1400"`).
   - Sau khi xuất PPTX, chạy script vá theme và run element để đảm bảo DrawingML ribbon hiển thị chuẩn xác 100% `Times New Roman`.
7. **Bắt buộc lập Bản phác thảo chi tiết (Storyboard) từng slide duyệt trước khi tạo PPTX**:
   - Khi có file giáo án, file SGK hoặc tài liệu giảng dạy, trợ lý **bắt buộc** phải lập bản phác thảo chi tiết từng slide (mô tả rõ Kênh hình, Kênh chữ/Câu hỏi, Khung ghi nhớ, Lời giảng GV) để giáo viên duyệt.
   - **Tuyệt đối không chạy lệnh tạo slide hay init project** khi chưa có sự phản hồi đồng ý của giáo viên.
8. **Cơ chế linh hoạt tiếp nhận & xử lý 3 nguồn hình ảnh**:
   - Bài giảng không làm bài toàn chữ, nhưng không chèn ảnh trang trí vô nghĩa.
   - Xử lý mượt mà cả 3 nguồn ảnh: (1) Bóc tách trực tiếp từ PDF SGK/ảnh chụp điện thoại; (2) Lấy ảnh từ thư mục riêng trên máy giáo viên; (3) Tự động tìm kiếm ảnh thực tế/hiển vi khoa học chất lượng cao từ web (Openverse & Wikimedia).
9. **Đa dạng Phong cách chủ đề (5 Theme Styles) & Đa dạng Bố cục (6 Layout Patterns chuẩn STEM_MHHTH_v6)**:
   - Cho phép giáo viên chọn hoặc trợ lý tự động phối hợp **5 phong cách bảng màu chủ đề** khác nhau (STEM Navy-Gold, Bio-Nature Emerald, Chem-Lab Purple-Cyan, Classic Academic, Warm Terracotta).
   - Không lặp lại 1 bố cục đơn điệu: Trong một bài giảng (8–12 slide), bắt buộc luân chuyển linh hoạt **6 kiểu bố cục hiện đại** (Split 2 cột, Lưới 2×2 4 màu phân biệt, 3 Dải thẻ ngang đánh số lớn, Sơ đồ quy trình mũi tên ngang `▶`, Bảng dải băng nhãn màu, Bảng đối chiếu & Thẻ số liệu lớn) và sử dụng ký hiệu `▸` cho mọi danh sách.

---

## II. LUỒNG TƯƠNG TÁC GỢI Ý (KHI GIÁO VIÊN BẮT ĐẦU VỚI "TÔI MUỐN LÀM PPTX")

Khi giáo viên gửi câu lệnh mở đầu chung chung như:
> *"Tôi muốn làm pptx"*, *"Tôi muốn tạo pptx"*, *"Tôi muốn làm slide"*, *"Làm slide cho tôi"*, *"Tạo bài giảng pptx"*... (chưa đính kèm tài liệu cụ thể)

Trợ lý **bắt buộc không được tự ý tạo bài ngay**, mà phải thực hiện đúng luồng hướng dẫn 3 bước sau:

### BƯỚC 1: Phản hồi Lời chào, Hướng dẫn cách đưa File/Ảnh & Cú pháp mẫu chi tiết
Trợ lý gửi ngay phản hồi nguyên văn, đầy đủ và chi tiết theo mẫu sau:

```markdown
Dạ kính chào thầy/cô! Để em hỗ trợ soạn bộ slide PowerPoint (`.pptx`) đẹp mắt, chuẩn sư phạm GDPT 2018 (Font Times New Roman 22–20–18pt, không đè chữ, 6 bố cục hiện đại), thầy/cô làm theo hướng dẫn từng bước rất đơn giản dưới đây nhé:

---
### 📂 BƯỚC CHUẨN BỊ: 3 CÁCH ĐƯA FILE GIÁO ÁN / SGK / ẢNH VÀO CHO EM ĐỌC

Thầy/cô có thể chọn **1 trong 3 cách** tiện nhất trên máy tính:
1. **Cách A — Kéo thả trực tiếp vào ô chat:**
   - Mở thư mục máy tính, giữ chuột trái vào file **Giáo án (`.docx`, `.pdf`)**, **SGK (`.pdf`)** hoặc **Ảnh chụp** rồi **kéo thả thẳng vào ô nhập tin nhắn** này (hoặc bấm nút đính kèm `📎` / `+`).
2. **Cách B — Copy đường dẫn file trên máy tính (Nhanh nhất với file PDF/Word nặng):**
   - **Thao tác 1:** Mở thư mục chứa file trên máy tính (ví dụ trong `Downloads` hoặc `Ổ D:`).
   - **Thao tác 2:** Nhấp **Chuột phải** vào file cần dùng $\to$ chọn **"Copy as path"** *(Sao chép dưới dạng đường dẫn)* — hoặc bấm vào file rồi nhấn phím tắt `Ctrl + Shift + C`.
   - **Thao tác 3:** Quay lại ô chat này, nhấn `Ctrl + V` để dán đường dẫn vào câu lệnh (Ví dụ: `"D:\GiaoAn\KHTN6_Bai17.docx"`).
3. **Cách C — Gom ảnh vào 1 thư mục trên máy tính (Khi thầy/cô có nhiều ảnh riêng):**
   - **Thao tác 1:** Tạo 1 thư mục mới trên ổ D (ví dụ: `D:\anh_bai17`).
   - **Thao tác 2:** Copy (`Ctrl + C`) các ảnh chụp thí nghiệm, ảnh cắt từ SGK rồi dán (`Ctrl + V`) vào thư mục `D:\anh_bai17`.
   - **Thao tác 3:** Nhắn đường dẫn `D:\anh_bai17` vào câu lệnh bên dưới để em tự động quét và chèn vào slide.

---
### 🎨 CHỌN PHONG CÁCH MÀU SẮC SLIDE (5 PHONG CÁCH CHUẨN STEM):
- **Style 1:** `STEM Navy & Gold` (Header xanh đậm `#1B3A6B`, chỉ vàng cam `#E8941A` — *Mặc định cho Toán, Lí, STEM*)
- **Style 2:** `Bio-Nature Emerald` (Xanh lục bảo `#0F5132`, vàng nắng — *Rất hợp Sinh học, Tế bào, KHTN*)
- **Style 3:** `Chem-Lab Royal Purple` (Tím hoàng gia `#3B0764`, xanh Cyan — *Rất hợp Hóa học, Nguyên tử*)
- **Style 4:** `Classic Academic Light` (Nền sáng thanh lịch, thẻ xanh `#1F4E79` — *Hợp bài lý thuyết nhẹ nhàng*)
- **Style 5:** `Warm Terracotta` (Đỏ cam ấm áp `#7C2D12` — *Hợp Tiếng Anh, Khởi động, Lịch sử, Địa lí*)

---
### ✨ CHỌN MỨC HIỆU ỨNG TRÌNH CHIẾU (`animations.json`):
- **Mức `Vừa` *(Mặc định chuẩn sư phạm)***: Mở trang hiện Kênh hình $\to$ Bấm chuột lần 1 hiện **Câu hỏi thảo luận** $\to$ Bấm chuột lần 2 hiện **Em cần ghi nhớ**; Bấm nút **"Xem đáp án"** ở câu trắc nghiệm.
- **Mức `Nhiều` *(Có hiệu ứng Morph biến hình)***: Như mức Vừa + Thêm hiệu ứng **Morph** phóng to chi tiết sơ đồ/tế bào hoặc biến đổi trước–sau thí nghiệm cực mượt.
- **Mức `Không`**: Hiện sẵn toàn bộ nội dung trên slide.

---
### ❓ THẦY CÔ ĐANG CÓ TÀI LIỆU DẠNG NÀO? (CHỌN PHÍM 1, 2 HOẶC 3):
- **[Phím 1]** Có **File Giáo án** (Word `.docx` hoặc `.pdf`)
- **[Phím 2]** Có **File Sách giáo khoa** (PDF SGK hoặc ảnh chụp các trang sách)
- **[Phím 3]** Đã có sẵn **Kịch bản / Nội dung từng slide**

---
### 💬 CÁC MẪU CÂU LỆNH CHI TIẾT (THẦY CÔ COPY & ĐIỀN THÔNG TIN DÙNG NGAY):

📌 **Mẫu 1 — Làm từ File Giáo án / PDF SGK (Bóc tách ảnh gốc + Hiệu ứng Vừa/Morph):**
> *"Làm cho tôi slide từ file `"D:\GiaoAn\Bai17_CauTaoTeBao.pdf"` (hoặc file đính kèm). Môn KHTN 6, bộ Kết nối tri thức, 1 tiết, Trường THCS Ứng Hòe, GV: Nguyễn Văn Thiện, Phong cách Style 2 (Xanh Sinh học), Hiệu ứng mức Nhiều (có Morph phóng to tế bào). Nhớ bóc tách đúng các hình 17.1, 17.2 trong file vào slide và lên Bản phác thảo Storyboard chi tiết cho tôi duyệt trước nhé!"*

📌 **Mẫu 2 — Kết hợp Giáo án + Thư mục ảnh riêng đã copy trên máy:**
> *"Soạn slide bài Cấu tạo tế bào, KHTN 6 bộ Cánh Diều, Trường THCS ..., GV: ..., Phong cách Style 1 (STEM Navy), Hiệu ứng mức Vừa. Nội dung lấy từ file `"D:\GiaoAn\Bai17.docx"`, còn hình ảnh minh hoạ em lấy toàn bộ trong thư mục `"D:\anh_bai17"` đưa vào các slide tương ứng. Lên bản phác thảo cho tôi xem trước nhé!"*

📌 **Mẫu 3 — Chưa có sẵn ảnh, nhờ AI tự tìm ảnh thực tế / hiển vi siêu nét từ Web:**
> *"Soạn slide bài 17 Cấu tạo tế bào, KHTN 6 Kết nối tri thức, Trường THCS ..., GV: ..., Phong cách Style 1, Hiệu ứng mức Vừa. Ở các slide quan sát, em tự tìm giúp tôi ảnh chụp tế bào vảy hành thật và tế bào biểu bì dưới kính hiển vi độ nét cao từ trên mạng nhé. Lập bản phác thảo Storyboard cho tôi duyệt trước!"*

📌 **Mẫu 4 — Dành cho môn Tiếng Anh (Global Success / Smart World / Friends Plus):**
> *"Soạn slide Tiếng Anh lớp [7] Unit [4]: [Music and Arts] - Lesson [Getting Started / A Closer Look 1], từ file SGK `"D:\English7_GlobalSuccess.pdf"` trang [40-41]. Trường THCS ..., GV: ..., Phong cách Style 5. Nhớ lập bảng Vocabulary có phiên âm quốc tế IPA `/.../` kèm ảnh Flashcard, khung Grammar rõ ràng và hiệu ứng bấm nút hiện đáp án cho các Task nhé!"*

👉 **Thầy/cô chỉ cần gõ phím `1`, `2`, `3` hoặc copy 1 trong 4 mẫu câu lệnh trên gửi cho em. Em sẽ lập ngay BẢN PHÁC THẢO CHI TIẾT TỪNG SLIDE (Kênh hình, Bố cục, Hiệu ứng, Câu hỏi, Ghi nhớ) để thầy/cô duyệt OK rồi mới xuất file PPTX ạ!**
```

> ⚠️ **BẮT BUỘC DỪNG VÀ CHỜ**: Sau khi gửi tin nhắn trên, trợ lý phải dừng lại và chờ giáo viên chọn 1, 2, 3 (hoặc gửi câu lệnh kèm đường dẫn file). Không chạy bất kỳ lệnh `project_manager.py init` hay tạo file nào lúc này.

---

### BƯỚC 2: Hướng dẫn chi tiết theo lựa chọn của giáo viên (Nếu giáo viên mới chỉ gõ số 1, 2 hoặc 3)

#### 🔹 Trường hợp 1: Giáo viên chọn số `1` (File Giáo án Word/PDF)
Trợ lý phản hồi:
```markdown
Dạ, với **File Giáo án (Word hoặc PDF)**, thầy/cô thực hiện theo 3 bước nhỏ sau nhé:

**Bước 1 — Lấy đường dẫn file Giáo án (hoặc kéo thả file):**
- Mở thư mục chứa file giáo án trên máy tính $\to$ Nhấp **Chuột phải** vào file giáo án $\to$ Chọn **"Copy as path"** *(hoặc bấm `Ctrl + Shift + C`)*.
- *(Nếu thầy/cô có thư mục ảnh riêng muốn chèn thêm, hãy gom ảnh vào 1 thư mục như `D:\anh_bai_day` rồi copy đường dẫn thư mục đó).*

**Bước 2 — Copy câu lệnh mẫu dưới đây, dán (`Ctrl + V`) đường dẫn file vào và gửi cho em:**
> "Đây là file giáo án của tôi: `"D:\Duong_dan_file_giao_an.docx"`.
> - Bài dạy: [Tên bài], Môn: [KHTN 6], Bộ sách: [Kết nối tri thức / Cánh Diều / CTST]
> - Trường: [THCS ...], Giáo viên: [Nguyễn Văn ...], Số tiết: [1 tiết]
> - Phong cách màu: [Style 1: STEM Navy / hoặc Style 2: Xanh Sinh học]
> - Nguồn ảnh: [Bóc tách ảnh có sẵn trong giáo án / hoặc Lấy từ thư mục D:\anh_bai_day / hoặc Nhờ AI tìm ảnh thực tế trên mạng]
> Em hãy đọc giáo án, bỏ các phần hành chính và lên Bản phác thảo Storyboard chi tiết từng slide cho tôi duyệt trước nhé!"

**Bước 3 — Duyệt Bản phác thảo & Nhận file PPTX:**
- Em sẽ gửi bảng phác thảo chi tiết từng slide (bố cục gì, ảnh nào, câu hỏi gì, khung ghi nhớ gì).
- Thầy/cô xem xong nhắn **"OK"** (hoặc yêu cầu sửa đổi), em sẽ xuất ngay file `.pptx` hoàn chỉnh ạ!
```

#### 🔹 Trường hợp 2: Giáo viên chọn số `2` (File Sách Giáo Khoa PDF / Ảnh chụp SGK)
Trợ lý phản hồi:
```markdown
Dạ, với **File Sách Giáo Khoa (PDF hoặc Ảnh chụp trang sách)**, thầy/cô làm theo 3 bước cực dễ sau nhé:

**Bước 1 — Đưa file SGK hoặc Ảnh chụp cho em:**
- **Nếu là file PDF SGK cả cuốn:** Nhấp **Chuột phải** vào file PDF trên máy $\to$ chọn **"Copy as path"** (`Ctrl + Shift + C`), và nhớ số trang của bài học (ví dụ: trang 60 đến 63).
- **Nếu là ảnh chụp các trang sách:** Kéo thả trực tiếp các ảnh chụp đó vào ô chat này (hoặc bỏ chung vào thư mục `D:\anh_sgk` rồi copy đường dẫn thư mục).

**Bước 2 — Copy câu lệnh mẫu dưới đây gửi cho em:**
> "Soạn slide bài giảng từ file SGK: `"D:\SGK_KHTN6_KNTT.pdf"` (từ trang [60] đến trang [63]).
> - Bài: [Bài 17: Cấu tạo tế bào], Môn: [KHTN 6], Bộ sách: [Kết nối tri thức]
> - Trường: [THCS ...], Giáo viên: [Nguyễn Văn ...], Tiết: [1]
> - Phong cách màu: [Style 1: STEM Navy & Gold / hoặc Style 2: Xanh Sinh học]
> - Yêu cầu ảnh: Bóc tách chuẩn xác các Hình [17.1, 17.2, 17.3] trong SGK đưa vào slide (và tìm thêm ảnh hiển vi thực tế trên mạng nếu cần).
> Em hãy thiết kế tiến trình 3 bước (Quan sát hình → Câu hỏi thảo luận → Em cần ghi nhớ) và lập Bản phác thảo Storyboard chi tiết cho tôi duyệt trước nhé!"

**Bước 3 — Duyệt Bản phác thảo & Nhận file PPTX:**
- Em bóc tách ảnh gốc trong sách, lên phác thảo chi tiết gửi thầy/cô xem trước. Thầy/cô duyệt **"OK"** là em xuất file PowerPoint ngay ạ!
```

#### 🔹 Trường hợp 3: Giáo viên chọn số `3` (Đã có kịch bản từng slide)
Trợ lý phản hồi:
```markdown
Dạ tuyệt vời! Với **Kịch bản có sẵn**, thầy/cô toàn quyền làm chủ nội dung, em sẽ lo phần thiết kế 6 kiểu bố cục đẹp mắt và chèn ảnh sắc nét:

**Bước 1 — Chuẩn bị nội dung & ảnh (nếu có):**
- Nếu kịch bản lưu trong file Word: Nhấp **Chuột phải** vào file $\to$ chọn **"Copy as path"** (hoặc dán thẳng chữ vào ô chat).
- Nếu có ảnh riêng muốn chèn vào từng slide: Copy các ảnh đó vào 1 thư mục (ví dụ `D:\anh_slide`) và đặt tên ảnh rõ ràng (`slide2.jpg`, `slide3.png`...).

**Bước 2 — Gửi kịch bản theo mẫu sau:**
> - Trường: [THCS ...], GV: [Nguyễn Văn ...], Lớp: [...], Bài: [...], Tiết: [...]
> - Phong cách màu: [Style 1: STEM Navy / Style 2: Xanh Sinh học / Style 3: Tím Hóa học...]
> - Thư mục ảnh đính kèm (nếu có): `"D:\anh_slide"`
> - Slide 1 (Trang bìa): [Tên bài học]
> - Slide 2 (Khởi động): [Nội dung + Ảnh muốn dùng]
> - Slide 3 (Phần I - Bố cục Lưới 4 ô hoặc Split 2 cột): [Nội dung + Ảnh]
> - Slide 4: ...

**Bước 3 — Nhận thẳng file PPTX hoàn chỉnh:**
- Vì thầy/cô đã có kịch bản chi tiết, em sẽ giữ nguyên 100% nội dung, tự động phối hợp bố cục, chèn ảnh và xuất thẳng file `.pptx` luôn mà không làm mất thời gian chờ duyệt lại ạ!
```

---

## III. QUY TRÌNH THỰC HIỆN CHI TIẾT TỪNG LUỒNG

Khi giáo viên đã gửi tài liệu cụ thể (hoặc ngay từ đầu giáo viên đã gửi file kèm yêu cầu rõ ràng), trợ lý đối chiếu và thực hiện đúng 1 trong 3 quy trình sau:

---

### QUY TRÌNH A: Từ File Giáo Án → Kế hoạch → Duyệt → PPTX

```
[A1] Đọc & phân tích file giáo án
           ↓
[A2] Trích xuất nội dung thực dạy (bỏ phần hành chính)
           ↓
[A3] Lập Bảng Kế Hoạch Slide → Trình bày cho giáo viên duyệt
           ↓
     ⏸️ DỪNG & CHỜ GIÁO VIÊN ĐỒNG Ý (hoặc chỉnh sửa)
           ↓
[A4] Khởi tạo dự án & Tìm kiếm ảnh/sơ đồ
           ↓
[A5] Sinh mã SVG từng slide theo kế hoạch đã duyệt
           ↓
[A6] Kiểm định chất lượng → Xuất PPTX → Vá font Times New Roman → Bàn giao
```

#### [A1] Đọc & phân tích giáo án:
```bash
python3 skills/ppt-master/scripts/source_to_md.py <đường_dẫn_file_giáo_án>
```

#### [A2] Quy tắc trích xuất nội dung:
- **LẤY**: Phần *Hoạt động 1, 2, 3, 4* (Tiến trình dạy học) — nội dung thực sự dạy học sinh.
- **BỎ HOÀN TOÀN**: Mục tiêu dạy học, Năng lực chung, Năng lực đặc thù, Thiết bị dạy học, Bảng ma trận năng lực số, Phụ lục hành chính.
- **GHI CHÚ** các hình ảnh/thí nghiệm/biểu đồ mà giáo án đề cập đến để chuẩn bị kênh hình.

#### [A3] Lập & Trình bày Bản Phác Thảo Chi Tiết Từng Slide (Storyboard):

Trợ lý **bắt buộc** phải lập bản phác thảo chi tiết (Storyboard) từng slide cho giáo viên xem trước. Bản phác thảo gồm 2 phần: **Bảng tổng quan** và **Chi tiết nội dung từng slide** theo mẫu:

```markdown
📋 KẾ HOẠCH & BẢN PHÁC THẢO CHI TIẾT SLIDE (STORYBOARD)
Bài học: [Tên bài] — Môn: [Môn] [Lớp] — Bộ sách: [Tên bộ sách]
Tổng dự kiến: XX slide | Thời lượng: 45 phút | Khổ: 16:9 | Font: Times New Roman
🎨 Phong cách chủ đề: [Style 1: STEM Modern Navy & Gold / hoặc Style 2: Bio-Nature Emerald...] *(Thầy cô có thể yêu cầu đổi sang 1 trong 5 Style)*

---
### 1. BẢNG TỔNG QUAN TIẾN TRÌNH & BỐ CỤC:
| Slide | Tiêu đề slide | Kiểu Bố Cục (Layout) | Kênh hình (Ảnh SGK / Thực tế / Thư mục) |
|:-----:|:--------------|:---------------------|:----------------------------------------|
| 01    | Trang bìa     | Cover Banner Đặc     | Họa tiết vector khoa học / Ảnh chủ đề   |
| 02    | Khởi động     | Layout 1 (Split 2 cột)| 2–3 ảnh thực tế đời sống / ảnh web      |
| 03    | I. [Tên phần] | Layout 3 (3 Dải đánh số)| Hình X.X SGK / Sơ đồ / Ảnh thư mục   |
| 04    | II. [Tên phần]| Layout 2 (Lưới 2×2 4 màu)| 4 ô phân loại màu sắc trực quan     |
| 05    | III. [Quy trình]| Layout 4 (Mũi tên ngang ▶)| Chuỗi các bước thí nghiệm/quy trình |
| ...   | ...           | ...                  | ...                                     |
| XX    | Vận dụng & Dặn dò | Layout 6 (Bảng & Thẻ) | Tình huống thực tế về nhà             |

---
### 2. PHÁC THẢO CHI TIẾT TỪNG SLIDE (KÊNH HÌNH & KÊNH CHỮ):

#### 🔹 Slide 01: TRANG BÌA
- **Tiêu đề:** [TÊN BÀI HỌC IN HOA]
- **Thông tin:** Trường [Tên trường] • GV: [Tên thầy cô] • Lớp [Lớp] • Tiết [Tiết]
- **Kênh hình & Bố cục:** Nền đậm sang trọng kèm viền vàng cam `#E8941A` chuẩn `STEM_v6`.

#### 🔹 Slide 02: HOẠT ĐỘNG KHỞI ĐỘNG
- **Tiêu đề & Bố cục:** KHỞI ĐỘNG: [TÊN TÌNH HUỐNG] *(Layout 1: Trái Ảnh – Phải Hỏi & Ghi nhớ)*
- **📸 Kênh hình:** [Mô tả chi tiết 2–3 ảnh: ảnh gì, nguồn từ đâu (Web Openverse/SGK/Thư mục GV)].
- **❓ Câu hỏi thảo luận:** "[Câu hỏi phát vấn gợi mở học sinh suy nghĩ]?"
- **💡 Em cần ghi nhớ (Dẫn dắt):** ▸ [Ý chốt mở ra bài học mới].
- **🎙️ Ghi chú lời giảng GV:** "[Lời thầy cô dẫn dắt học sinh vào bài học]".

#### 🔹 Slide 03: I. [TÊN MỤC BÀI HỌC]
- **Tiêu đề & Bố cục:** [I. TÊN NỘI DUNG TRỌNG TÂM] *(Layout 2: Lưới 2×2 4 màu / hoặc Layout 3: 3 Dải thẻ đánh số)*
- **📸 Kênh hình:** [Chỉ rõ: Hình X.X bóc tách từ SGK trang YY / Ảnh chụp từ thư mục GV / Sơ đồ vẽ].
- **❓ Câu hỏi thảo luận:**
  1. [Câu hỏi 1 cho học sinh quan sát hình]?
  2. [Câu hỏi 2 phát triển tư duy]?
- **💡 Em cần ghi nhớ (Chốt ghi vở):**
  - ▸ [Ý 1: Định nghĩa / đặc điểm cốt lõi].
  - ▸ [Ý 2: Vai trò / quy luật].
- **🎙️ Ghi chú lời giảng GV:** "[Lời giải thích, hướng dẫn học sinh phân tích hình ảnh]".

*(... Các slide tiếp theo trình bày chi tiết tương tự ...)*

---
💡 Thầy cô xem bản phác thảo chi tiết trên và phản hồi giúp em nhé:
- "Đồng ý / OK / Làm đi" → Em bắt đầu tạo bộ slide PPTX ngay.
- "Đổi sang phong cách [Style 1: STEM Navy / Style 2: Xanh Sinh học / Style 3: Tím Hóa học / Style 4: Sáng Học thuật / Style 5: Cam Năng động]" → Em sẽ đổi toàn bộ bảng màu.
- "Đổi bố cục slide X thành [Lưới 4 ô / 3 Dải đánh số / Quy trình mũi tên...]" → Em sẽ đổi kiểu trình bày.
- "Đổi ảnh slide X" hoặc "Sửa nội dung / Thêm / Bớt slide" → Em sẽ điều chỉnh và gửi lại bảng cập nhật.
```

> ⚠️ **BẮT BUỘC DỪNG & CHỜ**: Sau khi gửi Bản phác thảo chi tiết, **dừng lại ngay** và hỏi:  
> *"Thầy cô xem bản phác thảo chi tiết kênh hình và kênh chữ từng slide ở trên đã đúng ý chưa ạ? Thầy cô muốn chỉnh sửa gì không trước khi em bắt đầu tạo file PPTX?"*  
> **Tuyệt đối không chạy lệnh tạo slide hay init project khi chưa có phản hồi đồng ý.**

---

### QUY TRÌNH B: Từ File SGK → Kế hoạch Storyboard → Duyệt → PPTX

```
[B1] Đọc & phân tích file SGK (nhận diện hình ảnh, bảng, thí nghiệm)
           ↓
[B2] Tự lên kịch bản sư phạm chuẩn 3 bước (Quan sát → Hỏi → Ghi nhớ)
           ↓
[B3] Lập Bản Phác Thảo Storyboard Chi Tiết → Trình bày cho giáo viên duyệt
           ↓
     ⏸️ DỪNG & CHỜ GIÁO VIÊN ĐỒNG Ý (hoặc chỉnh sửa)
           ↓
[B4] Khởi tạo dự án & Chuẩn bị kênh hình (bóc tách ảnh SGK / lấy ảnh thư mục / tìm ảnh web)
           ↓
[B5] Sinh mã SVG từng slide theo kế hoạch đã duyệt
           ↓
[B6] Kiểm định chất lượng → Xuất PPTX → Vá font Times New Roman → Bàn giao
```

#### [B1] Đọc & nhận diện nội dung SGK:
```bash
python3 skills/ppt-master/scripts/source_to_md.py <đường_dẫn_file_sgk>
```
Khi đọc SGK, **chủ động nhận diện và ghi chú**:
- Các **hình ảnh, biểu đồ, bảng số liệu** trong SGK (ghi rõ: "Hình X.X: [mô tả]").
- Các **câu hỏi thảo luận** SGK đặt ra ở cuối mỗi phần.
- Các **thí nghiệm, thực hành** — cần bóc tách ảnh chụp dụng cụ hoặc vẽ sơ đồ diễn biến.
- Các **kết luận, kiến thức trọng tâm** để đưa vào khung "Em cần ghi nhớ".

#### [B2] Tự lên kịch bản sư phạm từ SGK:
Tổ chức lại theo cấu trúc sư phạm 3 bước:
- Từ mỗi **hình ảnh / biểu đồ / thí nghiệm** trong SGK $\to$ thiết kế 1 slide gồm Kênh hình + Câu hỏi + Ghi nhớ.
- Từ **câu hỏi SGK** $\to$ chuyển thành câu hỏi thảo luận nhóm/cặp đôi.
- Từ **lý thuyết** $\to$ chọn lọc 2–3 ý cốt lõi để chốt vào khung `💡 EM CẦN GHI NHỚ`.

#### [B3] Lập & Trình bày Bản Phác Thảo Storyboard (SGK):
Trình bày đầy đủ Bản phác thảo Storyboard chi tiết từng slide giống như mẫu tại mục [A3], trong đó ghi rõ từng số hiệu Hình SGK (Hình X.X, trang YY) được bố trí ở từng slide, câu hỏi thảo luận tương ứng và nội dung ghi nhớ chốt vào vở.

> ⚠️ **BẮT BUỘC DỪNG & CHỜ**: Phải dừng lại và chờ phản hồi đồng ý của giáo viên trước khi thực hiện bước [B4].

---

### QUY TRÌNH C: Từ Kịch bản Sẵn có → Thiết kế & Chèn ảnh → PPTX

```
[C1] Đọc & phân tích toàn bộ kịch bản giáo viên cung cấp
           ↓
[C2] Xác nhận nhanh thông tin hành chính (nếu thiếu)
           ↓
[C3] Khởi tạo dự án & Tìm kiếm ảnh/sơ đồ phù hợp
           ↓
[C4] Sinh mã SVG đẹp theo đúng 100% nội dung & thứ tự kịch bản
           ↓
[C5] Kiểm định chất lượng → Xuất PPTX → Vá font Times New Roman → Bàn giao
```

> ✅ **Quy trình C KHÔNG có bước duyệt kế hoạch** vì giáo viên đã tự soạn sẵn nội dung. Trợ lý đi thẳng vào thiết kế và xuất file hoàn chỉnh.

#### Nguyên tắc thiết kế theo kịch bản:
- **Giữ nguyên 100% nội dung** giáo viên đã viết — không tự ý thêm bớt ý tưởng.
- Tự động tối ưu layout, màu sắc, cỡ chữ chuẩn (22-20-18pt Times New Roman), tạo ảnh minh hoạ sắc nét.
- Nếu nội dung 1 slide quá dài, tự động tách đôi thành 2 slide phụ và báo cho giáo viên biết.

---

## IV. QUY CHUẨN XỬ LÝ 3 NGUỒN HÌNH ẢNH (SGK, THỰC TẾ, THƯ MỤC CÓ SẴN)

Để bài giảng đạt chất lượng sư phạm cao nhất, slide **không được toàn chữ** và **không chèn ảnh minh họa vô nghĩa/hoạt hình thiếu khoa học**. Trợ lý hỗ trợ và xử lý mượt mà cả 3 nguồn hình ảnh:

### 1. NGUỒN 1: Bóc tách trực tiếp từ File PDF SGK, Word Giáo án hoặc Ảnh chụp điện thoại
- **Khi nào áp dụng**: Giáo viên gửi kèm file SGK (PDF), file Giáo án (DOCX có chèn ảnh) hoặc ảnh chụp các trang sách từ điện thoại.
- **Tại sao cần dùng**: Đảm bảo hình ảnh trên slide chuẩn xác 100% theo đúng sách giáo khoa học sinh đang cầm trên tay (Hình X.X), tạo sự quen thuộc và thống nhất tuyệt đối trong tiết học.
- **Quy trình kỹ thuật**:
  1. Trích xuất toàn bộ ảnh gốc:
     ```bash
     python3 skills/ppt-master/scripts/source_to_md.py <đường_dẫn_file_pdf_hoặc_docx>
     ```
     Script sẽ tự động giải nén toàn bộ hình ảnh độ phân giải gốc vào thư mục con `extracted_images/` hoặc `images/`.
  2. Phân loại và định danh ảnh theo số hiệu hình SGK (ví dụ: `hinh_17_1_cau_tao_te_bao.png`, `hinh_17_2_te_bao_thuc_vat.png`).
  3. Chèn vào slide với cơ chế khóa tỉ lệ (chống méo hình/móp hình):
     ```xml
     <image xlink:href="images/hinh_17_1.png" x="60" y="112" width="550" height="420" preserveAspectRatio="xMidYMid meet"/>
     ```
  4. Luôn ghi chú thích ảnh chuẩn mực phía dưới:
     `<text ... font-size="18.67" fill="#64748B">Hình 17.1: Cấu tạo tế bào nhân thực (SGK KHTN 6)</text>`

### 2. NGUỒN 2: Sử dụng kho ảnh có sẵn trong thư mục trên máy tính của giáo viên
- **Khi nào áp dụng**: Giáo viên đã có sẵn thư mục ảnh tư liệu (ảnh chụp thí nghiệm thực tế tại trường, ảnh scan chất lượng cao, ảnh do tổ bộ môn sưu tầm) lưu trên ổ đĩa máy tính (ví dụ: `D:\tai_lieu_giang_day\anh_khtn6_bai17\`).
- **Cách giáo viên gửi lệnh**:
  - Giáo viên chỉ cần gửi đường dẫn thư mục:
    > *"Lấy ảnh trong thư mục D:\tai_lieu_giang_day\anh_khtn6_bai17\ đưa vào các slide tương ứng nhé!"*
  - Hoặc chép trực tiếp ảnh vào thư mục dự án `projects/<tên_dự_án>/images/`.
- **Quy trình kỹ thuật**:
  1. Trợ lý liệt kê toàn bộ file ảnh trong thư mục (`.jpg`, `.png`, `.jpeg`, `.webp`).
  2. Đối chiếu tên file hoặc nội dung ảnh với từng slide trong Bản phác thảo Storyboard.
  3. Tự động sao chép hoặc trỏ đường dẫn ảnh vào thư mục `images/` của dự án.
  4. Đặt ảnh vào khung hình chữ nhật bo góc mềm mại, hiển thị rõ ràng cho học sinh.

### 3. NGUỒN 3: Tự động tìm kiếm ảnh thực tế / ảnh hiển vi / ảnh khoa học chất lượng cao từ Web
- **Khi nào áp dụng**:
  - Bài học về sự vật, hiện tượng, sinh vật có thật trong tự nhiên (ví dụ: tế bào vảy hành dưới kính hiển vi, tế bào máu, tế bào trứng cá hồi, vi khuẩn E. coli, mô hình nguyên tử, động cơ nhiệt...).
  - Giáo viên không có sẵn ảnh hoặc muốn có thêm ảnh chụp thực tế sinh động, sắc nét để học sinh mở rộng hiểu biết.
- **Công cụ thực hiện**:
  - Dùng script tích hợp sẵn:
    ```bash
    python3 skills/ppt-master/scripts/image_search.py "<từ khóa tiếng Anh>" -o images/<tên_file>.jpg
    ```
  - Tìm kiếm trực tiếp từ kho ảnh khoa học mở khổng lồ: **Openverse** và **Wikimedia Commons**.
- **Đặc điểm & Tiêu chuẩn**:
  - **100% Miễn phí & An toàn bản quyền**: Nguồn giấy phép mở Creative Commons (CC), hoàn toàn hợp pháp cho giảng dạy.
  - **Không cần API key**: Chạy trực tiếp, không phụ thuộc tài khoản dịch vụ ngoài.
  - **Độ phân giải cực cao (2000px – 4000px)**: Ảnh gốc siêu nét, chiếu lên màn hình lớn không vỡ hạt.
  - **Dịch thuật ngữ khoa học chính xác**: Trợ lý tự động dịch từ khóa tiếng Việt sang thuật ngữ tiếng Anh chuyên ngành (ví dụ: *"tế bào vảy hành kính hiển vi"* $\to$ `"onion epidermal cells light microscope"`) để lấy đúng ảnh chụp hiển vi thật chuẩn xác của các viện nghiên cứu.

---

## V. HỆ THỐNG 5 PHONG CÁCH CHỦ ĐỀ (THEME STYLES) & 6 KIỂU BỐ CỤC (LAYOUT PATTERNS) CHUẨN STEM_MHHTH_v6

Để bài giảng luôn mới mẻ, cuốn hút và phù hợp với từng môn học/chủ đề, trợ lý hỗ trợ **5 Phong cách bảng màu (Theme Styles)** và **6 Kiểu bố cục (Layout Patterns)** kế thừa tinh hoa thiết kế từ bộ slide mẫu `STEM_MHHTH_v6.pptx`. Giáo viên có thể chỉ định phong cách yêu thích hoặc trợ lý tự động chọn phong cách phù hợp nhất với môn học:

### 🎨 1. BẢNG 5 PHONG CÁCH CHỦ ĐỀ MÀU SẮC (5 THEME STYLES)

| Mã Phong Cách | Tên Phong Cách | Nền Slide | Màu Header Đặc & Footer | Đường Chỉ Điểm Nhấn (6px) | 4 Màu Thẻ Phân Nhóm (Đậm / Nền Nhạt) | Phù Hợp Nhất Cho |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| **Style 1** | **STEM Modern Navy & Gold** *(Chuẩn STEM_v6)* | `#F0F5FB` | `#1B3A6B` *(Xanh Navy)* | `#E8941A` *(Vàng cam)* | 1. Đỏ `#C0392B` / `#FDEDEC`<br>2. Cam `#E8941A` / `#FFF3DB`<br>3. Ngọc `#16A085` / `#E8F8F5`<br>4. Lam `#1B3A6B` / `#E8EFF8` | Toán học, Vật lí, Hoạt động STEM, Báo cáo sáng kiến |
| **Style 2** | **Bio-Nature Emerald** *(Xanh Sinh Học)* | `#F2F9F6` | `#0F5132` *(Lục bảo đậm)* | `#F59E0B` *(Vàng nắng)* | 1. Lá `#198754` / `#E8F5E9`<br>2. Cam `#D97706` / `#FEF3C7`<br>3. Biển `#0284C7` / `#E0F2FE`<br>4. Tím `#7C3AED` / `#F3E8FF` | Sinh học, KHTN (Tế bào, Đa dạng sinh học, Sinh thái) |
| **Style 3** | **Chem-Lab Royal Purple** *(Tím Hoá Học)* | `#F5F3FF` | `#3B0764` *(Tím hoàng gia)* | `#06B6D4` *(Xanh Cyan)* | 1. Tím `#6D28D9` / `#EDE9FE`<br>2. Cyan `#0891B2` / `#CFFAFE`<br>3. Hồng `#BE185D` / `#FCE7F3`<br>4. Cam `#EA580C` / `#FFEDD5` | Hóa học, KHTN (Chất, Nguyên tử, Bảng tuần hoàn) |
| **Style 4** | **Classic Academic Light** *(Học Thuật Sáng)* | `#F8FAFC` | Nền sáng + Badge `#EBF3FA` | `#3B82F6` *(Line mảnh)* | 1. Xanh `#1F4E79` / `#EFF6FF`<br>2. Vàng `#F59E0B` / `#FFFBEB`<br>3. Lục `#10B981` / `#ECFDF5`<br>4. Tím `#6366F1` / `#EEF2FF` | Bài giảng lý thuyết truyền thống, Ôn tập nhẹ nhàng |
| **Style 5** | **Warm Terracotta** *(Năng Động Ấm Áp)* | `#FFFDF9` | `#7C2D12` *(Đỏ nâu ấm)* | `#FBBF24` *(Vàng tươi)* | 1. Cam `#EA580C` / `#FFEDD5`<br>2. Rêu `#15803D` / `#DCFCE7`<br>3. Lam `#1D4ED8` / `#DBEAFE`<br>4. Đỏ `#B91C1C` / `#FEE2E2` | Hoạt động Khởi động, Trò chơi, Lịch sử, Địa lí |

> 💡 **Quy tắc chọn Style**: Nếu giáo viên không chỉ định, trợ lý tự động chọn **Style 1 (STEM Navy & Gold)** cho Toán/Lí/STEM, **Style 2 (Bio-Nature Emerald)** cho Sinh học/Tế bào, **Style 3 (Chem-Lab)** cho Hóa học, hoặc luân chuyển khi giáo viên yêu cầu *"Đổi sang phong cách..."*.

---

### 📐 2. SÁU KIỂU BỐ CỤC HIỆN ĐẠI (6 LAYOUT PATTERNS TỪ STEM_MHHTH_v6)

Tuyệt đối **không dùng 1 bố cục lặp đi lặp lại cho cả bài**. Trong một bài giảng (8–12 slide), trợ lý phải phối hợp linh hoạt 6 kiểu bố cục sau và luôn dùng ký hiệu `▸` cho các dòng liệt kê:

#### 🔹 Layout 1: `Split Visual-Pedagogy` (Trái Kênh Hình 45% – Phải Hỏi & Ghi Nhớ 55%)
- **Ứng dụng**: Slide hình thành kiến thức có ảnh SGK, ảnh hiển vi thực tế hoặc sơ đồ thí nghiệm.
- **Cấu trúc**: Cột trái (`x=40..590`) đặt khung ảnh lớn bo góc kèm chú thích; Cột phải (`x=620..1240`) chia 2 hộp: Hộp trên là `❓ CÂU HỎI THẢO LUẬN` (nền vàng nhạt `#FFF3DB`, thanh tiêu đề cam `#E8941A`), hộp dưới là `💡 EM CẦN GHI NHỚ` (nền xanh nhạt `#E8EFF8`, thanh tiêu đề `#1B3A6B`).

#### 🔹 Layout 2: `2x2 Color-Coded Grid` (Lưới 4 Ô Đa Sắc — Chuẩn Slide 10, 18, 19 STEM_v6)
- **Ứng dụng**: Khi bài học có **4 phần, 4 thành phần, 4 vai trò, 4 tính chất** hoặc **4 câu hỏi luyện tập**.
- **Cấu trúc SVG mẫu**:
```xml
<!-- Ô 1 (Trái Trên - Đỏ San Hô) -->
<rect x="40" y="125" width="585" height="255" rx="10" fill="#FDEDEC" stroke="#F5B7B1" stroke-width="1"/>
<rect x="40" y="125" width="585" height="52" rx="10" fill="#C0392B"/>
<text x="60" y="159" font-size="26.67" font-weight="bold" fill="#FFFFFF" font-family="Times New Roman, serif">1. [TIÊU ĐỀ Ô 1]</text>
<text x="60" y="205" font-size="24.0" fill="#1E293B" font-family="Times New Roman, serif">▸ [Nội dung ý 1...]</text>

<!-- Ô 2 (Phải Trên - Cam Vàng) -->
<rect x="655" y="125" width="585" height="255" rx="10" fill="#FFF3DB" stroke="#FAD7A0" stroke-width="1"/>
<rect x="655" y="125" width="585" height="52" rx="10" fill="#E8941A"/>
<text x="675" y="159" font-size="26.67" font-weight="bold" fill="#FFFFFF" font-family="Times New Roman, serif">2. [TIÊU ĐỀ Ô 2]</text>

<!-- Ô 3 (Trái Dưới - Xanh Ngọc) -->
<rect x="40" y="400" width="585" height="255" rx="10" fill="#E8F8F5" stroke="#A3E4D7" stroke-width="1"/>
<rect x="40" y="400" width="585" height="52" rx="10" fill="#16A085"/>
<text x="60" y="434" font-size="26.67" font-weight="bold" fill="#FFFFFF" font-family="Times New Roman, serif">3. [TIÊU ĐỀ Ô 3]</text>

<!-- Ô 4 (Phải Dưới - Xanh Navy) -->
<rect x="655" y="400" width="585" height="255" rx="10" fill="#E8EFF8" stroke="#AED6F1" stroke-width="1"/>
<rect x="655" y="400" width="585" height="52" rx="10" fill="#1B3A6B"/>
<text x="675" y="434" font-size="26.67" font-weight="bold" fill="#FFFFFF" font-family="Times New Roman, serif">4. [TIÊU ĐỀ Ô 4]</text>
```

#### 🔹 Layout 3: `3-Row Numbered Cards` (3 Dải Thẻ Ngang Đánh Số Lớn — Chuẩn Slide 8 STEM_v6)
- **Ứng dụng**: Khi trình bày **3 thành phần chính** (ví dụ: Màng tế bào, Chất tế bào, Nhân tế bào), **3 định luật**, hoặc **3 bước trọng tâm**.
- **Cấu trúc SVG mẫu**:
```xml
<!-- Dải thẻ 1 -->
<rect x="40" y="130" width="1200" height="160" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
<rect x="40" y="130" width="85" height="160" rx="10" fill="#C0392B"/>
<text x="82" y="225" font-size="42.0" font-weight="bold" fill="#FFFFFF" text-anchor="middle" font-family="Times New Roman, serif">1</text>
<text x="150" y="172" font-size="26.67" font-weight="bold" fill="#C0392B" font-family="Times New Roman, serif">[Tên thành phần / Bước 1]</text>
<text x="150" y="212" font-size="24.0" fill="#1E293B" font-family="Times New Roman, serif">▸ [Mô tả chi tiết ngắn gọn, súc tích dòng 1]</text>
<!-- Dải thẻ 2 (y=310, màu #16A085) và Dải thẻ 3 (y=490, màu #1B3A6B) tương tự -->
```

#### 🔹 Layout 4: `Horizontal Process Flow` (Sơ Đồ Quy Trình Mũi Tên Ngang `▶` — Chuẩn Slide 9 STEM_v6)
- **Ứng dụng**: Dạy về **Quy trình thí nghiệm, Chu trình sinh học, Các bước giải bài toán thực tế**.
- **Cấu trúc**:
  - Phần trên (`y=125..245`): Hộp định nghĩa/Khái niệm nền `#E8EFF8`.
  - Phần giữa (`y=290..430`): Chuỗi 4–6 hộp bước quy trình (`fill="#C0392B"`, `#E8941A`, `#16A085`, `#2980B9`, `#1B3A6B`) xếp ngang, ngăn cách bởi ký hiệu mũi tên `▶` cỡ lớn.
  - Phần dưới (`y=465..655`): Khung `💡 EM CẦN GHI NHỚ` hoặc các tiêu chí kiểm chứng.

#### 🔹 Layout 5: `Concept Label Stripes` (Bảng Dải Băng Nhãn Màu — Chuẩn Slide 12 STEM_v6)
- **Ứng dụng**: Bảng tổng hợp thuật ngữ, chức năng các bộ phận/bào quan, hoặc phân công nhiệm vụ nhóm.
- **Cấu trúc**: 4–6 hàng ngang (`height="72"` mỗi hàng). Cột trái (`width="320"`) là hộp màu đặc (`#C0392B`, `#E8941A`, `#16A085`, `#2980B9`...) in chữ trắng đậm tên bộ phận; Cột phải (`width="880"`) là hộp nền trắng ghi chức năng tương ứng.

#### 🔹 Layout 6: `Comparison Table & Big Stat Cards` (Bảng Đối Chiếu Màu & Thẻ Số Liệu Lớn — Chuẩn Slide 4, 26 STEM_v6)
- **Ứng dụng**: So sánh 2 đối tượng (Tế bào nhân sơ vs Nhân thực; Thực vật vs Động vật; Trước vs Sau) hoặc nhấn mạnh các con số khoa học ấn tượng.
- **Cấu trúc**:
  - Bảng so sánh 3 cột: Cột 1 (Tiêu chí - Header `#1B3A6B`), Cột 2 (Đối tượng A - Header `#1B3A6B`, nền `#E8EFF8`), Cột 3 (Đối tượng B nổi bật - Header `#1E8A44`, nền xanh lá dịu `#D4EDDA`).
  - Hoặc đặt 3 **Thẻ Số Liệu Lớn (Big Stat Cards)** bên phải: Số liệu in cỡ `44pt` (`font-size="58.67"`) màu đậm nổi bật phía trên, lời giải thích 2 dòng phía dưới.

---

## VI. CÁC BƯỚC KỸ THUẬT CHUNG (KHI ĐÃ BẮT ĐẦU TẠO SLIDE)

### Bước kỹ thuật 1: Khởi tạo dự án
```bash
python3 skills/ppt-master/scripts/project_manager.py init <tên_dự_án>
python3 skills/ppt-master/scripts/project_manager.py import-sources <project_path> <file_nguồn>
```

### Bước kỹ thuật 2: Chuẩn bị kênh hình
- Ảnh thực tế đời sống / hiển vi khoa học:
  ```bash
  python3 skills/ppt-master/scripts/image_search.py "<từ khóa tiếng Anh>" -o images/<tên_file>.jpg
  ```
- Sơ đồ thí nghiệm / cấu tạo khoa học:
  Vẽ trực tiếp bằng hình học SVG vector (ống nghiệm, ngọn lửa nến, biểu đồ quạt donut).

### Bước kỹ thuật 3: Quy chuẩn Header & Footer SVG (Hỗ trợ cả 2 Kiểu Header)

#### Kiểu Header A — `Solid Top Banner` (Chuẩn STEM_MHHTH_v6 cho Style 1, 2, 3, 5):
Thanh Header màu đậm tràn viền (`height="100"`) kèm đường chỉ vàng cam `#E8941A` (`height="6"`) cực kỳ sang trọng và nổi bật:
```python
header_banner_svg = f"""
    <!-- Solid Top Banner Header (Chuẩn STEM_v6) -->
    <g id="page_header" data-pptx-role="header" data-pptx-bounds="0 0 1280 106">
        <rect x="0" y="0" width="1280" height="100" fill="{theme_primary}"/>
        <rect x="0" y="100" width="1280" height="6" fill="{theme_accent}"/>
        <rect x="40" y="14" width="260" height="26" rx="5" fill="{theme_accent}"/>
        <text x="52" y="33" font-size="18.67" font-weight="bold" fill="#FFFFFF" font-family="Times New Roman, serif">{tag}</text>
        <text x="40" y="80" font-size="29.33" font-weight="bold" fill="#FFFFFF" font-family="Times New Roman, serif">{title}</text>
        <text x="1240" y="80" font-size="18.67" font-weight="bold" fill="#E2E8F0" text-anchor="end" font-family="Times New Roman, serif">{page_num:02d} / {total_pages:02d}</text>
    </g>
"""
```

#### Kiểu Header B — `Clean Academic` (Nền sáng thanh lịch cho Style 4):
```python
header_clean_svg = f"""
    <!-- Clean Academic Header -->
    <g id="page_header" data-pptx-role="header" data-pptx-bounds="60 20 1160 78">
        <rect x="60" y="24" width="280" height="28" rx="6" fill="#EBF3FA"/>
        <text x="70" y="44" font-size="18.67" font-weight="bold" fill="#1F4E79" font-family="Times New Roman, serif">{tag}</text>
        <text x="60" y="80" font-size="29.33" font-weight="bold" fill="#1F4E79" font-family="Times New Roman, serif">{title}</text>
        <line x1="60" y1="96" x2="1220" y2="96" stroke="#E2E8F0" stroke-width="1.5"/>
    </g>
"""
```

#### Khung Footer chuẩn (Đồng bộ với Style):
```python
footer_svg = f"""
    <!-- Footer -->
    <g id="page_footer" data-pptx-role="footer" data-pptx-bounds="0 688 1280 32">
        <rect x="0" y="688" width="1280" height="32" fill="{theme_primary}"/>
        <text x="40" y="710" font-size="18.67" fill="#FFFFFF" font-family="Times New Roman, serif">{ten_truong} • GV: {ten_gv} • {ten_bai}</text>
        <text x="1240" y="710" font-size="18.67" font-weight="bold" fill="{theme_accent}" text-anchor="end" font-family="Times New Roman, serif">Trang {page_num:02d}/{total_pages:02d}</text>
    </g>
"""
```

### Bước kỹ thuật 4: Thiết lập Hiệu ứng Sư phạm Bấm chuột, Nút Đáp án & Morph (`animations.json`)

Để bài giảng có hiệu ứng chuẩn nhịp dạy học trên lớp, khi viết mã SVG ở mỗi slide nội dung, **bắt buộc bọc từng khối nội dung vào các thẻ `<g id="...">` riêng biệt ở cấp gốc (direct-root groups)** có `data-pptx-bounds` không chồng lấn:
- `id="kenh_hinh"`: Khung hình ảnh SGK / sơ đồ (Hiện sẵn khi mở trang).
- `id="cau_hoi_thao_luan"`: Hộp câu hỏi thảo luận (Bấm chuột lần 1 mới hiện).
- `id="em_can_ghi_nho"`: Khung chốt kiến thức ghi vở (Bấm chuột lần 2 mới hiện).
- Ở slide Trắc nghiệm / Luyện tập: Tạo nhóm nút bấm `id="nut_xem_dap_an"` và nhóm hộp đáp án `id="hop_dap_an"` đặt cạnh nhau (không đè lên nhau).

#### 1. Cấu trúc `animations.json` chuẩn (3 nhịp bấm chuột + Nút đáp án + Morph):
Tạo file `<project_path>/animations.json` trước khi chạy `svg_to_pptx.py`:
```json
{
  "version": 1,
  "defaults": {
    "transition": { "effect": "fade", "duration": 0.4 }
  },
  "slides": {
    "02_khoi_dong": {
      "transition": { "effect": "push", "duration": 0.5 },
      "groups": {
        "cau_hoi_thao_luan": {
          "effects": [{ "effect": "entrance_fade", "trigger": "on-click", "order": 1, "duration": 0.35 }]
        },
        "em_can_ghi_nho": {
          "effects": [{ "effect": "entrance_wipe", "trigger": "on-click", "order": 2, "duration": 0.4 }]
        }
      }
    },
    "04_chi_tiet_te_bao": {
      "transition": { "effect": "morph", "effect_options": { "morph_by": "object" }, "duration": 0.8 },
      "morph": {
        "from": "03_tong_quan_te_bao",
        "pairs": {
          "khoi-nhan-te-bao": { "from": "group_nhan_nho", "to": "group_nhan_phong_to" }
        }
      }
    },
    "07_luyen_tap": {
      "groups": {
        "hop_dap_an": {
          "effects": [{ "effect": "entrance_fade", "trigger_shape": "nut_xem_dap_an", "order": 1, "duration": 0.3 }]
        }
      }
    }
  }
}
```
- Kiểm tra hợp lệ cấu hình hiệu ứng trước khi xuất:
  ```bash
  python3 skills/ppt-master/scripts/animation_config.py validate <project_path>
  ```

---

### Bước kỹ thuật 5: Quy chuẩn Chuyên biệt khi soạn Môn Tiếng Anh (English Teaching Mode)

Khi giáo viên yêu cầu soạn slide môn **Tiếng Anh** (*Global Success, i-Learn Smart World, Friends Plus, Explore English...*), trợ lý tự động kích hoạt **Chế độ Tiếng Anh**:
1. **Tiến trình chuẩn tiết dạy Tiếng Anh (PPP & SGK mới)**:
   - `Slide 1 (Cover)` $\to$ `Slide 2 (Warm-up: Kim's Game / Guessing Picture / Pelmanism)` $\to$ `Slide 3 (I. Vocabulary: Bảng từ vựng + IPA + Ảnh Flashcard)` $\to$ `Slide 4 (II. Listen & Read / Presentation)` $\to$ `Slide 5 (III. Grammar Focus: (+), (-), (?) & Usage)` $\to$ `Slide 6–7 (IV. Practice: Task 1, Task 2, Task 3 theo SGK kèm nút bấm hiện đáp án)` $\to$ `Slide 8 (V. Production: Work in pairs / Let's talk & Wrap-up + Homework)`.
2. **Quy chuẩn trình bày Từ vựng (Vocabulary) & Phiên âm Quốc tế IPA**:
   - Bắt buộc ghi đầy đủ: **Từ vựng (Word) + Từ loại `(n/v/adj/adv)` + Phiên âm Quốc tế IPA `/.../` (có dấu trọng âm `'`) + Nghĩa tiếng Việt**.
   - Font `Times New Roman` hiển thị hoàn hảo 100% ký tự IPA (`/ˈnætʃ.ər.əl/`, `/θɪŋk/`, `/ʃʊd/`).
3. **Nhãn tiêu đề Khung chuẩn Tiếng Anh trên Slide**:
   - `🔤 NEW VOCABULARY` *(Thay cho Khung kiến thức ở phần từ vựng)*
   - `📐 GRAMMAR FOCUS` *(Khung công thức ngữ pháp)*
   - `💬 LET'S TALK / WORK IN PAIRS` *(Thay cho `CÂU HỎI THẢO LUẬN`)*
   - `🎯 PRACTICE — TASK 1, 2, 3` *(Các bài tập thực hành có nút bấm hiện Key/Answer)*
   - `💡 REMEMBER! / KEY TAKEAWAYS` *(Thay cho `EM CẦN GHI NHỚ`)*

---

### Bước kỹ thuật 5.5: Quy chuẩn Hiển thị Công thức Khoa học & Toán học (Môn Toán – Lí – Hóa – KHTN)

Khi giáo viên soạn slide cho các môn có công thức (**Toán, Vật Lí, Hóa Học, KHTN, Sinh học**), trợ lý áp dụng **3 cấp độ** hiển thị theo độ phức tạp của công thức:

#### Cấp độ 1 — Công thức đơn giản (Inline Unicode): ✅ Mặc định, không cần cài thêm

Dùng trực tiếp ký tự Unicode toán học trong thẻ `<text>` SVG — hiển thị hoàn hảo trong PPTX:

| Ký hiệu cần | Viết trong SVG | Hiển thị trong PPTX |
| :--- | :--- | :--- |
| Chỉ số dưới hóa học | `H₂SO₄`, `CO₂`, `NaHCO₃` | H₂SO₄, CO₂, NaHCO₃ |
| Số mũ vật lý | `v₀`, `s = v₀t + ½at²`, `E = mc²` | Hiển thị đúng |
| Ký hiệu phổ biến | `→`, `⇌`, `±`, `≤`, `≥`, `≈`, `∞` | Hiển thị đúng |
| Ký hiệu Hi Lạp | `Δ`, `α`, `β`, `λ`, `ω`, `μ`, `π`, `θ`, `φ` | Hiển thị đúng |
| Đơn vị vật lý | `m/s`, `m/s²`, `kg⋅m/s`, `°C`, `Ω`, `μF` | Hiển thị đúng |
| Pt đơn giản Toán | `F = ma`, `P = UI`, `Δs = ½at²`, `s = (a+b)h/2` | Hiển thị đúng |

**Cách viết SVG mẫu** (khung "EM CẦN GHI NHỚ" môn Vật Lí):
```xml
<g id="em_can_ghi_nho" data-pptx-bounds="40 500 1200 180">
  <rect x="40" y="500" width="1200" height="180" rx="10" fill="#FFF9E6" stroke="#E8941A" stroke-width="3"/>
  <text x="80" y="540" font-size="26.67" font-weight="bold" fill="#E8941A" font-family="Times New Roman, serif">💡 EM CẦN GHI NHỚ</text>
  <text x="80" y="580" font-size="24" fill="#1A1A2E" font-family="Times New Roman, serif">▸ Định luật II Newton: F = ma</text>
  <text x="80" y="615" font-size="24" fill="#1A1A2E" font-family="Times New Roman, serif">▸ Gia tốc: a = Δv/Δt (m/s²)</text>
  <text x="80" y="650" font-size="24" fill="#1A1A2E" font-family="Times New Roman, serif">▸ Quãng đường: s = v₀t + ½at² (m)</text>
</g>
```

---

#### Cấp độ 2 — Công thức trung bình (Vẽ SVG thủ công): ✅ Đủ đẹp, không cần thư viện ngoài

Dùng các thẻ `<text>`, `<line>`, `<rect>`, `<tspan>` SVG để "vẽ" công thức trông giống LaTeX.  
Áp dụng cho: phân số đơn giản, căn bậc 2 ngắn, chỉ số phức hợp.

**Mẫu vẽ phân số `a/b` bằng SVG thuần túy:**
```xml
<!-- Phân số: v̄ = Δs / Δt -->
<g transform="translate(200, 400)">
  <!-- Tử số -->
  <text x="0" y="0" font-size="24" fill="#1A1A2E" font-family="Times New Roman, serif" text-anchor="middle">Δs</text>
  <!-- Gạch phân số -->
  <line x1="-30" y1="8" x2="30" y2="8" stroke="#1A1A2E" stroke-width="2"/>
  <!-- Mẫu số -->
  <text x="0" y="32" font-size="24" fill="#1A1A2E" font-family="Times New Roman, serif" text-anchor="middle">Δt</text>
  <!-- Ký hiệu = và vế trái -->
  <text x="-80" y="16" font-size="24" fill="#1A1A2E" font-family="Times New Roman, serif">v̄ =</text>
</g>
```

**Mẫu vẽ căn thức `√(b²-4ac)` bằng SVG:**
```xml
<g transform="translate(300, 500)">
  <!-- Dấu căn -->
  <text x="0" y="0" font-size="28" fill="#1A1A2E" font-family="Times New Roman, serif">√</text>
  <!-- Nội dung trong căn (có gạch trên) -->
  <text x="28" y="0" font-size="24" fill="#1A1A2E" font-family="Times New Roman, serif">b²−4ac</text>
  <line x1="28" y1="-22" x2="130" y2="-22" stroke="#1A1A2E" stroke-width="1.5"/>
</g>
```

---

#### Cấp độ 3 — Công thức phức tạp (Render LaTeX → PNG → Nhúng SVG): ⭐ Đẹp hoàn hảo như LaTeX

Khi gặp công thức rất phức tạp: **tích phân, ma trận, sigma lồng nhau, phương trình vi phân, hóa hữu cơ chuỗi dài** — dùng `matplotlib` (đã có sẵn trong venv) để render LaTeX thành ảnh PNG 300 DPI rồi nhúng vào SVG qua thẻ `<image>`.

**Script Python render công thức** (lưu tại `skills/ppt-master/scripts/render_formula.py` hoặc chạy thẳng):
```python
#!/usr/bin/env python3
# render_formula.py — Render công thức LaTeX → PNG → nhúng vào SVG
import sys
import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.mathtext as mathtext

def render_latex_to_base64_png(latex_str: str, fontsize: int = 22, dpi: int = 300) -> str:
    """Render chuỗi LaTeX thành PNG base64 để nhúng trực tiếp vào SVG <image>."""
    fig, ax = plt.subplots(figsize=(0.01, 0.01))
    ax.set_axis_off()
    t = ax.text(0.5, 0.5, f"${latex_str}$",
                fontsize=fontsize, ha='center', va='center',
                fontfamily='Times New Roman',
                transform=ax.transAxes)
    fig.canvas.draw()
    # Tính toán kích thước bbox thực
    renderer = fig.canvas.get_renderer()
    bbox = t.get_window_extent(renderer=renderer)
    w_in = (bbox.width + 20) / fig.dpi
    h_in = (bbox.height + 12) / fig.dpi
    fig.set_size_inches(w_in, h_in)
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=dpi, bbox_inches='tight',
                pad_inches=0.05, transparent=True)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

# === Ví dụ sử dụng ===
if __name__ == '__main__':
    # Công thức Tích phân
    b64 = render_latex_to_base64_png(r'\int_a^b f(x)\,dx = F(b) - F(a)')
    print(f'data:image/png;base64,{b64[:60]}...')  # In mẫu
```

**Cách nhúng PNG base64 vào SVG:**
```xml
<!-- Nhúng công thức tích phân vào slide — chiều rộng/cao tự điều chỉnh -->
<image x="100" y="420" width="520" height="80"
       href="data:image/png;base64,iVBORw0KGgoAAAANS..."
       preserveAspectRatio="xMidYMid meet"/>
```

**Quy trình thực tế khi gặp công thức phức tạp:**
```bash
# Bước 1: Render công thức thành ảnh PNG (chạy từ thư mục repo)
d:\2anh-studio-main\venv\Scripts\python.exe skills/ppt-master/scripts/render_formula.py \
    --latex "\int_a^b f(x)\,dx" \
    --output projects/<project>/images/formula_01.png \
    --fontsize 24 --dpi 300

# Bước 2: Tham chiếu file PNG trong SVG (dùng đường dẫn tương đối)
# <image href="../images/formula_01.png" x="100" y="420" width="500" height="80"/>

# Bước 3: Xuất PPTX bình thường — bộ exporter tự nhúng ảnh vào PPTX
d:\2anh-studio-main\venv\Scripts\python.exe skills/ppt-master/scripts/svg_to_pptx.py <project_path>
```

#### Bảng quyết định nhanh — Chọn Cấp độ nào?

| Loại công thức | Môn điển hình | Cấp độ dùng |
| :--- | :--- | :---: |
| `F = ma`, `v₀`, `H₂SO₄`, `CO₂`, `E = mc²` | Lý, Hóa, KHTN | **Cấp 1** (Unicode) |
| `v̄ = Δs/Δt`, `√(b²−4ac)`, `x = (-b ± √Δ)/2a` | Toán, Lý | **Cấp 2** (SVG thủ công) |
| `∫f(x)dx`, Ma trận, `∑ᵢ₌₁ⁿ`, `lim_{x→∞}` | Toán Đại học/THPT | **Cấp 3** (matplotlib) |
| Chuỗi hóa hữu cơ, cơ chế phản ứng | Hóa hữu cơ | **Cấp 3** (matplotlib) |

> **⚠️ LƯU Ý**: Công thức render thành ảnh PNG (Cấp 3) sẽ **không thể bấm vào chỉnh sửa** trực tiếp trong PowerPoint. Khi cần chỉnh công thức, phải render lại PNG. Hãy giữ file LaTeX nguồn bên cạnh.

---

### Bước kỹ thuật 6: Kiểm định SVG, Xuất Native DrawingML PPTX & Kiểm tra Hiệu ứng
1. **Kiểm tra chất lượng SVG**:
   ```bash
   python3 skills/ppt-master/scripts/svg_quality_checker.py <project_path> --canonical-authoring --stage final --json
   ```
2. **Xuất PowerPoint Native (tự động đọc `animations.json`)**:
   ```bash
   python3 skills/ppt-master/scripts/svg_to_pptx.py <project_path>
   ```
3. **Vá font Times New Roman** (chạy ngay sau khi xuất PPTX):
   ```bash
   python3 skills/ppt-master/scripts/patch_fonts.py <đường_dẫn_file.pptx>
   ```
4. **Kiểm tra hiệu ứng sư phạm & Bàn giao**:
   ```bash
   python3 tools/vi/kiem_hieu_ung.py <duong_dan_file.pptx> --muc vua
   ```
   *(Hoặc `--muc nhieu` nếu có hiệu ứng Morph; đảm bảo kết quả trả về `"ready": true`).*
5. **Tạo bản sao có tên thân thiện & Gửi link**:
   - Đặt tên: `[Mon][Khoi]_[TenBai]_ChuanSuPham.pptx`
   - Cung cấp link mở file cho giáo viên với cú pháp `file:///...`.

---

## VII. XỬ LÝ KHI GIÁO VIÊN PHẢN HỒI KẾ HOẠCH (Luồng A & B)

| Phản hồi của giáo viên | Hành động của trợ lý |
|:---|:---|
| "Đồng ý" / "OK" / "Làm đi" / "Được" | Bắt đầu Bước kỹ thuật 1 (init project) ngay |
| "Đổi sang phong cách [Style 1 / STEM / Xanh Sinh học...]" | Đổi toàn bộ bảng màu và kiểu Header sang Style tương ứng |
| "Đổi bố cục slide X thành lưới 4 ô / quy trình..." | Áp dụng đúng Layout Pattern giáo viên yêu cầu cho slide X |
| "Thêm hiệu ứng Morph cho slide X và Y" | Thiết kế 2 slide liên tiếp có cặp nhóm đối tượng đồng nhất và khai báo `"morph"` trong `animations.json` |
| "Bỏ slide X" / "Gộp slide X và Y" / "Thêm slide..." | Điều chỉnh cấu trúc bảng Storyboard và hiển thị lại toàn bộ bảng để giáo viên xác nhận |

**Nguyên tắc vàng khi nhận phản hồi**: Mỗi lần cập nhật bảng kế hoạch phải **hiển thị lại toàn bộ bảng đã cập nhật** để giáo viên dễ xem và duyệt lần cuối.

---

## VIII. BẢNG TRA CỨU CÁC CỤM TỪ CHUẨN SƯ PHẠM (ĐA MÔN & TIẾNG ANH)

| Mục | ❌ KHÔNG DÙNG (Lý luận nội bộ) | ✅ DÙNG CHUẨN SƯ PHẠM (KHTN / Toán / Văn...) | ✅ DÙNG CHUẨN MÔN TIẾNG ANH (English Mode) |
| :--- | :--- | :--- | :--- |
| **Kênh hình** | `Kênh hình 11.1 SGK`, `Hình ảnh kênh hình` | `HÌNH 11.1: [TÊN]`, `QUAN SÁT HÌNH 11.1 (SGK)` | `LOOK AT THE PICTURE`, `VISUAL FLASHCARD` |
| **Phát vấn** | `Câu hỏi phát vấn`, `Phát vấn học sinh` | `CÂU HỎI THẢO LUẬN`, `❓ THẢO LUẬN NHÓM` | `💬 LET'S TALK`, `❓ WORK IN PAIRS / GROUPS` |
| **Ghi vở** | `Kết luận học sinh ghi vào vở`, `Chốt bài ghi vở` | `💡 EM CẦN GHI NHỚ`, `💡 KIẾN THỨC TRỌNG TÂM` | `💡 REMEMBER!`, `🔤 NEW VOCABULARY`, `📐 GRAMMAR FOCUS` |
| **Thí nghiệm / Thực hành** | `Mô phỏng kênh hình thí nghiệm` | `THÍ NGHIỆM: [TÊN THÍ NGHIỆM]` | `🎯 PRACTICE — TASK 1, 2, 3` |
| **Đề mục** | Có dòng chữ nhỏ chú thích dưới đề mục | **Bỏ hoàn toàn**, chỉ để tiêu đề to rõ (22pt) | **Bỏ hoàn toàn**, chỉ để Unit / Lesson Title to rõ (22pt) |
| **Ký hiệu liệt kê** | Dấu gạch ngang `-` đơn điệu | Dùng ký hiệu tam giác `▸` sắc nét, hiện đại | Dùng ký hiệu `▸` sắc nét, hiện đại |
