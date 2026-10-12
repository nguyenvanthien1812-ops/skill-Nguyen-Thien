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

### 8 Nguyên tắc vàng:
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

---

## II. LUỒNG TƯƠNG TÁC GỢI Ý (KHI GIÁO VIÊN BẮT ĐẦU VỚI "TÔI MUỐN LÀM PPTX")

Khi giáo viên gửi câu lệnh mở đầu chung chung như:
> *"Tôi muốn làm pptx"*, *"Tôi muốn tạo pptx"*, *"Tôi muốn làm slide"*, *"Làm slide cho tôi"*, *"Tạo bài giảng pptx"*... (chưa đính kèm tài liệu cụ thể)

Trợ lý **bắt buộc không được tự ý tạo bài ngay**, mà phải thực hiện đúng luồng hướng dẫn 3 bước sau:

### BƯỚC 1: Phản hồi Lời chào, 4 Lưu ý vàng và Đưa ra Lựa chọn & Cú pháp mẫu
Trợ lý gửi ngay phản hồi nguyên văn theo mẫu sau:

```markdown
Dạ kính chào thầy/cô! Để em hỗ trợ soạn bộ slide PowerPoint đẹp mắt, chuẩn kiến thức, đúng sư phạm và hình ảnh sắc nét nhất, thầy cô lưu ý giúp em một số điểm sau:

💡 4 Lưu ý để slide đạt chuẩn cao nhất:
1. Bộ sách: Ghi rõ bộ SGK (Kết nối tri thức, Cánh diều hay Chân trời sáng tạo).
2. Thông tin bài: Tên trường, tên GV, khối lớp, tiết học để tự động in lên trang bìa và chân trang.
3. Kênh hình & Ảnh minh hoạ: Em hỗ trợ bóc tách ảnh từ SGK (PDF), lấy ảnh từ thư mục máy tính, hoặc tự tìm ảnh chụp thực tế/hiển vi khoa học siêu nét từ Web.
4. Chuẩn hiển thị: Slide dùng font Times New Roman, tiêu đề bài 22pt, đề mục 20pt, nội dung 18pt (rõ nét cho học sinh ngồi cuối lớp).

---
❓ Thầy cô hiện đang có sẵn tài liệu ở dạng nào dưới đây ạ?
- [Phím 1] Thầy cô có File Giáo án (Word hoặc PDF)
- [Phím 2] Thầy cô có File Sách giáo khoa (PDF hoặc ảnh chụp SGK)
- [Phím 3] Thầy cô đã có kịch bản/nội dung từng slide cụ thể rồi

💡 CÁC MẪU CÂU LỆNH GỢI Ý THẦY CÔ CÓ THỂ DÙNG NGAY:
📌 Cách 1 (Dùng ảnh SGK): Đính kèm file PDF SGK (hoặc Word) và nhắn:
> "Soạn slide bài 17 Cấu tạo tế bào, SGK KHTN 6 Kết nối tri thức từ trang 60 đến 63. Trường THCS ..., GV: ..., Tiết 1. Nhớ bóc tách đúng các hình 17.1, 17.2 trong sách vào slide cho tôi nhé!"

📌 Cách 2 (Dùng thư mục ảnh trên máy tính): Gom ảnh vào một thư mục và nhắn:
> "Soạn slide bài Cấu tạo tế bào KHTN 6 Cánh Diều. Trường ..., GV ... Ảnh minh hoạ lấy từ thư mục D:\anh_tebao\ đưa vào các slide tương ứng giúp tôi nhé!"

📌 Cách 3 (Nhờ AI tìm ảnh thực tế/hiển vi nét cao từ Web): Nhắn kèm yêu cầu tìm ảnh:
> "Soạn slide bài Cấu tạo tế bào KHTN 6. Ở phần thực hành quan sát, tìm giúp tôi ảnh chụp tế bào vảy hành thật và tế bào biểu bì dưới kính hiển vi độ nét cao nhé!"

👉 Thầy cô chỉ cần nhắn số 1, 2, 3 (hoặc gửi file đính kèm kèm câu lệnh mẫu), em sẽ lập ngay BẢN PHÁC THẢO CHI TIẾT TỪNG SLIDE (Kênh hình, Kênh chữ, Em cần ghi nhớ, Lời giảng) gửi thầy cô duyệt trước khi tạo file PPTX ạ!
```

