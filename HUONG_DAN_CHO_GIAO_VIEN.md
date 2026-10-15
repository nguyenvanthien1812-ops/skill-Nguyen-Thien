# 📘 HƯỚNG DẪN CẦM TAY CHỈ VIỆC: TẠO SLIDE BÀI GIẢNG BẰNG TRỢ LÝ AI
### Dành cho thầy cô giáo Trường THCS Ứng Hòe — Không cần giỏi tin học

> [!NOTE]
> Tài liệu này hướng dẫn từng bước cực kỳ chi tiết, từ việc lấy file trên máy tính đến khi nhận được file PowerPoint hoàn chỉnh. Thầy cô làm theo đúng thứ tự là sẽ thành công.

---

## 🔰 BƯỚC 0 — TRƯỚC KHI BẮT ĐẦU: MỞ CỬA SỔ CHAT VỚI TRỢ LÝ AI

Mở trình duyệt (Chrome hoặc Edge) trên máy tính và đăng nhập vào phần mềm trợ lý AI của nhà trường. Thầy cô sẽ thấy một **ô nhập tin nhắn ở dưới cùng màn hình** — đó là nơi thầy cô gõ câu lệnh và gửi tài liệu.

---

## 🔑 BƯỚC 0.1 — KÍCH HOẠT BẢN QUYỀN (CHỈ CẦN LÀM ĐÚNG 1 LẦN ĐẦU TIÊN)

> **💡 Giáo viên có cần cài đặt phần mềm gì phức tạp không?**  
> **HOÀN TOÀN KHÔNG!**  
> - ❌ **Không cần cài MathType**: Công thức toán trên slide dùng chuẩn Native OMML của Microsoft, mở trực tiếp bằng PowerPoint là sửa được ngay.  
> - ❌ **Không cần cài MiKTeX hay LaTeX**: Hệ thống tự động biên dịch toàn bộ.  
> - ❌ **Không cần tài khoản hay nạp tiền API**: Dùng trực tiếp trên máy tính.  
> - ✅ **Máy tính chỉ cần có**: **Microsoft PowerPoint** (bản 2016 trở lên) và **Python** (nếu máy trắng tinh chưa có Python, thầy cô chỉ cần nhấp đúp file `cai_dat_tu_dong.bat` 1-click là xong hết).

### Quy trình 2 bước để nhận bản quyền từ Thầy Thiện:
1. **Lấy Mã máy gửi Thầy Thiện:**  
   - Mở thư mục phần mềm `tao-slide-bai-giang`.  
   - Nhấp đúp chuột vào file **`LAY_MA_MAY.bat`**.  
   - Màn hình đen hiện lên dòng chữ xanh: `Mã máy của bạn: [chuỗi ký tự]` và thông báo: *[ĐÃ TỰ ĐỘNG COPY VÀO BỘ NHỚ TẠM!]*.  
   - Thầy/cô chỉ cần mở Zalo gửi cho Thầy Thiện rồi nhấn **`Ctrl + V`** (Dán).
2. **Kích hoạt bản quyền:**  
   - Sau khi Thầy Thiện gửi lại cho thầy/cô một đoạn mã **License Key**.  
   - Thầy/cô nhấp đúp vào file **`KICH_HOAT_BAN_QUYEN.bat`** rồi dán mã Key vào (hoặc gửi thẳng đoạn mã Key đó vào khung chat AI này).  
   - Màn hình báo *🎉 KÍCH HOẠT THÀNH CÔNG!* $\to$ Từ nay thầy/cô sử dụng vĩnh viễn, không bao giờ phải làm lại bước này nữa!

---

## 📂 BƯỚC 1 — CHUẨN BỊ FILE TÀI LIỆU (Chọn 1 trong 4 cách)

Thầy cô chọn cách nào tiện nhất với mình:

---

### ✅ Cách 1 — Kéo thả file thẳng vào ô chat *(Dễ nhất)*

> **Áp dụng khi:** Thầy cô có file Giáo án Word (`.docx`), file PDF SGK, hoặc ảnh chụp bài dạy sẵn trong máy tính.

**Làm theo 3 bước sau:**

1. Mở thư mục chứa file giáo án trên máy tính *(Ví dụ: ổ D: → thư mục "Giáo án" → thư mục "Toán 6")*
2. Để **2 cửa sổ cạnh nhau**: bên trái là thư mục chứa file, bên phải là cửa sổ chat trợ lý AI
3. Dùng chuột **giữ vào file giáo án → KÉO SANG bên phải → THẢ vào ô nhập tin nhắn** → File tự động được tải lên ✔

