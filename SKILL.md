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

### 6 Nguyên tắc vàng:
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

---

## II. LUỒNG TƯƠNG TÁC GỢI Ý (KHI GIÁO VIÊN BẮT ĐẦU VỚI "TÔI MUỐN LÀM PPTX")

Khi giáo viên gửi câu lệnh mở đầu chung chung như:
> *"Tôi muốn làm pptx"*, *"Tôi muốn tạo pptx"*, *"Tôi muốn làm slide"*, *"Làm slide cho tôi"*, *"Tạo bài giảng pptx"*... (chưa đính kèm tài liệu cụ thể)

Trợ lý **bắt buộc không được tự ý tạo bài ngay**, mà phải thực hiện đúng luồng hướng dẫn 3 bước sau:

### BƯỚC 1: Phản hồi Lời chào, 4 Lưu ý vàng và Đưa ra 3 Lựa chọn
Trợ lý gửi ngay phản hồi nguyên văn theo mẫu sau:

```markdown
Dạ kính chào thầy/cô! Để em hỗ trợ soạn bộ slide PowerPoint đẹp mắt, chuẩn kiến thức và đúng sư phạm nhất, thầy cô lưu ý giúp em một số điểm sau:

💡 4 Lưu ý để slide đạt chuẩn cao nhất:
1. Bộ sách: Ghi rõ bộ SGK (Kết nối tri thức, Cánh diều hay Chân trời sáng tạo).
2. Thông tin bài: Tên trường, tên GV, khối lớp, tiết học để tự động in lên trang bìa và chân trang.
3. Tài liệu: File Word, PDF hoặc ảnh chụp rõ nét để trích xuất đủ bảng biểu, thí nghiệm.
4. Chuẩn hiển thị: Slide dùng font Times New Roman, tiêu đề bài 22pt, đề mục 20pt, nội dung 18pt (rõ nét cho học sinh ngồi cuối lớp).

---
❓ Thầy cô hiện đang có sẵn tài liệu ở dạng nào dưới đây ạ?
- [Phím 1] Thầy cô có File Giáo án (Word hoặc PDF)
- [Phím 2] Thầy cô có File Sách giáo khoa (PDF hoặc ảnh chụp SGK)
- [Phím 3] Thầy cô đã có kịch bản/nội dung từng slide cụ thể rồi

👉 Thầy cô chỉ cần nhắn số 1, 2 hoặc 3 (hoặc gửi file đính kèm kèm số), em sẽ hướng dẫn chi tiết bước tiếp theo ngay ạ!
```

> ⚠️ **BẮT BUỘC DỪNG VÀ CHỜ**: Sau khi gửi tin nhắn trên, trợ lý phải dừng lại và chờ giáo viên chọn 1, 2 hoặc 3. Không chạy bất kỳ lệnh `project_manager.py init` hay tạo file nào lúc này.

---

### BƯỚC 2: Hướng dẫn chi tiết theo lựa chọn của giáo viên

#### 🔹 Trường hợp 1: Giáo viên chọn số `1` (File Giáo án)
Trợ lý phản hồi:
```markdown
Dạ, với File Giáo án, thầy cô làm theo mẫu sau nhé:

📎 Thầy cô đính kèm file giáo án và nhắn cú pháp mẫu:
> "Đây là giáo án bài [Tên bài], môn [KHTN 6], bộ sách [Cánh Diều], Trường [THCS ...], GV [Nguyễn Văn ...], Tiết [...]. Em phân tích và lên kế hoạch slide cho tôi xem trước nhé!"

⚙️ Quy trình tiếp theo của em:
1. Em đọc giáo án, tự động lọc bỏ các phần hành chính (Mục tiêu, Năng lực số...).
2. Lập Bảng kế hoạch chi tiết từng slide gửi thầy cô duyệt.
3. Thầy cô xem xong bấm OK thì em mới bắt đầu tạo slide PPTX hoàn chỉnh ạ.
```