> ⚠️ **BẮT BUỘC DỪNG VÀ CHỜ**: Sau khi gửi tin nhắn trên, trợ lý phải dừng lại và chờ giáo viên chọn 1, 2 hoặc 3 (hoặc phản hồi câu lệnh). Không chạy bất kỳ lệnh `project_manager.py init` hay tạo file nào lúc này.

---

### BƯỚC 2: Hướng dẫn chi tiết theo lựa chọn của giáo viên

#### 🔹 Trường hợp 1: Giáo viên chọn số `1` (File Giáo án)
Trợ lý phản hồi:
```markdown
Dạ, với File Giáo án, thầy cô làm theo mẫu gợi ý sau nhé:

📎 Thầy cô đính kèm file giáo án và nhắn cú pháp mẫu:
> "Đây là giáo án bài [Tên bài], môn [KHTN 6], bộ sách [Cánh Diều], Trường [THCS ...], GV [Nguyễn Văn ...], Tiết [...]. [Tùy chọn ảnh: Lấy ảnh trong thư mục D:\... / hoặc Tìm giúp tôi ảnh thực tế/hiển vi]. Em phân tích và lên bản phác thảo Storyboard chi tiết từng slide cho tôi xem trước nhé!"

⚙️ Quy trình tiếp theo của em:
1. Em đọc giáo án, tự động lọc bỏ các phần hành chính rườm rà (Mục tiêu, Năng lực số...).
2. Lập Bản phác thảo Storyboard chi tiết từng slide (mô tả rõ Kênh hình, Câu hỏi phát vấn, Khung ghi nhớ, Lời giảng GV) gửi thầy cô duyệt.
3. Thầy cô xem xong bấm OK (hoặc yêu cầu chỉnh sửa) thì em mới bắt đầu tạo slide PPTX hoàn chỉnh ạ.
```

#### 🔹 Trường hợp 2: Giáo viên chọn số `2` (File Sách Giáo Khoa)
Trợ lý phản hồi:
```markdown
Dạ, với File Sách Giáo Khoa, thầy cô chọn 1 trong các mẫu gợi ý sau nhé:

📎 Mẫu 2A (Bóc tách ảnh SGK): Gửi file PDF SGK (hoặc ảnh chụp các trang sách) và nhắn:
> "Soạn slide bài [Tên bài], SGK [Môn ... Lớp ...] trang [X đến Y], bộ sách [Kết nối tri thức]. Trường [...], GV [...], Tiết [...]. Nhớ bóc tách đúng các hình X.1, X.2 trong sách vào slide nhé!"

📎 Mẫu 2B (Dùng thêm ảnh thư mục máy tính):
> "... Lấy thêm ảnh thí nghiệm từ thư mục D:\tai_lieu\anh_bai_day\ đưa vào slide nhé!"

📎 Mẫu 2C (Nhờ AI tìm ảnh thực tế/hiển vi khoa học từ Web):
> "... Tìm giúp tôi ảnh thực tế/ảnh chụp kính hiển vi độ nét cao của [tên đối tượng] trên mạng đưa vào bài giảng nhé!"

⚙️ Quy trình tiếp theo của em:
1. Em bóc tách toàn bộ hình ảnh, biểu đồ, thí nghiệm trong SGK (hoặc thư mục/web).
2. Tự thiết kế tiến trình 3 bước sư phạm: Quan sát hình → Câu hỏi thảo luận → Em cần ghi nhớ.
3. Trình bày Bản phác thảo Storyboard chi tiết từng slide để thầy cô duyệt trước khi tạo file PPTX ạ.
```