---

### ✅ Cách 2 — Copy đường dẫn file *(Nhanh nhất cho file nặng)*

> **Áp dụng khi:** File PDF SGK hoặc Word nặng, kéo thả chậm, hoặc thầy cô biết rõ file nằm ở đâu trên máy.

1. Mở thư mục chứa file *(Windows Explorer)*
2. **Nhấp CHUỘT PHẢI** vào file → Chọn **"Copy as path"** *(Sao chép dưới dạng đường dẫn)*
   - ⚠️ Nếu không thấy tùy chọn này: **Giữ phím `Shift`** rồi mới nhấp chuột phải → sẽ thấy ngay
3. Quay sang cửa sổ chat → Nhấn `Ctrl + V` để dán vào ô tin nhắn
   - Ví dụ hiện ra: `"D:\Giao_an\Toan6_Bai13.docx"`
4. Nhấn **Enter** hoặc nút **Gửi** ✔

---

### ✅ Cách 3 — Chụp ảnh trang sách bằng điện thoại *(Tiện nhất ở nhà hoặc không có file máy tính)*

> **Áp dụng khi:** Thầy cô có sách giáo khoa hoặc tài liệu in sẵn, không có file trên máy.

1. Lấy điện thoại, **chụp ảnh trang SGK** cần dạy *(chụp rõ nét, đủ ánh sáng, không bị lóa)*
2. Chuyển ảnh lên máy tính bằng 1 trong 2 cách:
   - Cắm dây USB điện thoại vào máy tính → kéo ảnh sang máy
   - Gửi ảnh lên **Zalo** trên điện thoại → mở Zalo trên máy tính → tải ảnh xuống
3. Kéo thả ảnh vào ô chat *(giống Cách 1)* ✔

---

### ✅ Cách 4 — Gõ tóm tắt nội dung trực tiếp *(Nếu không có file nào)*

> **Áp dụng khi:** Thầy cô muốn tạo bài từ đầu hoàn toàn theo ý mình.

Chỉ cần gõ thẳng vào ô chat nội dung bài học, ví dụ:

> *"Tôi cần soạn bài ƯCLN và BCNN cho lớp 6. Nội dung gồm: Khái niệm ƯCLN, Quy tắc 3 bước tìm ƯCLN, Khái niệm BCNN, Quy tắc 3 bước tìm BCNN, Công thức liên hệ: ƯCLN × BCNN = a × b."*

---

## 💬 BƯỚC 2 — GỬI CÂU LỆNH TẠO SLIDE

Sau khi đã gửi file lên, thầy cô **gõ thêm 1 câu lệnh yêu cầu** bên dưới rồi nhấn Enter.

> [!TIP]
> Chỉ cần **copy một trong các mẫu câu bên dưới**, thay tên bài và lớp cho phù hợp rồi gửi đi. Không cần phải gõ gì thêm!

---

### 📋 BỘ MẪU CÂU LỆNH THEO TỪNG NHU CẦU

---

#### 🟦 Soạn bài giảng thông thường *(Môn KHTN / Sinh / Địa / Sử / Văn)*

```
Soạn cho tôi bài giảng slide PowerPoint từ file giáo án tôi gửi.
Trình bày theo tiến trình 3 bước: quan sát hình → câu hỏi thảo luận → khung em cần ghi nhớ.
Chữ to rõ, nhiều hình ảnh minh họa thực tế nhé.
```

---

#### 🟧 Soạn bài Toán / Vật lí / Hóa học *(Có công thức toán học)*

```
Soạn slide bài giảng từ tài liệu tôi gửi.
Các công thức toán học phải to, rõ, chuẩn SGK — dùng định dạng OMML
để giáo viên click đúp sửa được trực tiếp trong PowerPoint.
Chữ tiêu đề cỡ 24, nội dung cỡ 20, có lời giải chi tiết từng bước.
```

---

#### 🟩 Làm slide bài tập điền từ / trò chơi tương tác

```
Làm cho tôi 1 slide bài tập điền từ vào chỗ trống.
Slide chia 2 cột hoặc 2 khung rõ ràng.
Những chữ IN HOA là chỗ trống học sinh cần điền.
Khi giáo viên bấm vào đáp án bên dưới thì chữ sẽ tự động chạy lên đúng chỗ trống.
```

---