#### 🔹 Trường hợp 2: Giáo viên chọn số `2` (File Sách Giáo Khoa)
Trợ lý phản hồi:
```markdown
Dạ, với File Sách Giáo Khoa, thầy cô làm theo mẫu sau nhé:

📎 Thầy cô gửi file PDF SGK (hoặc ảnh chụp các trang sách) và nhắn:
> "Soạn slide bài [Tên bài], SGK [Môn ... Lớp ...] trang [X đến Y], bộ sách [Kết nối tri thức]. Trường [...], GV [...], Tiết [...]. Nhớ lấy đủ hình ảnh thí nghiệm/biểu đồ trong sách nhé!"

⚙️ Quy trình tiếp theo của em:
1. Em bóc tách toàn bộ hình ảnh, biểu đồ, thí nghiệm trong SGK.
2. Tự thiết kế tiến trình 3 bước: Quan sát hình → Câu hỏi thảo luận → Em cần ghi nhớ.
3. Trình bày Bảng kế hoạch slide để thầy cô duyệt trước khi tạo file PPTX ạ.
```

#### 🔹 Trường hợp 3: Giáo viên chọn số `3` (Đã có kịch bản từng slide)
Trợ lý phản hồi:
```markdown
Dạ tuyệt vời! Với Kịch bản có sẵn, thầy cô toàn quyền làm chủ nội dung, em chỉ lo phần thiết kế đẹp và chèn ảnh:

📝 Thầy cô gửi nội dung theo mẫu (dán trực tiếp vào chat hoặc gửi file Word):
> - Trường: ..., GV: ..., Lớp: ..., Bài: ..., Tiết: ...
> - Slide 1: Trang bìa - [Tên bài]
> - Slide 2: Khởi động - [Nội dung thầy cô muốn]
> - Slide 3: Phần I - [Nội dung thầy cô muốn, cần ảnh gì ghi rõ]
> - Slide 4: ...

⚙️ Quy trình tiếp theo của em:
Em sẽ làm đúng 100% nội dung thầy cô gửi, tự động tìm ảnh nét / vẽ sơ đồ vector đẹp và xuất thẳng file PPTX luôn, không cần qua bước duyệt kế hoạch nữa ạ!
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

#### [A3] Lập & Trình bày Bảng Kế Hoạch Slide:

Trình bày **Bảng kế hoạch slide** theo đúng định dạng này:

```markdown
📋 KẾ HOẠCH SLIDE — [Tên bài] — [Môn] [Lớp]
Tổng dự kiến: XX slide | Thời lượng tiết: 45 phút

| Slide | Tiêu đề slide | Nội dung chính | Hình ảnh / Sơ đồ |
|:-----:|:--------------|:---------------|:-----------------|
| 01    | Trang bìa     | Tên bài, trường, lớp, tiết, GV | Không |
| 02    | Hoạt động khởi động | Tình huống: [tóm tắt] | Tìm 3 ảnh web: [từ khoá tiếng Anh] |
| 03    | I. [Tên phần] | Nội dung 1: ... Nội dung 2: ... | Ảnh SGK / Sơ đồ vẽ |
| ...   | ...           | ...            | ...              |
| XX    | Vận dụng & Dặn dò | Nhiệm vụ về nhà: ... | Không |

💡 Lưu ý khi thầy cô phản hồi:
- "Bỏ slide X" → Em sẽ xoá
- "Gộp slide X và Y" → Em sẽ gộp nội dung
- "Thêm slide về Z" → Em sẽ bổ sung
- "Sửa nội dung slide X" → Em sẽ điều chỉnh
- "Đồng ý / OK / Làm đi" → Em bắt đầu tạo PPTX ngay
```

> ⚠️ **BẮT BUỘC DỪNG & CHỜ**: Sau khi xuất bảng kế hoạch, **dừng lại ngay** và hỏi: *"Thầy cô xem kế hoạch trên có đồng ý chưa ạ? Thầy cô muốn điều chỉnh gì không trước khi em bắt đầu làm slide?"*  
> **Tuyệt đối không chạy lệnh tạo slide hay init project khi chưa có phản hồi đồng ý.**

---

### QUY TRÌNH B: Từ File SGK → Kế hoạch → Duyệt → PPTX

```
[B1] Đọc & phân tích file SGK (nhận diện hình ảnh, bảng, thí nghiệm)
           ↓
[B2] Tự lên kịch bản sư phạm chuẩn 3 bước (Quan sát → Hỏi → Ghi nhớ)
           ↓
[B3] Lập Bảng Kế Hoạch Slide → Trình bày cho giáo viên duyệt
           ↓
     ⏸️ DỪNG & CHỜ GIÁO VIÊN ĐỒNG Ý (hoặc chỉnh sửa)
           ↓
[B4] Khởi tạo dự án & Chuẩn bị kênh hình (bóc tách ảnh SGK / vẽ sơ đồ)
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
- Các **thí nghiệm, thực hành** — cần vẽ sơ đồ diễn biến.
- Các **kết luận, kiến thức trọng tâm** để đưa vào khung "Em cần ghi nhớ".