#### 🔹 Trường hợp 3: Giáo viên chọn số `3` (Đã có kịch bản từng slide)
Trợ lý phản hồi:
```markdown
Dạ tuyệt vời! Với Kịch bản có sẵn, thầy cô toàn quyền làm chủ nội dung, em chỉ lo phần thiết kế đẹp và chèn ảnh:

📝 Thầy cô gửi nội dung theo mẫu (dán trực tiếp vào chat hoặc gửi file Word):
> - Trường: ..., GV: ..., Lớp: ..., Bài: ..., Tiết: ...
> - Slide 1: Trang bìa - [Tên bài]
> - Slide 2: Khởi động - [Nội dung thầy cô muốn, cần ảnh gì ghi rõ hoặc chỉ định thư mục ảnh]
> - Slide 3: Phần I - [Nội dung thầy cô muốn, ghi chú ảnh SGK / ảnh web]
> - Slide 4: ...

⚙️ Quy trình tiếp theo của em:
Em sẽ làm đúng 100% nội dung thầy cô gửi, tự động xử lý ảnh nét / vẽ sơ đồ vector đẹp và xuất thẳng file PPTX luôn, không cần qua bước duyệt kế hoạch nữa ạ!
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
Tổng dự kiến: XX slide | Thời lượng: 45 phút | Khổ: 16:9 (hoặc 4:3) | Font: Times New Roman

---
### 1. BẢNG TỔNG QUAN TIẾN TRÌNH:
| Slide | Tiêu đề slide | Hoạt động / Nội dung | Kênh hình (Ảnh SGK / Thực tế / Thư mục) |
|:-----:|:--------------|:---------------------|:----------------------------------------|
| 01    | Trang bìa     | Tên bài, trường, lớp, tiết, GV | Họa tiết vector khoa học trang nhã |
| 02    | Khởi động     | Tình huống thực tế dẫn dắt vào bài | 2–3 ảnh thực tế đời sống / ảnh web |
| 03    | I. [Tên phần] | Quan sát → Thảo luận → Chốt ghi nhớ | Hình X.X SGK / Sơ đồ / Ảnh thư mục |
| ...   | ...           | ...                  | ... |
| XX    | Vận dụng & Dặn dò | Nhiệm vụ thực tế về nhà | Không |

---
### 2. PHÁC THẢO CHI TIẾT TỪNG SLIDE (KÊNH HÌNH & KÊNH CHỮ):

#### 🔹 Slide 01: TRANG BÌA
- **Tiêu đề:** [TÊN BÀI HỌC IN HOA]
- **Thông tin:** Trường [Tên trường] • GV: [Tên thầy cô] • Lớp [Lớp] • Tiết [Tiết]
- **Kênh hình:** Họa tiết vector khoa học trang nhã.

#### 🔹 Slide 02: HOẠT ĐỘNG KHỞI ĐỘNG
- **Tiêu đề:** KHỞI ĐỘNG: [TÊN TÌNH HUỐNG/CÂU ĐỐ]
- **📸 Kênh hình:** [Mô tả chi tiết 2–3 ảnh: ảnh gì, nguồn từ đâu (Web Openverse/SGK/Thư mục GV)].
- **❓ Câu hỏi thảo luận:** "[Câu hỏi phát vấn gợi mở học sinh suy nghĩ]?"
- **💡 Em cần ghi nhớ (Dẫn dắt):** [Ý chốt mở ra bài học mới].
- **🎙️ Ghi chú lời giảng GV:** "[Lời thầy cô dẫn dắt học sinh vào bài học]".

#### 🔹 Slide 03: I. [TÊN MỤC BÀI HỌC]
- **Tiêu đề:** [I. TÊN NỘI DUNG TRỌNG TÂM]
- **📸 Kênh hình:** [Chỉ rõ: Hình X.X bóc tách từ SGK trang YY / Ảnh chụp từ thư mục GV / Sơ đồ vẽ].
- **❓ Câu hỏi thảo luận:**
  1. [Câu hỏi 1 cho học sinh quan sát hình]?
  2. [Câu hỏi 2 phát triển tư duy]?
- **💡 Em cần ghi nhớ (Chốt ghi vở):**
  - [Ý 1: Định nghĩa / đặc điểm cốt lõi].
  - [Ý 2: Vai trò / quy luật].
- **🎙️ Ghi chú lời giảng GV:** "[Lời giải thích, hướng dẫn học sinh phân tích hình ảnh]".

*(... Các slide tiếp theo trình bày chi tiết tương tự ...)*

---
💡 Thầy cô xem bản phác thảo chi tiết trên và phản hồi giúp em nhé:
- "Đồng ý / OK / Làm đi" → Em bắt đầu tạo bộ slide PPTX ngay.
- "Đổi ảnh slide X thành [mô tả ảnh]" → Em sẽ đổi nguồn ảnh theo ý thầy cô.
- "Sửa câu hỏi / nội dung slide Y" → Em sẽ cập nhật lại nội dung.
- "Thêm / Bớt / Gộp slide" → Em sẽ điều chỉnh cấu trúc và gửi lại bảng cập nhật.
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

## V. CÁC BƯỚC KỸ THUẬT CHUNG (KHI ĐÃ BẮT ĐẦU TẠO SLIDE)

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

### Bước kỹ thuật 3: Quy chuẩn Header & Bố cục SVG

#### Khung Header chuẩn (Không dòng chữ bé):
```python
header_svg = f"""
    <!-- Header -->
    <g id="page_header" data-pptx-role="header" data-pptx-bounds="60 20 1160 78">
        <rect x="60" y="24" width="280" height="28" rx="6" fill="#EBF3FA"/>
        <text x="70" y="44" font-size="18.67" font-weight="bold" fill="#1F4E79" font-family="Times New Roman, serif">{tag}</text>
        <text x="60" y="80" font-size="29.33" font-weight="bold" fill="#1F4E79" font-family="Times New Roman, serif">{title}</text>
        <line x1="60" y1="96" x2="1220" y2="96" stroke="#E2E8F0" stroke-width="1.5"/>
    </g>
"""
```

#### Khung Footer chuẩn:
```python
footer_svg = f"""
    <!-- Footer -->
    <g id="page_footer" data-pptx-role="footer" data-pptx-bounds="60 670 1160 40">
        <line x1="60" y1="672" x2="1220" y2="672" stroke="#E2E8F0" stroke-width="1.5"/>
        <text x="60" y="695" font-size="18.67" fill="#94A3B8" font-family="Times New Roman, serif">{ten_bai} • GV: {ten_gv} • Lớp {lop}</text>
        <text x="1220" y="695" font-size="18.67" font-weight="bold" fill="#1F4E79" text-anchor="end" font-family="Times New Roman, serif">{page_num:02d} / {total_pages:02d}</text>
    </g>
"""
```

#### Quy chuẩn thẻ thảo luận & Em cần ghi nhớ:
```xml
<!-- Khung Câu hỏi thảo luận -->
<rect x="645" y="112" width="575" height="265" rx="16" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
<rect x="645" y="112" width="575" height="42" rx="16" fill="#F59E0B"/>
<text x="690" y="141" font-size="26.67" font-weight="bold" fill="#FFFFFF" font-family="Times New Roman, serif">CÂU HỎI THẢO LUẬN</text>