#### 🟥 Làm sơ đồ tư duy ôn tập / tổng kết chương

```
Tạo cho tôi 1 slide sơ đồ tư duy dạng tỏa tròn đẹp mắt, hấp dẫn học sinh
về chủ đề [ĐIỀN TÊN BÀI VÀO ĐÂY].
Có mẹo nhớ nhanh cho học sinh, hiệu ứng bung tỏa từ tâm khi trình chiếu.
```

---

#### 🟨 Soạn bài tập có lời giải chi tiết

```
Tạo slide hướng dẫn giải các bài tập trong ảnh/file tôi gửi.
Mỗi bài tập 1 slide, trình bày từng bước, có công thức to rõ.
Thêm slide đáp án riêng để giáo viên click hiện ra khi cần.
```

---

#### 🟪 Làm nhiều slide cùng lúc theo chủ đề

```
Soạn bộ slide đầy đủ cho bài [TÊN BÀI] lớp [SỐ LỚP], gồm:
- Slide khởi động (câu hỏi thực tế hoặc trò chơi nhỏ)
- Slide hình thành kiến thức (3 bước: hình → câu hỏi → ghi nhớ)
- Slide luyện tập (2–3 bài tập từ dễ đến khó)
- Slide tổng kết và dặn dò về nhà
```

---

## 👀 BƯỚC 3 — XEM VÀ DUYỆT KỊCH BẢN *(Chỉ mất 1 phút)*

Sau khi gửi câu lệnh, trợ lý AI sẽ hiển thị một **bảng tóm tắt kịch bản từng slide** để thầy cô duyệt trước khi làm thật. Ví dụ:

```
Slide 1  │ Trang bìa: Tên bài + tên giáo viên
Slide 2  │ Khởi động: Câu đố thực tế (Bài toán chia bánh)
Slide 3  │ Khái niệm ƯCLN + hình minh họa
Slide 4  │ Quy tắc 3 bước tìm ƯCLN (ví dụ step-by-step)
Slide 5  │ Khái niệm BCNN + hình minh họa
Slide 6  │ Quy tắc 3 bước tìm BCNN (ví dụ step-by-step)
Slide 7  │ Công thức vàng liên hệ + Mẹo nhớ nhanh
Slide 8  │ Bài tập luyện tập có đáp án
Slide 9  │ Tổng kết và dặn dò về nhà
```

**Thầy cô phản hồi theo 1 trong các cách sau:**

| Thầy cô muốn | Gõ vào chat |
|:---|:---|
| Đồng ý toàn bộ, làm đi | `Đồng ý, làm đi nhé` |
| Đổi màu sắc phong cách | `Đổi sang màu xanh lá cây sinh học nhé` |
| Thêm slide | `Thêm 1 slide bài tập nữa sau slide 8` |
| Bớt slide | `Bỏ slide 9 đi, không cần dặn dò` |
| Đổi nội dung 1 slide | `Slide 2 làm câu hỏi về ƯCLN trước đi` |
| Muốn ít chữ hơn | `Ít chữ hơn nhé, mỗi ý 1 hình thôi` |
| Muốn nhiều chữ hơn | `Thêm nội dung chi tiết vào slide 3 và 5` |

---

## ⏳ BƯỚC 4 — CHỜ TRỢ LÝ AI TẠO SLIDE *(3 – 7 phút, không cần làm gì)*

Trợ lý AI sẽ tự động thực hiện toàn bộ các bước sau — thầy cô không cần làm gì thêm:

- ✅ Đọc và phân tích toàn bộ tài liệu giáo án
- ✅ Tìm kiếm hình ảnh thực tế minh họa từ Internet
- ✅ Thiết kế slide chuyên nghiệp theo chuẩn sư phạm GDPT 2018
- ✅ Tạo công thức toán học chuẩn OMML *(click đúp sửa được ngay trong PowerPoint)*
- ✅ Cài đặt hiệu ứng trình chiếu phù hợp
- ✅ Xuất file PowerPoint (.pptx) chỉnh sửa 100%
- ✅ Kiểm tra chất lượng tự động trước khi giao file

> [!IMPORTANT]
> Thầy cô **không cần ngồi nhìn màn hình chờ**. Có thể làm việc khác. Khi xong, trợ lý sẽ thông báo và hiện link tải file.

---

## 🎉 BƯỚC 5 — NHẬN FILE VÀ MỞ POWERPOINT