#### [B2] Tự lên kịch bản sư phạm từ SGK:
Tổ chức lại theo cấu trúc sư phạm 3 bước:
- Từ mỗi **hình ảnh / biểu đồ / thí nghiệm** trong SGK $\to$ thiết kế 1 slide gồm Kênh hình + Câu hỏi + Ghi nhớ.
- Từ **câu hỏi SGK** $\to$ chuyển thành câu hỏi thảo luận nhóm/cặp đôi.
- Từ **lý thuyết** $\to$ chọn lọc 2–3 ý cốt lõi để chốt vào khung `💡 EM CẦN GHI NHỚ`.

#### [B3] Lập & Trình bày Bảng Kế Hoạch Slide (SGK):
Trình bày bảng kế hoạch có cột hình ảnh SGK:

```markdown
📋 KẾ HOẠCH SLIDE — [Tên bài] — [Môn] [Lớp] (từ SGK)
Tổng dự kiến: XX slide | Nguồn: SGK [Bộ sách] trang XX–XX

| Slide | Tiêu đề slide | Nội dung chính | Hình ảnh SGK / Cần tìm thêm |
|:-----:|:--------------|:---------------|:-----------------------------|
| 01    | Trang bìa     | Tên bài, trường, lớp, GV | Không |
| 02    | Khởi động     | [Tình huống thực tế liên quan đến bài] | Tìm ảnh: [từ khoá tiếng Anh] |
| 03    | [Phần I]      | Quan sát Hình X.X SGK → Câu hỏi thảo luận → Chốt ghi nhớ | Hình X.X từ SGK |
| ...   | ...           | ...            | ...                          |

💡 Thầy cô kiểm tra xem thứ tự và nội dung kịch bản có phù hợp với phân phối tiết dạy của trường mình không nhé!
```

> ⚠️ **BẮT BUỘC DỪNG & CHỜ**: Phải dừng lại và chờ phản hồi đồng ý của giáo viên.

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

## IV. CÁC BƯỚC KỸ THUẬT CHUNG (KHI ĐÃ BẮT ĐẦU TẠO SLIDE)

### Bước kỹ thuật 1: Khởi tạo dự án
```bash
python3 skills/ppt-master/scripts/project_manager.py init <tên_dự_án>
python3 skills/ppt-master/scripts/project_manager.py import-sources <project_path> <file_nguồn>
```

### Bước kỹ thuật 2: Chuẩn bị kênh hình
- Ảnh thực tế đời sống:
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

## V. XỬ LÝ KHI GIÁO VIÊN PHẢN HỒI KẾ HOẠCH (Luồng A & B)

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

## VI. BẢNG TRA CỨU CÁC CỤM TỪ CHUẨN SƯ PHẠM

| Mục | ❌ KHÔNG DÙNG (Lý luận nội bộ) | ✅ DÙNG CHUẨN SƯ PHẠM (Học sinh & SGK) |
| :--- | :--- | :--- |
| **Kênh hình** | `Kênh hình 11.1 SGK`, `Hình ảnh kênh hình` | `HÌNH 11.1: [TÊN]`, `QUAN SÁT HÌNH 11.1 (SGK)` |
| **Phát vấn** | `Câu hỏi phát vấn`, `Phát vấn học sinh` | `CÂU HỎI THẢO LUẬN`, `❓ THẢO LUẬN NHÓM` |
| **Ghi vở** | `Kết luận học sinh ghi vào vở`, `Chốt bài ghi vở` | `💡 EM CẦN GHI NHỚ`, `💡 KIẾN THỨC TRỌNG TÂM` |
| **Thí nghiệm** | `Mô phỏng kênh hình thí nghiệm` | `THÍ NGHIỆM: [TÊN THÍ NGHIỆM]` |
| **Đề mục** | Có dòng chữ nhỏ chú thích dưới đề mục | **Bỏ hoàn toàn**, chỉ để tiêu đề to rõ và thanh gạch ngang |
| **Khởi động** | `Hoạt động phát vấn khởi động` | `HOẠT ĐỘNG KHỞI ĐỘNG`, `TÌNH HUỐNG THỰC TẾ` |
| **Củng cố** | `Kiểm tra trắc nghiệm phát vấn` | `HOẠT ĐỘNG LUYỆN TẬP`, `THỬ TÀI ĐÚNG – SAI` |