<!-- Khung Em cần ghi nhớ (chốt kiến thức ghi vở) -->
<rect x="645" y="390" width="575" height="270" rx="16" fill="#EFF6FF" stroke="#3B82F6" stroke-width="2"/>
<rect x="645" y="390" width="575" height="42" rx="16" fill="#1F4E79"/>
<text x="690" y="419" font-size="26.67" font-weight="bold" fill="#FFFFFF" font-family="Times New Roman, serif">💡 EM CẦN GHI NHỚ</text>
```

### Bước kỹ thuật 4: Kiểm định & Xuất Native DrawingML PPTX
1. **Kiểm tra chất lượng**:
   ```bash
   python3 skills/ppt-master/scripts/svg_quality_checker.py <project_path> --canonical-authoring --stage final --json
   ```
2. **Xuất PowerPoint Native**:
   ```bash
   python3 skills/ppt-master/scripts/svg_to_pptx.py <project_path>
   ```
3. **Vá font Times New Roman** (chạy sau khi xuất PPTX):
   ```bash
   python3 skills/ppt-master/scripts/patch_fonts.py <đường_dẫn_file.pptx>
   ```

### Bước kỹ thuật 5: Kiểm tra hiệu ứng sư phạm & Bàn giao
- Chạy kiểm tra hiệu ứng:
   ```bash
   python3 tools/vi/kiem_hieu_ung.py <duong_dan_file.pptx> --muc vua
   ```
   *(Đảm bảo kết quả trả về `"ready": true` và các thẻ câu hỏi/kết luận xuất hiện theo click chuột.)*
- Tạo bản sao có tên thân thiện:
   `KHTN[Khối]_[TenBai]_ChuanSuPham.pptx`
- Cung cấp link mở file cho giáo viên với cú pháp `file:///...`.