Khi trợ lý AI hoàn thành, sẽ xuất hiện **đường link màu xanh** → Thầy cô click vào để mở file ngay.

Hoặc tìm file trong thư mục **Downloads (Tải xuống)**:

1. Nhấn `Windows + E` → mở cửa sổ thư mục máy tính
2. Chọn **"Downloads"** hoặc **"Tải xuống"** ở cột trái
3. Tìm file `.pptx` vừa được tạo *(sắp xếp theo ngày mới nhất — file ở đầu tiên)*
4. Nhấp **đúp chuột** vào file để mở bằng PowerPoint ✔

---

## 🖥️ BƯỚC 6 — TRÌNH CHIẾU VÀ CHỈNH SỬA TRONG POWERPOINT

### ▶️ Trình chiếu ngay trên lớp:

| Muốn làm gì | Nhấn phím |
|:---|:---:|
| Bắt đầu chiếu từ slide 1 | `F5` |
| Chiếu từ slide đang xem | `Shift + F5` |
| Sang slide tiếp theo | `→` *(mũi tên phải)* |
| Quay lại slide trước | `←` *(mũi tên trái)* |
| Thoát khỏi chế độ chiếu | `Esc` |

---

### ✏️ Chỉnh sửa nội dung bất kỳ:

1. **Nhấp chuột 1 lần** vào vùng văn bản cần sửa
2. **Nhấp đúp** *(2 lần nhanh)* để vào chế độ chỉnh sửa
3. Xóa / gõ nội dung mới bình thường như trong Word
4. Nhấp ra ngoài khi xong

---

### 🔢 Chỉnh sửa công thức toán học *(Đặc biệt quan trọng — không cần MathType)*

> [!IMPORTANT]
> Công thức trên slide được tạo theo chuẩn Native OMML của Microsoft PowerPoint. Thầy cô **không cần cài MathType** hay bất kỳ phần mềm phụ trợ nào.

1. **Nhấp đúp chuột trực tiếp vào công thức**
2. Thanh công cụ **"Equation Tools"** *(Công cụ Phương trình)* hiện ra ở trên cùng
3. Dùng các nút trên thanh công cụ để:
   - Thay số trong công thức
   - Đổi dấu `+` thành `-` hoặc ngược lại
   - Thêm/bớt phần tử trong phân số, hệ phương trình
4. Nhấp ra ngoài khi xong ✔

---

## 🆘 BẢNG XỬ LÝ KHI GẶP SỰ CỐ

| Vấn đề thầy cô gặp | Gõ vào chat để yêu cầu sửa |
|:---|:---|
| Slide quá nhiều chữ | *"Ít chữ hơn nhé, mỗi slide chỉ 3–4 dòng thôi"* |
| Chữ quá nhỏ | *"Chữ nội dung nhỏ quá, tăng lên cỡ 20 đi"* |
| Công thức toán không đẹp / bị nhỏ | *"Công thức bị nhỏ, làm to lên cỡ 28pt và dùng OMML nhé"* |
| Màu sắc không hợp | *"Đổi sang màu [màu thầy cô muốn] nhé"* |
| Thiếu ảnh minh họa | *"Tìm thêm ảnh thực tế cho slide 3 và slide 5"* |
| Muốn thêm hiệu ứng click | *"Thêm hiệu ứng xuất hiện từng dòng khi click chuột"* |
| Muốn thêm lời giải | *"Thêm slide lời giải chi tiết cho bài tập ở slide 8"* |
| File không mở được | Kiểm tra đã cài **Microsoft PowerPoint 2016** trở lên chưa |
| Muốn làm lại hoàn toàn | *"Làm lại từ đầu nhé, lần này tôi muốn [mô tả lại yêu cầu]"* |

---

## ⌨️ PHÍM TẮT VÀNG CẦN NHỚ

| Phím tắt | Làm gì |
|:---:|:---|
| `Ctrl + C` | Sao chép *(copy)* |
| `Ctrl + V` | Dán *(paste)* |
| `Ctrl + Shift + C` | Copy đường dẫn file *(khi nhấp chuột phải vào file)* |
| `F5` | Bắt đầu trình chiếu từ slide 1 |
| `Shift + F5` | Chiếu từ slide đang mở |
| `→` | Chuyển slide tiếp theo *(khi đang chiếu)* |
| `Esc` | Thoát khỏi chế độ chiếu |
| `Ctrl + S` | Lưu file *(nhớ lưu sau khi chỉnh sửa!)* |
| `Ctrl + Z` | Hoàn tác *(undo — khi sửa nhầm)* |

---

## 💡 5 MẸO HỮU ÍCH TỪ THỰC TẾ SỬ DỤNG

> [!TIP]
> Đây là những mẹo thực tế được các thầy cô chia sẻ lại sau khi dùng thành thạo.

**Mẹo 1 — "Gửi cả bộ giáo án, không cần lọc trước":**  
Cứ gửi nguyên file giáo án dài — kể cả phần mục tiêu, năng lực số, yêu cầu cần đạt... Trợ lý AI sẽ **tự động lọc bỏ phần hành chính**, chỉ giữ lại nội dung tiến trình dạy học thực sự cần cho học sinh.

**Mẹo 2 — "Chụp ảnh bài tập từ sách, gửi thẳng":**  
Thấy bài tập hay trong sách bài tập hoặc đề kiểm tra cũ → chụp ảnh bằng điện thoại → gửi vào chat và gõ thêm: *"Tạo slide lời giải chi tiết cho bài tập này, có công thức to rõ"*.

**Mẹo 3 — "Lưu câu lệnh hay vào Notepad để tái sử dụng":**  
Khi tìm ra câu lệnh nào tạo ra bài giảng đẹp đúng ý → copy câu lệnh đó ra một file Notepad lưu trên màn hình Desktop. Lần sau chỉ cần mở ra, đổi tên bài và gửi lại — không cần gõ lại từ đầu.

**Mẹo 4 — "Nói thẳng điều mình muốn, không cần dùng từ kỹ thuật":**  
Thay vì lo nghĩ *"mình dùng từ kỹ thuật này có đúng không?"*, cứ nói đúng ý như đang nói với người thật:  
- *"Slide này chữ bé quá, to lên đi"*  
- *"Hình này không liên quan, đổi hình khác"*  
- *"Thêm ô màu vàng bao quanh phần ghi nhớ"*

**Mẹo 5 — "Dùng bài giảng cũ đẹp làm khuôn cho bài mới":**  
Khi đã có 1 bài giảng ưng ý, gửi file đó vào chat và gõ: *"Lấy phong cách thiết kế của file này, làm thêm bài [tên bài mới] theo cùng kiểu"*. Trợ lý sẽ giữ nguyên màu sắc, bố cục, font chữ yêu thích của thầy cô.

---

## 🎯 TÓM TẮT QUY TRÌNH 6 BƯỚC

```
┌──────────────────────────────────────────────────────────────┐
│                                                               │
│  🔰  BƯỚC 0  Mở cửa sổ chat trợ lý AI                      │
│       ↓                                                       │
│  📂  BƯỚC 1  Gửi file tài liệu vào chat                    │
│              (Kéo thả / Copy đường dẫn / Chụp ảnh / Gõ)    │
│       ↓                                                       │
│  💬  BƯỚC 2  Gõ câu lệnh tạo slide (copy mẫu ở trên)       │
│       ↓                                                       │
│  👀  BƯỚC 3  Duyệt kịch bản → Gõ "Đồng ý, làm đi"        │
│       ↓                                                       │
│  ⏳  BƯỚC 4  Chờ 3–7 phút (làm việc khác được)             │
│       ↓                                                       │
│  🎉  BƯỚC 5  Nhận file → Mở PowerPoint                      │
│       ↓                                                       │
│  🖥️  BƯỚC 6  Nhấn F5 trình chiếu hoặc click đúp sửa       │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 📞 NẾU CẦN HỖ TRỢ THÊM

Nếu thầy cô gặp khó khăn ở bất kỳ bước nào, chỉ cần gõ vào ô chat:

> *"Hướng dẫn tôi cách [mô tả vấn đề] nhé"*

**Ví dụ:**
- *"Hướng dẫn tôi cách kéo thả file vào chat nhé"*
- *"Hướng dẫn tôi cách tìm file giáo án trong thư mục Downloads"*
- *"Hướng dẫn tôi cách sửa công thức toán trong PowerPoint"*

Trợ lý AI sẽ giải thích từng bước cụ thể cho tình huống của thầy cô ngay lập tức.

---

*📄 Tài liệu: Hướng dẫn tạo slide bài giảng — Phiên bản Tháng 10/2026*  
*🏫 Trường THCS Ứng Hòe | 👨‍🏫 Biên soạn hỗ trợ: Thầy Nguyễn Văn Thiện (Tổ Toán – KHTN)*