---

## VI. XỬ LÝ KHI GIÁO VIÊN PHẢN HỒI KẾ HOẠCH (Luồng A & B)

| Phản hồi của giáo viên | Hành động của trợ lý |
|:---|:---|
| "Đồng ý" / "OK" / "Làm đi" / "Được" | Bắt đầu Bước kỹ thuật 1 (init project) ngay |
| "Bỏ slide X" | Ghi chú xoá slide X, cập nhật lại bảng kế hoạch, hỏi "Thầy cô xác nhận kế hoạch mới chưa ạ?" |
| "Gộp slide X và Y" | Ghi chú gộp nội dung, cập nhật bảng, hỏi xác nhận |
| "Thêm slide về [chủ đề]" | Thêm slide mới vào đúng vị trí, cập nhật bảng, hỏi xác nhận |
| "Sửa nội dung slide X thành..." | Cập nhật nội dung slide X theo ý giáo viên, xác nhận lại |
| "Ít slide hơn" / "Nhiều slide hơn" | Điều chỉnh số lượng, giải thích gộp/chia như thế nào, hỏi xác nhận |
| "Bài này không cần luyện tập" | Bỏ slide Luyện tập, cập nhật bảng, hỏi xác nhận |

**Nguyên tắc vàng khi nhận phản hồi**: Mỗi lần cập nhật bảng kế hoạch phải **hiển thị lại toàn bộ bảng đã cập nhật** để giáo viên dễ xem và duyệt lần cuối.

---

## VII. BẢNG TRA CỨU CÁC CỤM TỪ CHUẨN SƯ PHẠM

| Mục | ❌ KHÔNG DÙNG (Lý luận nội bộ) | ✅ DÙNG CHUẨN SƯ PHẠM (Học sinh & SGK) |
| :--- | :--- | :--- |
| **Kênh hình** | `Kênh hình 11.1 SGK`, `Hình ảnh kênh hình` | `HÌNH 11.1: [TÊN]`, `QUAN SÁT HÌNH 11.1 (SGK)` |
| **Phát vấn** | `Câu hỏi phát vấn`, `Phát vấn học sinh` | `CÂU HỎI THẢO LUẬN`, `❓ THẢO LUẬN NHÓM` |
| **Ghi vở** | `Kết luận học sinh ghi vào vở`, `Chốt bài ghi vở` | `💡 EM CẦN GHI NHỚ`, `💡 KIẾN THỨC TRỌNG TÂM` |
| **Thí nghiệm** | `Mô phỏng kênh hình thí nghiệm` | `THÍ NGHIỆM: [TÊN THÍ NGHIỆM]` |
| **Đề mục** | Có dòng chữ nhỏ chú thích dưới đề mục | **Bỏ hoàn toàn**, chỉ để tiêu đề to rõ và thanh gạch ngang |
| **Khởi động** | `Hoạt động phát vấn khởi động` | `HOẠT ĐỘNG KHỞI ĐỘNG`, `TÌNH HUỐNG THỰC TẾ` |
| **Củng cố** | `Kiểm tra trắc nghiệm phát vấn` | `HOẠT ĐỘNG LUYỆN TẬP`, `THỬ TÀI ĐÚNG – SAI` |
