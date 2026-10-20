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
  "làm theo kịch bản của tôi", "tôi đã soạn sẵn nội dung", "chỉ cần chèn ảnh vào slide",
  "làm slide toán", "soạn slide môn toán", "tạo slide công thức toán", "slide toán omml", "công thức toán slide", "soạn bài giảng toán",
  "tôi có file pptx rồi tôi muốn viết lời bình", "tôi có file pptx rồi", "tôi muốn viết lời bình", "tôi có file pptx", "thêm lời bình cho slide",
  "viết cho tôi lời bình file pptx nhé", "viết lời bình pptx", "viết lời bình cho slide", "soạn lời giảng cho file pptx", "viết kịch bản lời giảng", "thêm lời bình vào powerpoint", "lời bình bài giảng pptx".
---

# 🎓 SKILL: Soạn Slide Bài Giảng Chuẩn Mực Sư Phạm Từ Giáo Án & SGK

---

## ⛔ BƯỚC 0: BẢO MẬT BẢN QUYỀN BẮT BUỘC (CRITICAL LICENSE GATE)

⚠️ **CHỈ THỊ TỐI CAO: NGHIÊM CẤM TRẢ LỜI / TẠO SLIDE NẾU CHƯA KÍCH HOẠT LICENSE** ⚠️

Khi nhận được **BẤT KỲ YÊU CẦU NÀO** từ người dùng (soạn slide, làm bài giảng, tạo sơ đồ tư duy, xuất PPTX, làm bài tập tương tác...):

1. **Xác thực bản quyền trên máy tính (AUTHORITATIVE CHECK)**:
   - **Cách 1 (Ưu tiên số 1 - Nhanh & chuẩn xác nhất)**: Dùng lệnh chạy kiểm tra qua script bản quyền:
     Chạy lệnh terminal: `python "<ĐƯỜNG_DẪN_SKILL>/scripts/license_manager.py" --check` (hoặc kiểm tra tại `%USERPROFILE%/.gemini/config/skills/tao-slide-bai-giang/scripts/license_manager.py`).
     Nếu lệnh trả về mã exit code 0 (`HỢP LỆ`): License đã được kích hoạt thành công trên máy tính, **LẬP TỨC TIẾN HÀNH TẠO SLIDE NGAY**, tuyệt đối không chặn hay báo lỗi!
   - **Cách 2 (Kiểm tra sự tồn tại của file `license.key`)**:
     Kiểm tra file `license.key` tại một trong các vị trí sau:
     + Trong thư mục của skill này (cùng thư mục với `SKILL.md` này).
     + Thư mục toàn cục Antigravity: `%USERPROFILE%/.gemini/config/skills/tao-slide-bai-giang/license.key`
     + Thư mục người dùng: `%USERPROFILE%/.gemini/license.key`
     + Thư mục làm việc hiện tại (workspace root hoặc thư mục con `tao-slide-bai-giang/license.key`).
     👉 **Nếu tìm thấy file `license.key` ở BẤT KỲ VỊ TRÍ NÀO TRÊN**, coi như đã kích hoạt thành công và tiến hành tạo slide ngay!
   - **Cách 3 (Nếu người dùng dán trực tiếp mã License Key vào khung chat)**:
     + Kích hoạt ngay bằng lệnh: `python "<ĐƯỜNG_DẪN_SKILL>/scripts/license_manager.py" --activate "<MÃ_KEY>"`
     + Hoặc tạo file `license.key` với nội dung chuỗi key đó tại cả thư mục skill và thư mục `%USERPROFILE%/.gemini/config/skills/tao-slide-bai-giang/license.key`.
     + Sau đó tiến hành tạo slide ngay cho người dùng!

2. **Nếu và chỉ nếu TẤT CẢ các bước kiểm tra trên đều thất bại (hoàn toàn không có file `license.key` và lệnh --check báo lỗi):**
   - **TUYỆT ĐỐI NGHIÊM CẤM:** Không được sinh bất kỳ slide, SVG, hình ảnh nào ra khung chat, không được soạn bài giảng, không được xuất file PPTX hay vẽ sơ đồ.
   - **CHỈ ĐƯỢC PHÉP TRẢ LỜI DUY NHẤT thông báo sau:**
     > "⛔ **SKILL CHƯA ĐƯỢC KÍCH HOẠT BẢN QUYỀN TRÊN MÁY TÍNH NÀY!**
     >
     > Để sử dụng phần mềm soạn slide bài giảng, thầy/cô vui lòng:
     > 1. Nhấp đúp vào file **`LAY_MA_MAY.bat`** trong thư mục phần mềm để lấy Mã máy (Machine ID).
     > 2. Gửi Mã máy cho tác giả để nhận License Key bản quyền.
     > 3. Nhấp đúp vào file **`KICH_HOAT_BAN_QUYEN.bat`** để dán Key kích hoạt và sử dụng vĩnh viễn (hoặc gửi trực tiếp mã License Key vào khung chat này để em kích hoạt giúp thầy/cô)."
   - **DỪNG TIẾN TRÌNH NGAY LẬP TỨC!** Không trả lời thêm bất kỳ nội dung bài giảng nào.

3. **Kiểm tra Phân Quyền Theo Từng Tiện Ích (`MODULAR FEATURE GATE` - Bắt buộc kiểm tra khi `--check` hợp lệ):**
   - Khi chạy `python "<ĐƯỜNG_DẪN_SKILL>/scripts/license_manager.py" --check`, đọc dòng `UNLOCKED_FEATURES : ...` trong kết quả:
     + Nếu `UNLOCKED_FEATURES : ALL` $\rightarrow$ Giáo viên sở hữu gói **FULL VIP (Trọn bộ tiện ích)**, được phép thực hiện mọi yêu cầu.
     + Nếu `UNLOCKED_FEATURES` chỉ liệt kê một số mã tiện ích cụ thể (mua lẻ từng tiện ích), đối chiếu yêu cầu hiện tại của giáo viên với các mã tiện ích sau:
       * `slide_bai_giang`: Soạn slide bài giảng 3 bước từ giáo án / SGK
       * `so_do_tu_duy`: Tạo sơ đồ tư duy Infographic Radial tỏa tròn
       * `bai_tap_tuong_tac`: Slide bài tập điền từ / trò chơi tương tác có hiệu ứng click
       * `cong_thuc_omml`: Soạn slide có công thức toán học Native OMML chỉnh sửa được
       * `tim_anh_web`: Tự động tìm kiếm và chèn ảnh minh họa từ Internet
       * `video_bai_giang`: Xuất PPTX hỗ trợ lồng tiếng / dựng video bài giảng
     + **Nếu tiện ích giáo viên yêu cầu KHÔNG nằm trong `UNLOCKED_FEATURES`**:
       * **TUYỆT ĐỐI NGHIÊM CẤM** thực thi tiện ích chưa mua đó (kể cả khi giáo viên yêu cầu qua hướng dẫn câu lệnh).
       * **DỪNG NGAY LẬP TỨC** và chỉ trả lời thông báo lịch sự sau:
         > "🔒 **TIỆN ÍCH NÀY CHƯA NẰM TRONG GÓI BẢN QUYỀN HIỆN TẠI CỦA THẦY/CÔ!**
         >
         > • **Tiện ích Thầy/Cô đang yêu cầu:** `<Tên tiện ích đang gọi>`
         > • **Gói bản quyền hiện tại trên máy đang mở khóa:** `<Tên các tiện ích trong Gói mở khóa>`
         >
         > 💡 **Cách mở khóa thêm tiện ích (không cần cài đặt lại phần mềm):**
         > 1. Thầy/Cô vui lòng liên hệ Tác giả để đăng ký mở khóa thêm tiện ích này (hoặc nâng cấp lên gói **FULL VIP Trọn bộ tiện ích**).
         > 2. Sau khi nhận Mã License Key mới từ Tác giả, Thầy/Cô chỉ cần dán trực tiếp mã đó vào khung chat này (hoặc chạy `KICH_HOAT_BAN_QUYEN.bat`) là mở khóa sử dụng được ngay!"

> Chỉ khi nào license hợp lệ VÀ tiện ích nằm trong gói được phép sử dụng thì mới được tiếp tục thực hiện các bước bên dưới!

---

## I. MỤC TIÊU & NGUYÊN TẮC CỐT LÕI (DÀNH RIÊNG CHO THẦY NGUYỄN THIỆN — THCS ỨNG HÒE)

Skill này được thiết kế chuyên biệt và tối ưu riêng cho **Thầy Nguyễn Thiện** (Giáo viên môn KHTN — Trường THCS Ứng Hòe), hỗ trợ chuyển đổi bất kỳ giáo án (Word, PDF), nội dung Sách giáo khoa (SGK) hoặc kịch bản tự soạn thành một bộ slide PowerPoint bài giảng trình chiếu chuyên nghiệp, chuẩn mực sư phạm, đạt độ chính xác cao về mặt khoa học và hình ảnh hiển thị sắc nét nhất trên máy chiếu.

### 🌟 Hồ sơ Giáo viên mặc định:
- **Giáo viên**: Nguyễn Thiện
- **Đơn vị**: Trường THCS Ứng Hòe
- **Cấp học**: THCS (Lớp 6, 7, 8, 9)
- **Bộ môn phụ trách**: Khoa học tự nhiên (Vật lí, Hóa học, Sinh học) & Toán học
- **Font chuẩn**: Times New Roman (hiển thị 100% tiếng Việt có dấu, không đè chữ)
- **Màu chủ đạo mặc định**: `#1F4E79` (STEM Xanh Navy chuyên môn) hoặc đổi linh hoạt theo từng phân môn.

---

### 10 Nguyên tắc vàng tạo PPTX chuẩn mực:
1. **Loại bỏ 100% slide hành chính rườm rà**:
   - Tuyệt đối **không** tạo các slide: "Mục tiêu bài học", "Năng lực số và AI", "Phẩm chất và năng lực", "Tiến trình dạy học", "Yêu cầu cần đạt".
   - Bộ slide trình chiếu chỉ phục vụ học sinh trên lớp theo chuẩn **Công văn 5512**:
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
6. **Quy chuẩn Cỡ Chữ Chiếu Lớp Học Chuẩn Mực (Chống Chữ Nhỏ Khi Chiếu Máy Chiếu)**:
   - **Font chữ toàn bài**: **Times New Roman** (`Times New Roman, serif`).
   - **Quy đổi DPI bắt buộc (PowerPoint Display Engine)**: `1 px = 0.75 pt` $\implies$ `px = pt / 0.75` (hoặc `pt = px * 0.75`).
   - **Nâng toàn bộ cỡ chữ lên chuẩn Trình chiếu lớp học (Presentation Mode)** để học sinh ngồi cuối lớp (khoảng cách 8–10m) nhìn rõ từng nét:
     - 🌟 **Tiêu đề của bài, tên slide (Slide Title)**: **32pt – 36pt** (rực rỡ, to rõ) $\to$ SVG ghi `font-size="42.67"` đến `48.0` (`sz="3200"` đến `"3600"`).
     - 🌟 **Tiêu đề các phần / thẻ / khung ghi nhớ (Section / Box Header)**: **24pt – 26pt** $\to$ SVG ghi `font-size="32.0"` đến `34.67` (`sz="2400"` đến `"2600"`).
     - 🌟 **Nội dung bài học / câu hỏi thảo luận / chốt kiến thức (Body text)**: **20pt – 24pt** (tối thiểu 20pt, chuẩn mực là 22pt–24pt) $\to$ SVG ghi `font-size="26.67"` đến `32.0` (`sz="2000"` đến `"2400"`). Tuyệt đối **không** để 18pt vì quá nhỏ trên máy chiếu.
     - 🌟 **Chú thích ảnh, số trang, chân trang (Caption/Footer)**: **16pt – 18pt** $\to$ SVG ghi `font-size="21.33"` đến `24.0` (`sz="1600"` đến `"1800"`).
   - Sau khi xuất PPTX, chạy script vá theme và run element để đảm bảo DrawingML ribbon hiển thị chuẩn xác 100% `Times New Roman`.

6.B. **Quy Tắc Tuyệt Đối Chống Tràn Chữ Khỏi Khung (Frame Text Overflow Prevention)**:
   - **Quy tắc 1: Công thức tính chiều cao khung (`height`)**:
     Khi vẽ khung chữ nhật (`<rect>`) hoặc khung vẽ tay (`<use href="#ht-khung-but-da">`), chiều cao khung phải được tính toán đủ cho toàn bộ các dòng chữ:
     `Chiều cao khung (H) >= Padding trên (35px) + Padding dưới (35px) + (Số dòng * khoảng cách dòng dy)`
     *Ví dụ: Khung có tiêu đề + 3 dòng ghi nhớ (tổng 4 dòng text), mỗi dòng cách nhau `dy="38"`, thì chiều cao khung tối thiểu phải là: `35 + 35 + (4 * 38) = 222px` $\to$ Đặt `height="230"` đến `240` để có khoảng thở.*
   - **Quy tắc 2: Chống tràn mép phải (Bắt buộc ngắt dòng `<tspan>`)**:
     Một dòng text trong khung chỉ chứa tối đa **10 – 12 từ** (khoảng 40 – 48 ký tự tiếng Việt). Vượt quá độ dài này, **bắt buộc phải ngắt sang dòng mới** bằng `<tspan x="[tọa độ lề trái khung + 40]" dy="38">`. Tuyệt đối không để một câu dài tuột chạy thẳng sang mép phải khung.
   - **Quy tắc 3: Tối đa số lượng dòng trong một khung**:
     Mỗi khung "Em cần ghi nhớ" hoặc "Thảo luận" chỉ chứa tối đa **3 – 4 ý gạch đầu dòng ngắn gọn**, cô đọng. Không bao giờ đưa cả đoạn văn dài vào khung.
   - **Quy tắc 4: Khoảng đệm an toàn với khung vẽ tay (`ht-khung-but-da`)**:
     Vì khung vẽ tay có đường viền lượn sóng và góc nghiêng, vị trí đặt chữ `x` phải cách mép trái khung tối thiểu **40px**, mép trên tối thiểu **35px**, và mép phải cách ít nhất **40px** để chữ không bao giờ đè lên hoặc vượt qua nét vẽ viền.
7. **Bắt buộc lập Bản phác thảo chi tiết (Storyboard) từng slide duyệt trước khi tạo PPTX**:
   - Khi có file giáo án, file SGK hoặc tài liệu giảng dạy, trợ lý **bắt buộc** phải lập bản phác thảo chi tiết từng slide (mô tả rõ Kênh hình, Kênh chữ/Câu hỏi, Khung ghi nhớ, Lời giảng GV) để thầy Nguyễn Thiện duyệt.
   - **Tuyệt đối không chạy lệnh tạo slide hay init project** khi chưa có sự phản hồi đồng ý của thầy.
8. **Cơ chế linh hoạt tiếp nhận & xử lý 3 nguồn hình ảnh**:
   - Bài giảng không làm bài toàn chữ, nhưng không chèn ảnh trang trí vô nghĩa.
   - Xử lý mượt mà cả 3 nguồn ảnh: (1) Bóc tách trực tiếp từ PDF SGK/ảnh chụp điện thoại; (2) Lấy ảnh từ thư mục riêng trên máy giáo viên; (3) Tự động tìm kiếm ảnh thực tế/hiển vi khoa học chất lượng cao từ web (Openverse & Wikimedia).
9. **8 Kiểu Slide Chuẩn Mực Sư Phạm Có Tên Gọi (`docs/vi/tro-ly/kieu-slide.md`)**:
   - `Học đường sáng` *(Mặc định cho KHTN, Toán)*: Nền trắng/kem nhạt, tương phản cao cho học sinh cuối lớp nhìn rõ, bo góc nhẹ, thanh lịch.
   - `Bút dạ – sổ tay`: Nền giấy ấm, vệt bút dạ dưới từ khóa quan trọng, khung vẽ tay quanh khối nội dung, mũi tên sao vẽ tay, hợp bài ôn tập / sơ đồ tư duy.
   - `Cắt dán giấy`: Nền giấy kem xé mép, ảnh có viền trắng dán băng dính, chấm tram nghệ thuật, đồng bộ phong cách với video Vox.
   - `Sách tranh`: Màu sắc phấn tươi vui, khối bo tròn lớn, tranh vẽ trực quan cho học sinh nhỏ.
   - `Ruy băng hành chính`: Ruy băng vát chéo trang trọng, thẻ số liệu gọn gàng (hợp Báo cáo, Tổng kết, Đại hội).
   - `Lễ hội Đoàn`: Tươi vui, ruy băng cờ, dải giấy xé, hoa giấy (hợp sự kiện, cuộc thi, hoạt động Đội/Đoàn).
   - `Học thuật – hội thảo`: Xanh đậm Navy/Teal sang trọng, biểu đồ số liệu khoa học, seminar chuyên môn.
   - `Kính mờ CLB`: Nền tối viền sáng, thẻ kính mờ phát sáng công nghệ, hợp ngày hội STEM / CLB Tin học.
10. **Bộ 12 Họa Tiết Vẽ Tay Native DrawingML (`tools/vi/hoa_tiet/`)**:
   - Hỗ trợ nhúng 12 họa tiết vector nguyên bản vào slide: `bang-dinh.svg` (băng dính dán góc ảnh), `giay-xe-ngang.svg` (dải giấy xé), `ruy-bang.svg` (ruy băng tiêu đề), `gach-but-da.svg` (vệt highlight dưới từ khóa), `khung-but-da.svg` (khung vẽ tay bao quanh ghi nhớ), `sao-ve-tay.svg` (sao điểm nhấn), `mui-ten-ve-tay.svg` (mũi tên chỉ vào hình), `cham-tram.svg` (halftone), `o-ke.svg` (giấy kẻ ô cho công thức), `goc-nguech.svg`, `hoa-giay.svg`, `ngoac-kep.svg`.
   - **Nguyên tắc vector Native**: Tất cả đều là hình khối PowerPoint `<symbol>`/`<use>` hoặc shape chuẩn, có thể đổi màu, kéo giãn to nhỏ mà không bao giờ bị vỡ hạt như hình ảnh thông thường!

---

## II. LUỒNG 1: QUY TRÌNH CẦM TAY CHỈ VIỆC KHI GIÁO VIÊN YÊU CẦU "TÔI MUỐN TẠO PPTX" (CHUẨN 5 BƯỚC)

Khi giáo viên gửi câu lệnh mở đầu chung chung như:
> *"Tôi muốn làm pptx"*, *"Tôi muốn tạo pptx"*, *"Tôi muốn làm slide"*, *"Làm slide cho tôi"*, *"Tạo bài giảng pptx"*... (chưa đính kèm tài liệu cụ thể)

Trợ lý **bắt buộc không được tự ý tạo bài ngay, không hỏi các câu hỏi lý thuyết phức tạp dồn dập**, mà phải thực hiện đúng chuẩn 5 bước "Cầm tay chỉ việc":

---

### 🔹 BƯỚC 1: Hiển thị Menu 5 loại việc & Hỏi thầy cô chọn lựa chọn nào để hướng dẫn tiếp
Trợ lý phản hồi ngay mẫu sau:
```markdown
Hồ sơ hiện tại: **Trường THCS Ứng Hòe — Nguyễn Thiện**. Dùng tiếp?

Dạ, thầy/cô muốn tạo bài thuyết trình PowerPoint (PPTX) cho loại việc nào dưới đây ạ?

1. **Bài giảng dạy học** *(Gợi ý: bài học môn KHTN, Toán... theo phân phối chương trình)*
2. **Báo cáo – tổng kết** *(sơ kết học kỳ, tổng kết năm học, hội nghị viên chức, thi đua...)*
3. **Hoạt động Đoàn – Đội – sự kiện** *(Đại hội chi đoàn, lễ kỷ niệm, cuộc thi, ngoại khóa...)*
4. **Tập huấn / workshop / sinh hoạt chuyên môn** *(chia sẻ chuyên đề, bồi dưỡng giáo viên...)*
5. **Poster / ấn phẩm trình chiếu Zalo – Facebook**

👉 **Thầy/cô chọn lựa chọn số mấy (1, 2, 3, 4 hay 5) để em đưa hướng dẫn chi tiết từng bước cho thầy/cô nhé!**
```
> ⚠️ **DỪNG VÀ CHỜ**: Trợ lý dừng lại chờ thầy cô chọn số, không tự ý chạy lệnh init dự án.

---

### 🔹 BƯỚC 2: Khi giáo viên chọn Số 1 (Bài giảng) — Đưa ngay Hướng Dẫn Cầm Tay Chỉ Việc, Hỏi Mục Đích A/B & Menu Phong Cách / Mẫu Slide

Khi giáo viên gõ `1`, hoặc cung cấp tên môn học/bài dạy:
Trợ lý gửi ngay phản hồi hướng dẫn chi tiết theo mẫu:

```markdown
Dạ tuyệt vời ạ! Để em hỗ trợ Thầy/Cô thiết kế bài giảng chuẩn mực sư phạm và đúng ý nhất, Thầy/Cô làm theo 3 bước hướng dẫn ngắn gọn dưới đây nhé:

---
### 📂 BƯỚC 1: LẤY ĐƯỜNG DẪN FILE GIÁO ÁN (WORD) HOẶC SÁCH GIÁO KHOA (PDF)
- Mở thư mục chứa file **Giáo án (Word `.docx`)** hoặc **Sách giáo khoa (PDF)** trên máy tính.
- Nhấp **Chuột phải** vào file ➔ chọn **"Copy as path"** *(hoặc bấm tổ hợp phím `Ctrl + Shift + C`)*.

---
### 🎯 BƯỚC 2: CHỌN MỤC ĐÍCH SỬ DỤNG (CHỌN A HOẶC B)
* **Lựa chọn A — Trình chiếu dạy học trên lớp (Mặc định):**
  - Chữ to rõ (32–36pt tiêu đề, 22–24pt nội dung), khung ghi nhớ không tràn chữ, học sinh cuối lớp nhìn rõ.
  - Tiến trình sư phạm tương tác: Quan sát kênh hình ➔ Câu hỏi phát vấn ➔ Khung "💡 Em cần ghi nhớ" chốt bài ghi vở.
* **Lựa chọn B — Xuất thành Video bài giảng tự động:**
  - Viết toàn văn lời bình phát thanh viên từng câu từng chữ chuẩn thời lượng (3–5 phút hoặc 8–10 phút).
  - Tự động nạp vào Notes để xuất video MP4 có giọng đọc AI tự chạy đồng bộ.

---
### 🎨 BƯỚC 3: CHỌN PHONG CÁCH & MẪU SLIDE THẦY/CÔ YÊU THÍCH (CHỌN THEO SỐ HOẶC TÊN)

Em đã tích hợp sẵn kho phong cách chuẩn mực sư phạm và các mẫu hoạt cảnh đặc sắc từ kho mẫu 28 bài giảng thực tế để Thầy/Cô tùy ý chọn:

#### 🌟 NHÓM 1: PHONG CÁCH BÀI GIẢNG CHUẨN SGK GDPT 2018
* **[1] Học đường sáng** *(Mặc định cho Toán, KHTN, Lý, Hóa, Sinh)*: Nền trắng/kem sáng tinh khôi, tương phản rất cao, khối bo góc nhẹ, thanh lịch, học sinh ngồi bàn cuối nhìn cực rõ.
* **[2] Bút dạ – sổ tay**: Nền giấy ấm, vệt bút dạ highlight màu dưới từ khóa quan trọng, khung vẽ tay bao quanh khối ghi nhớ, mũi tên sao vẽ tay sinh động (rất hợp bài ôn tập, sơ đồ tư duy).
* **[3] Cắt dán giấy**: Nền giấy kem xé mép, ảnh dán viền trắng băng dính, nghệ thuật (rất hợp Ngữ văn, Lịch sử, Địa lí, GDCD; đồng bộ phong cách video Vox).
* **[4] Sách tranh tiểu học**: Màu phấn tươi sáng, khối bo tròn lớn, tranh minh họa nét mực đáng yêu, ít chữ (rất hợp Tiểu học, hoạt động trải nghiệm, ngoại khóa).

#### 🎮 NHÓM 2: MẪU HOẠT CẢNH ĐẶC BIỆT & TRÒ CHƠI TƯƠNG TÁC (TỪ KHO MẪU)
* **[5] Game Show "Ai là triệu phú"**: Khung lục giác phát sáng công nghệ, 4 đáp án A-B-C-D click đổi màu (Vàng khi chọn ➔ Xanh khi đúng ➔ Đỏ khi sai), hợp phần Khởi động hoặc Củng cố.
* **[6] Game Show "Ong non tìm mật / Hái hoa"**: Đám mây câu hỏi bo tròn, hình chú ong/hoa xinh xắn, tạo không khí học tập sôi nổi, hào hứng.
* **[7] Game Show "Rung chuông vàng"**: Đồng hồ đếm ngược 15 giây, hộp câu hỏi trung tâm, chuông reo kịch tính.
* **[8] Báo cáo SKKN & Thi Giáo viên dạy giỏi**: Tông Teal/Pastel sang trọng, thẻ đối chiếu Thực trạng vs Biện pháp, biểu đồ % số liệu khảo sát trước/sau áp dụng.

#### 🏛️ NHÓM 3: PHONG CÁCH SỰ KIỆN, HÀNH CHÍNH & VINH DANH
* **[9] Ruy băng hành chính / Đại hội**: Nền trắng trang nghiêm, ruy băng chéo mang tiêu đề, thẻ số liệu lớn (hợp Sơ kết, Tổng kết, Đại hội, Hội nghị viên chức).
* **[10] Lễ hội Đoàn – Đội & Vinh danh**: Màu cờ hoa rực rỡ, khung viền mạ vàng danh dự (hợp 26/3, 20/11, tuyên dương khen thưởng, CLB STEM).

---
### 📋 MẪU CÂU LỆNH ĐIỀN SẴN (THẦY/CÔ CHỈ CẦN COPY, ĐIỀN VÀO & GỬI CHO EM):

> "Soạn bài giảng [Tên bài], môn [KHTN 6 / Toán...], lớp [6] từ file `"<Dán_đường_dẫn_file_ở_đây>"`.
> - Mục đích: [Chọn Lựa chọn A: Dạy trên lớp / hoặc Lựa chọn B: Xuất Video bài giảng]
> - Phong cách/Mẫu slide: [Chọn số 1 đến 10, hoặc ghi tên kiểu như: 'Học đường sáng', 'Bút dạ – sổ tay', 'Game Ai là triệu phú'...]
> Em hãy đọc giáo án/SGK và lên Bảng kịch bản Storyboard chi tiết từng slide cho tôi duyệt trước nhé!"
```

> ⚠️ **DỪNG VÀ CHỜ**: Trợ lý dừng lại và chờ Thầy/Cô gửi đường dẫn file, lựa chọn mục đích (A hoặc B) và phong cách/mẫu slide đã chọn. **Tuyệt đối không tự ý viết bảng kịch bản dàn ý ngay khi chưa có phản hồi này**, vì kịch bản cho Trình chiếu (A) và kịch bản cho Video (B) có cấu trúc và dung lượng lời bình hoàn toàn khác nhau.

---

### 🔹 BƯỚC 3: Dựa trên lựa chọn A hoặc B, lập Bản phác thảo Kịch bản (Storyboard) gửi thầy cô duyệt trước
Sau khi thầy cô phản hồi thông tin bài dạy và chọn A hoặc B:
- **Nếu chọn A (Trình chiếu trên lớp)**: Lập kịch bản dàn ý tập trung vào tiến trình tổ chức hoạt động dạy học 3 bước (Kênh hình trực quan $\to$ Câu hỏi thảo luận $\to$ Khung "💡 Em cần ghi nhớ" chốt bài ghi vở), lời giảng gợi ý ngắn gọn.
- **Nếu chọn B (Video bài giảng)**: Lập kịch bản chi tiết gồm Kênh hình + Toàn văn lời bình lồng tiếng AI từng câu, tính toán tổng số từ khớp với thời lượng video thầy cô đã chọn (khoảng 120–140 từ/phút).
- **DỪNG VÀ HỎI**: *"Thầy cô xem lại kịch bản dàn ý trên, nếu thầy cô đồng ý (hoặc cần chỉnh sửa slide nào) thì nhắn em để em bắt đầu thiết kế PPTX nhé!"*

---

### 🔹 BƯỚC 4: Thầy cô đồng ý mới tiến hành vẽ SVG & Xuất file PowerPoint Native PPTX
- Khi thầy cô phản hồi "đồng ý", "OK", "tiến hành đi": AI mới bắt đầu khởi tạo dự án, thiết kế SVG chuẩn DrawingML, chạy bộ kiểm chất lượng và xuất file `.pptx` Native DrawingML trực tiếp chỉnh sửa được.

---

### 🔹 BƯỚC 5: Bàn giao file PPTX & Đề xuất xuất Video bài giảng
- Gửi đường dẫn mở file PPTX hoàn chỉnh.
- Đề xuất: *"File PPTX bài giảng của thầy cô đã sẵn sàng. Thầy cô có muốn xuất luôn thành **Video bài giảng** (định dạng MP4 Full HD có lồng tiếng AI phát thanh viên và hiệu ứng tự chạy) không ạ?"*

---

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

## II.B LUỒNG 2: KHI GIÁO VIÊN ĐÃ CÓ FILE PPTX VÀ YÊU CẦU: "TÔI CÓ FILE PPTX RỒI TÔI MUỐN VIẾT LỜI BÌNH"

Khi giáo viên gửi câu lệnh như:
> *"Tôi có file pptx rồi tôi muốn viết lời bình"*, *"Tôi có file pptx rồi"*, *"Tôi muốn viết lời bình cho slide"*, *"Viết cho tôi lời bình file pptx nhé"*, *"Viết lời bình pptx"*, *"Soạn lời giảng cho file pptx"*, *"Thêm lời bình vào powerpoint"*, *"Lời bình bài giảng pptx"*... (chưa đính kèm file cụ thể hoặc chưa chọn mục đích)

Trợ lý **bắt buộc không được trả lời chung chung**, không tự ý viết lời bình khi chưa biết mục đích, mà thực hiện đúng chuẩn 4 bước "Cầm tay chỉ việc":

---

### 🔹 BƯỚC 1: Hướng Dẫn Copy As Path File PPTX, Hỏi Mục Đích A/B & Menu Phong Cách Lời Bình / Thể Loại Bài
Trợ lý phản hồi ngay bản hướng dẫn:
```markdown
Hồ sơ hiện tại: **Trường THCS Ứng Hòe — Nguyễn Thiện**. Dùng tiếp?

Dạ kính chào Thầy/Cô! Để em hỗ trợ đọc toàn bộ slide trong file PowerPoint có sẵn của Thầy/Cô và soạn bộ Lời bình / Lời giảng bám sát từng trang đúng giọng văn mong muốn, Thầy/Cô làm theo 3 bước cực kỳ đơn giản dưới đây nhé:

---
### 📂 BƯỚC 1: LẤY ĐƯỜNG DẪN FILE POWERPOINT (.pptx)
Thầy/Cô chọn **1 trong 2 cách** tiện nhất trên máy tính:
- **Cách 1 (Kéo thả chuột - Dễ nhất):** Mở thư mục chứa file `.pptx` trên máy tính $\to$ kéo thả trực tiếp file vào khung chat này.
- **Cách 2 (Copy as path - Rất nhanh):** Tìm file `.pptx` trên máy tính $\to$ giữ phím `Shift` + nhấp **Chuột phải** vào file $\to$ chọn **"Copy as path"** *(hoặc bấm tổ hợp `Ctrl + Shift + C`)*.

---
### 🎯 BƯỚC 2: CHỌN MỤC ĐÍCH SỬ DỤNG LỜI BÌNH (CHỌN A HOẶC B)
Thầy/Cô dự định dùng lời bình này cho mục đích nào dưới đây ạ?

* **Lựa chọn A — Lời bình giảng bài trên lớp (Ghi chú Notes cho Thầy/Cô):**
  - Viết các ý gợi mở tự nhiên, câu hỏi phát vấn học sinh, hướng dẫn quan sát sơ đồ/hình ảnh và chốt kiến thức trọng tâm.
  - Phù hợp để Thầy/Cô bật chế độ **Presenter View** trên máy tính khi dạy học, nhìn vào màn hình phụ để giảng bài lưu loát mà không sợ quên ý.

* **Lựa chọn B — Toàn văn kịch bản lồng tiếng thu âm / Xuất Video bài giảng tự động:**
  - Viết đầy đủ trọn vẹn từng câu từng chữ chuẩn phát thanh viên (không viết tắt ký hiệu công thức).
  - Canh chuẩn thời lượng video (Thầy/Cô có thể chọn: video tóm tắt 3–5 phút hay bài giảng đầy đủ 8–10 phút; trung bình 60–120 từ/slide).
  - Tự động nạp vào mục Notes để xuất thành Video bài giảng MP4 có giọng đọc AI phát thanh viên tự động chạy.

---
### 🎙️ BƯỚC 3: CHỌN PHONG CÁCH LỜI BÌNH & THỂ LOẠI BÀI (CHỌN THEO SỐ HOẶC TÊN)

Em đã tích hợp sẵn các phong cách lời bình chuyên nghiệp cho từng thể loại bài để Thầy/Cô tùy ý lựa chọn:

#### 🌟 NHÓM 1: BÀI GIẢNG DẠY HỌC CHUẨN SGK GDPT 2018
* **[1] Giảng bài truyền cảm, gợi mở** *(Mặc định cho Toán, KHTN)*: Dẫn dắt học sinh quan sát kênh hình/sơ đồ, đặt câu hỏi phát vấn, giải thích dễ hiểu, chốt ghi nhớ.
* **[2] Ôn tập & Sơ đồ tư duy (Bút dạ – sổ tay)**: Nhấn mạnh từ khóa trọng tâm, hệ thống hóa kiến thức logic, lời dẫn ngắn gọn, đọng lại ý cốt lõi.
* **[3] Kể chuyện & Khám phá (Cắt dán / Xã hội)**: Giọng văn truyền cảm, liên hệ thực tế đời sống sinh động (rất hợp Ngữ văn, Lịch sử, Địa lí, GDCD).
* **[4] Dịu dàng, vui tươi (Sách tranh tiểu học)**: Nhẹ nhàng, gần gũi, khích lệ và tương tác ấm áp với học sinh lứa tuổi nhỏ.

#### 🎮 NHÓM 2: DẪN DẮT HOẠT CẢNH TRÒ CHƠI HỌC TẬP (GAME SHOW)
* **[5] MC Game Show "Ai là triệu phú"**: Sôi nổi, hồi hộp, kịch tính, lôi cuốn học sinh tham gia chọn đáp án A-B-C-D.
* **[6] Dẫn dắt Game "Ong tìm mật / Hái hoa / Rung chuông vàng"**: Hào hứng, cổ vũ, chúc mừng học sinh trả lời đúng, giải thích ngắn gọn câu trả lời.

#### 🏛️ NHÓM 3: BÁO CÁO CHUYÊN ĐỀ, HỘI THI & SỰ KIỆN
* **[7] Báo cáo SKKN & Thi Giáo viên dạy giỏi**: Đĩnh đạc, mạch lạc, lập luận sư phạm vững vàng, thuyết minh rõ nét số liệu khảo sát % hiệu quả biện pháp.
* **[8] Thuyết trình Đại hội / Hội nghị viên chức**: Trang nghiêm, chuẩn mực hành chính công vụ, dõng dạc, mạch lạc từng mục báo cáo và phương hướng.
* **[9] Lễ Vinh danh & Tuyên dương thành tích**: Hào hùng, truyền cảm hứng, tôn vinh trang trọng các cá nhân và tập thể tiêu biểu.

---
### 📋 MẪU CÂU LỆNH ĐIỀN SẴN (THẦY/CÔ CHỈ CẦN COPY & GỬI CHO EM):
> *"Tôi có file PowerPoint bài giảng: `"<Dán_đường_dẫn_file_pptx_ở_đây>"`. 
> - Môn: [KHTN 6 / Toán...], Lớp: [6].
> - Mục đích: [Chọn Lựa chọn A: Dạy trên lớp / hoặc Lựa chọn B: Xuất Video bài giảng - thời lượng ... phút]
> - Phong cách lời bình: [Chọn số 1 đến 9, hoặc ghi tên kiểu như: 'Giảng bài truyền cảm', 'MC Ai là triệu phú', 'Báo cáo SKKN'...]
> Em hãy đọc từng slide và lên Bảng kịch bản lời bình cho tôi duyệt trước nhé!"*
```

> ⚠️ **DỪNG VÀ CHỜ**: Trợ lý dừng lại chờ giáo viên gửi file `.pptx` (hoặc đường dẫn), chọn **Lựa chọn A hay B** và phong cách lời bình. **Tuyệt đối không tự ý viết lời bình trước khi có phản hồi này**, vì phong cách giảng trực tiếp trên lớp (A) và kịch bản đọc video lồng tiếng AI (B) có yêu cầu câu từ, độ dài và cấu trúc hoàn toàn khác nhau.

---

### 🔹 BƯỚC 2: Trích Xuất Nội Dung PPTX & Lập Bảng Kịch Bản Lời Bình Storyboard Gửi Thầy Cô Duyệt
Sau khi giáo viên gửi file và lựa chọn A hoặc B:
1. Trợ lý chạy script trích xuất dữ liệu slide:
   `python "<ĐƯỜNG_DẪN_SKILL>/scripts/them_loi_binh_pptx.py" "<file.pptx>" --extract`
2. Biên soạn lời bình chi tiết theo đúng lựa chọn (A hoặc B) và tuân thủ 6 nguyên tắc vàng (bám sát hình ảnh/công thức/câu hỏi trên slide, tự nhiên, có câu nối chuyển slide).
3. Trình bày Bảng Lời Bình Storyboard rõ ràng:
   `| Slide | Tiêu đề slide | Nội dung chính trên slide | Lời bình chi tiết (Từng câu từng chữ) | Thời lượng dự kiến |`
4. **DỪNG VÀ HỎI**: 
   > *"Thầy/Cô xem lại Bảng kịch bản lời bình từng slide trên. Nếu Thầy/Cô đồng ý (hoặc cần chỉnh sửa câu chữ ở slide nào), xin nhắn cho em để em nạp thẳng vào mục Notes của file PowerPoint nhé!"*

---

### 🔹 BƯỚC 3: Giáo Viên Đồng Ý $\to$ Tự Động Nạp (Inject) Lời Bình Vào Mục Notes Của PowerPoint
- Khi giáo viên nhắn *"Đồng ý"*, *"OK"*, *"Nạp vào slide đi"*:
  1. Trợ lý lưu nội dung lời bình ra file JSON tạm.
  2. Chạy lệnh:
     `python "<ĐƯỜNG_DẪN_SKILL>/scripts/them_loi_binh_pptx.py" "<file.pptx>" --inject-json "<file_notes.json>"`
  3. Lệnh tạo ra file mới an toàn: `[Tên_File_Gốc]_CoLoiBinh.pptx` (giữ nguyên 100% định dạng, hình ảnh, font chữ gốc, chỉ thêm văn bản vào phần Notes chân slide).

---

### 🔹 BƯỚC 4: Bàn Giao File & Đề Xuất Bước Tiếp Theo
- Bàn giao đường dẫn mở file `[Tên_File_Gốc]_CoLoiBinh.pptx`.
- Hướng dẫn Thầy/Cô cách xem lời bình trong PowerPoint (bấm vào tab **Notes** dưới chân slide hoặc bật **Slide Show $\to$ Use Presenter View** khi cắm máy chiếu).
- **Đặc biệt nếu giáo viên đã chọn Lựa chọn B (hoặc có nhu cầu làm video)**:
  > *"Em đã nạp toàn văn lời bình phát thanh viên vào từng slide. Thầy/Cô có muốn xuất luôn thành **Video bài giảng MP4** (có giọng đọc AI tự động đọc khớp từng slide và chuyển cảnh) không ạ?"*

---

---

### 🌟 6 NGUYÊN TẮC VÀNG KHI VIẾT LỜI BÌNH BÁM SÁT SLIDE POWERPOINT

Khi nhận được file `.pptx`, trợ lý chạy lệnh `python scripts/them_loi_binh_pptx.py "<file.pptx>" --extract` để trích xuất toàn bộ tiêu đề, đề mục, nội dung chữ, bảng biểu của từng slide. Sau đó biên soạn lời bình tuân thủ tuyệt đối 6 nguyên tắc:

1. **Bám sát 100% nội dung thực tế trên từng slide**:
   - Slide có định nghĩa hay khái niệm nào $\implies$ Lời bình giảng giải đúng định nghĩa đó, không bịa thêm kiến thức ngoài làm loãng bài.
   - Slide có công thức toán/lý/hóa $\implies$ Lời bình đọc chuẩn xác tên từng ký hiệu (ví dụ: *"Delta phẩy bằng b phẩy bình phương trừ a nhân c"*), giải thích ý nghĩa từng đại lượng và điều kiện áp dụng.
   - Slide có hình ảnh, sơ đồ, đồ thị $\implies$ Lời bình chủ động dẫn dắt: *"Các em hãy quan sát hình ảnh ở bên trái màn hình...", "Nhìn vào nhánh số 2 của sơ đồ..."*.
   - Slide có câu hỏi thảo luận / trắc nghiệm $\implies$ Lời bình đặt câu hỏi gợi mở, gợi ý hướng suy nghĩ, sau đó phân tích tại sao phương án đó là đáp án chính xác.
   - Slide có khung chốt ghi nhớ $\implies$ Lời bình nhấn mạnh: *"Đây là kiến thức trọng tâm của bài, các em hãy ghi cẩn thận nội dung đóng khung này vào vở nhé."*
2. **Khẩu khí sư phạm tự nhiên, ấm áp**:
   - Xưng hô chuẩn mực: *"Thầy/Cô chào các em..."*, *"Các em thân mến..."*, *"Thầy tin chắc rằng các em đã nhận ra..."*.
   - Tuyệt đối không dùng giọng đọc văn xuôi máy móc hay đọc lại từng chữ trơ trọi trên slide; phải có lời dẫn dắt, giải thích và liên hệ thực tế.
3. **Cầu nối chuyển tiếp mượt mà giữa các slide (Bridging Transitions)**:
   - Cuối mỗi slide có câu nối chuyển tiếp sang slide sau (ví dụ: *"Để hiểu rõ hơn quy tắc này được áp dụng như thế nào, thầy trò chúng ta cùng chuyển sang ví dụ ở slide tiếp theo..."*).
4. **Thời lượng chuẩn nhịp dạy học & làm video**:
   - Mỗi slide thông thường: 60 – 120 từ (tương đương 25 – 45 giây giảng bài).
   - Slide bài tập khó: 120 – 180 từ (khoảng 60 – 80 giây).
5. **Trình bày Bảng Lời Bình Storyboard cho giáo viên duyệt trước**:
   Trợ lý hiển thị bảng đầy đủ các cột:
   `| Slide | Tiêu đề slide | Nội dung slide tóm tắt | Lời bình giảng dạy chi tiết (từng câu từng chữ) | Thời lượng dự kiến |`
6. **Tự động nạp vào Notes của PowerPoint**:
   - Khi giáo viên gõ *"Đồng ý, nạp vào slide"* (hoặc chỉnh sửa xong), trợ lý lưu lời bình ra file JSON tạm và chạy lệnh:
     ```bash
     python "<ĐƯỜNG_DẪN_SKILL>/scripts/them_loi_binh_pptx.py" "<file.pptx>" --inject-json "<file_notes.json>"
     ```
   - Trợ lý xuất ra file mới có tên `[TenBai]_CoLoiBinh.pptx` (toàn bộ lời bình đã nằm gọn trong mục Notes của từng trang) và gửi link mở file trực tiếp cho giáo viên.
   - Sau đó hướng dẫn giáo viên: Mở PowerPoint bấm **Slide Show $\to$ Record** để đọc theo Notes hoặc kéo thả vào `XUAT_VIDEO_TU_PPTX.bat` để xuất video bài giảng MP4.

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

## V. HỆ THỐNG 7 PHONG CÁCH CHỦ ĐỀ (THEME STYLES) & 12 KIỂU BỐ CỤC HOẠT CẢNH (SCENE LAYOUT PATTERNS)

Để bài giảng luôn mới mẻ, cuốn hút và phù hợp với từng môn học, hoạt cảnh sư phạm và thuyết trình, hệ thống kế thừa tinh hoa từ 28 bộ slide mẫu chuyên nghiệp (`MẪU SLIDE` và `STEM_MHHTH_v6`), cung cấp **7 Phong cách bảng màu (Theme Styles)** và **12 Kiểu bố cục hoạt cảnh (Scene Layout Patterns)**. Giáo viên có thể chỉ định hoặc trợ lý tự động điều phối:

### 🎨 1. BẢNG 7 PHONG CÁCH CHỦ ĐỀ MÀU SẮC (7 THEME STYLES)

| Mã Phong Cách | Tên Phong Cách | Nền Slide | Màu Header & Footer | Đường Chỉ / Viền Nhấn | 4 Màu Thẻ Phân Nhóm (Đậm / Nền Nhạt) | Phù Hợp Nhất Cho |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| **Style 1** | **STEM Modern Navy & Gold** | `#F0F5FB` | `#1B3A6B` *(Navy)* | `#E8941A` *(Vàng cam)* | 1. Đỏ `#C0392B` / `#FDEDEC`<br>2. Cam `#E8941A` / `#FFF3DB`<br>3. Ngọc `#16A085` / `#E8F8F5`<br>4. Lam `#1B3A6B` / `#E8EFF8` | Toán học, Vật lí, Tin học, STEM, Báo cáo kỹ thuật |
| **Style 2** | **Bio-Nature Emerald** | `#F2F9F6` | `#0F5132` *(Lục bảo)* | `#F59E0B` *(Vàng nắng)* | 1. Lá `#198754` / `#E8F5E9`<br>2. Cam `#D97706` / `#FEF3C7`<br>3. Biển `#0284C7` / `#E0F2FE`<br>4. Tím `#7C3AED` / `#F3E8FF` | Sinh học, KHTN (Tế bào, Đa dạng sinh học, Môi trường) |
| **Style 3** | **Chem-Lab Royal Purple** | `#F5F3FF` | `#3B0764` *(Tím đậm)* | `#06B6D4` *(Xanh Cyan)* | 1. Tím `#6D28D9` / `#EDE9FE`<br>2. Cyan `#0891B2` / `#CFFAFE`<br>3. Hồng `#BE185D` / `#FCE7F3`<br>4. Cam `#EA580C` / `#FFEDD5` | Hóa học, KHTN (Chất, Nguyên tử, Bảng tuần hoàn) |
| **Style 4** | **Academic Contest & SKKN Pastel** | `#F8FAFC` | `#1F4E79` / `#298771` | `#B5C115` *(Mù tạt)* | 1. Teal `#298771` / `#E6F4F1`<br>2. Lam `#1F4E79` / `#EFF6FF`<br>3. Mù tạt `#B5C115` / `#F7F8E8`<br>4. Mận `#8C213E` / `#FDE8EE` | Báo cáo SKKN, Thi Giáo viên dạy giỏi, Hội nghị chuyên môn |
| **Style 5** | **Interactive Game Show Neon** | `#0A1128` | `#001F3F` *(Xanh thẫm)* | `#00F0FF` / `#FFFF00` | 1. Cyan `#00F0FF` / `#002840`<br>2. Vàng `#FFFF00` / `#333000`<br>3. Xanh lá `#22C55E` / `#052E16`<br>4. Đỏ `#EF4444` / `#380D0D` | Trò chơi Ai là triệu phú, Rung chuông vàng, Khởi động sôi động |
| **Style 6** | **Party Congress & Governance Red-Gold** | `#FFFDF9` | `#990000` *(Đỏ cờ)* | `#FFC000` *(Vàng Gold)* | 1. Đỏ cờ `#990000` / `#FEE2E2`<br>2. Vàng `#D97706` / `#FEF3C7`<br>3. Xanh `#1E3A8A` / `#DBEAFE`<br>4. Nâu `#78350F` / `#FEF2F2` | Đại hội Đảng, Hội nghị CBVC, Báo cáo nhiệm vụ UBND |
| **Style 7** | **Hall of Fame & Honor Metallic** | `#0D1B2A` / `#7A0C0C` | `#1B263B` / `#5A0000` | `#D4AF37` *(Gold kim loại)* | 1. Vàng Gold `#D4AF37` / `#2A2415`<br>2. Đỏ nhung `#B91C1C` / `#2D0A0A`<br>3. Lam sẫm `#1E3A8A` / `#0F172A`<br>4. Bạc `#94A3B8` / `#1E293B` | Lễ Vinh danh, Tuyên dương Gia đình Văn hóa, Khen thưởng thi đua |

---

### 📐 2. MƯỜI HAI KIỂU BỐ CỤC HOẠT CẢNH (12 SCENE LAYOUT PATTERNS TOÀN DIỆN)

Tuyệt đối **không dùng 1 bố cục lặp đi lặp lại**. Trong một bài thuyết trình hay bài giảng (8–16 slide), trợ lý phải luân chuyển linh hoạt các bố cục theo đúng từng hoạt cảnh:

#### 🔹 Layout 1: `Split Visual-Pedagogy` (Trái Kênh Hình 45% – Phải Hỏi & Ghi Nhớ 55%)
- **Hoạt cảnh**: Slide hình thành kiến thức có ảnh SGK, ảnh hiển vi thực tế hoặc sơ đồ thí nghiệm.
- **Cấu trúc**: Cột trái (`x=40..590`) đặt khung ảnh lớn bo góc kèm chú thích; Cột phải (`x=620..1240`) chia 2 hộp: Hộp trên là `❓ CÂU HỎI THẢO LUẬN` (nền vàng nhạt `#FFF3DB`, thanh cam `#E8941A`), hộp dưới là `💡 EM CẦN GHI NHỚ` (nền xanh nhạt `#E8EFF8`, thanh `#1B3A6B`).

#### 🔹 Layout 2: `2x2 Color-Coded Grid` (Lưới 4 Ô Đa Sắc)
- **Hoạt cảnh**: Bài học có **4 phần, 4 vai trò, 4 tính chất, 4 nhóm sinh vật** hoặc **4 câu hỏi luyện tập**.
- **Cấu trúc SVG**: 4 ô chữ nhật bo góc `rx="10"` với 4 cặp màu đậm/nhạt tương phản (`#C0392B`, `#E8941A`, `#16A085`, `#1B3A6B`), thanh tiêu đề cao `52px` in chữ trắng đậm 20pt, thân hộp chứa danh sách gạch đầu dòng `▸`.

#### 🔹 Layout 3: `3-Row Numbered Cards` (3 Dải Thẻ Ngang Đánh Số Lớn)
- **Hoạt cảnh**: Trình bày **3 thành phần chính**, **3 định luật**, hoặc **3 bước cốt lõi**.
- **Cấu trúc SVG**: 3 dải thẻ nằm ngang (`y=130, 310, 490`, `height="160"`). Đầu dải thẻ bên trái có khối màu đậm (`width="85"`) in số thứ tự `1`, `2`, `3` cỡ lớn `42pt` trắng tinh; bên phải in tiêu đề đậm và 2 dòng mô tả.

#### 🔹 Layout 4: `Horizontal Process Flow` (Sơ Đồ Quy Trình Mũi Tên Ngang `▶`)
- **Hoạt cảnh**: **Quy trình thí nghiệm, Chu trình sinh học, Các bước giải bài toán thực tế**.
- **Cấu trúc**: Hộp định nghĩa ở trên, chuỗi 4–6 khối quy trình nối tiếp nhau bằng mũi tên `▶` ở giữa, khung chốt ghi nhớ/tiêu chuẩn ở đáy.

#### 🔹 Layout 5: `Concept Label Stripes` (Bảng Dải Băng Nhãn Màu)
- **Hoạt cảnh**: Bảng tổng hợp thuật ngữ, phân lớp số học, chức năng các bộ phận/bào quan, bảng từ vựng.
- **Cấu trúc**: 4–6 hàng ngang (`height="72"`). Cột trái (`width="320"`) là hộp nhãn màu đặc in chữ trắng đậm; Cột phải (`width="880"`) là hộp nền trắng ghi chức năng và ví dụ.

#### 🔹 Layout 6: `Comparison Table & Big Stat Cards` (Bảng Đối Chiếu & Thẻ Số Liệu Lớn)
- **Hoạt cảnh**: So sánh 2 đối tượng (Nhân sơ vs Nhân thực; Thực vật vs Động vật; Trước vs Sau áp dụng).
- **Cấu trúc**: Bảng so sánh 3 cột (Tiêu chí - Đối tượng A - Đối tượng B nổi bật) kết hợp các thẻ số liệu lớn `44pt` (`font-size="58.67"`).

#### 🔹 Layout 7: `Status Quo Split Cards` (Thẻ Kép Đối Đầu Thuận Lợi vs Khó Khăn — Chuẩn SKKN mau1, mau7, mau11)
- **Hoạt cảnh**: Phân tích thực trạng, bối cảnh thực tế trong báo cáo SKKN, thi GVG, hội nghị.
- **Cấu trúc SVG**:
  - Cột trái (`x=40..620`): Khung `🟢 THUẬN LỢI` (nền xanh lá nhạt `#E8F5E9`, viền `#2E7D32`), thanh header xanh in chữ trắng, liệt kê các điểm tựa chuyên môn.
  - Cột phải (`x=660..1240`): Khung `🔴 KHÓ KHĂN` (nền đỏ nhạt `#FDEDEC`, viền `#C0392B`), thanh header đỏ gạch in chữ trắng, liệt kê các trở ngại cần tháo gỡ.

#### 🔹 Layout 8: `Interactive Quiz & Game Show Chamber` (Đấu Trường 4 Đáp Án Tương Tác — Chuẩn Ai là triệu phú, Ong non học việc)
- **Hoạt cảnh**: Khởi động, Trò chơi củng cố tiết học, Đố vui có thưởng.
- **Cấu trúc SVG**:
  - Hộp câu hỏi trung tâm (`y=120..240`, `width="1160"`) vát góc lục giác hoặc đám mây hoạt hình.
  - 4 ô đáp án A, B, C, D xếp lưới 2x2 (`y=270` và `y=440`, mỗi ô `width="560"`, `height="140"`).
  - Khai báo nút bấm `id="nut_dap_an_A"`, `id="nut_dap_an_B"`... trong `animations.json` để khi click sẽ đổi sang màu Xanh lá (`#22C55E` - Đúng) hoặc Đỏ (`#EF4444` - Sai).

#### 🔹 Layout 9: `Before-After Survey & Stat Growth` (Khảo Sát Số Liệu & Tăng Trưởng Trước - Sau — Chuẩn mau7, mau22)
- **Hoạt cảnh**: Minh chứng hiệu quả sáng kiến, đánh giá chất lượng học sinh trước và sau khi áp dụng giải pháp.
- **Cấu trúc**:
  - 2 Bảng số liệu song song: Cột 1 "Trước khi áp dụng" (tỉ lệ chưa đạt cao) vs Cột 2 "Sau khi áp dụng" (tỉ lệ Tốt/Xuất sắc tăng vọt).
  - Dưới chân bảng là 2 Thẻ phần trăm lớn `44pt` màu xanh ngọc: `▲ +35.2% Mức độ tích cực` và `▼ -28.4% Học sinh yếu kém`.

#### 🔹 Layout 10: `Hall of Fame & Honor Card` (Vinh Danh Cá Nhân / Gia Đình Văn Hóa / SKKN — Chuẩn P.Cửa Nam, PPT Vinh danh TQT)
- **Hoạt cảnh**: Lễ tuyên dương khen thưởng, vinh danh sáng kiến kinh nghiệm, hội nghị người tốt việc tốt.
- **Cấu trúc**:
  - Cột trái (`x=60..480`): Khung ảnh chân dung bo viền mạ vàng kép (`stroke="#D4AF37"` `stroke-width="4"`), phía dưới là dải tên và chức vụ/đơn vị.
  - Cột phải (`x=520..1220`): Khung danh hiệu tuyên dương lớn màu vàng gold, bên dưới là 3 khối thẻ mạ viền vàng tóm tắt 3 thành tích xuất sắc nhất.

#### 🔹 Layout 11: `KPI Metric Quad-Cards` (4 Thẻ Chỉ Tiêu Số Liệu Lớn — Chuẩn BC Thực hiện nhiệm vụ, mau28)
- **Hoạt cảnh**: Báo cáo tổng kết 6 tháng / năm học, phương hướng nhiệm vụ trọng tâm, chỉ tiêu thi đua.
- **Cấu trúc**: Lưới 4 thẻ số liệu (`width="585"`, `height="250"`). Mỗi thẻ hiển thị con số ấn tượng cỡ `44pt` (`font-size="58.67"`), nhãn chỉ tiêu 18pt đậm nét và thanh tiến độ hoàn thành % ở đáy thẻ.

#### 🔹 Layout 12: `Agenda Multi-Block Grid` (Mục Lục & Đề Cương 4 Khối Đa Năng — Chuẩn mau4, mau8, mau16)
- **Hoạt cảnh**: Trang Cấu trúc báo cáo, Đề cương bài học, Lộ trình nghiên cứu.
- **Cấu trúc**: 4 khối thẻ độc lập có huy hiệu tròn đánh số `01`, `02`, `03`, `04` phối màu đồng bộ với Style chủ đề, kèm icon gợi mở và 2 dòng tóm lược từng phần.

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

### Bước kỹ thuật 5.5: Quy chuẩn Hiển thị Công thức Khoa học & Toán học (Chuẩn Native OMML & Sư phạm lớp học)

Khi giáo viên soạn slide cho các môn có công thức (**Toán, Vật Lí, Hóa Học, KHTN, Sinh học**), công thức phải đạt 3 tiêu chuẩn: **Đẹp chuẩn mực như SGK**, **Cỡ chữ to rõ không mỏi mắt (≥ 22–32pt)** và **Chỉnh sửa được trực tiếp 100% trong PowerPoint**.

Trợ lý áp dụng hệ thống phân cấp công nghệ công thức như sau (ưu tiên số 1 cho Native OMML):

---

#### 🌟 CÔNG NGHỆ SỐ 1: NATIVE OMML FORMULA (CHỈNH SỬA TRỰC TIẾP 100% TRONG POWERPOINT — KHUYÊN DÙNG HÀNG ĐẦU)

Hệ thống tích hợp bộ biên dịch LaTeX sang **Office Math (OMML)** nguyên bản của Microsoft PowerPoint. Khi mở file PPTX, công thức hiển thị dưới dạng đối tượng toán học vector chuẩn mực (`m:oMath`), dùng font chuyên dụng `Cambria Math` kết hợp `Times New Roman`.

**Ưu điểm tuyệt đối cho giáo viên:**
1. **Chỉnh sửa trực tiếp 100%**: Giáo viên mở slide trong PowerPoint, click đúp chuột vào công thức là sửa được số, đổi dấu, thay đổi biểu thức bằng thanh công cụ *Equation Tools* (không cần cài thêm MathType hay phần mềm phụ trợ).
2. **Sắc nét vĩnh viễn (Vector thuần túy)**: Phóng to trên màn hình máy chiếu phòng học hay hội trường lớn không bao giờ bị vỡ hạt, mờ nhòe như ảnh chụp/ảnh PNG.
3. **Chuẩn mực ký hiệu Toán GDPT 2018**: Thể hiện hoàn hảo phân số gạch ngang $\frac{A}{B}$, căn bậc hai $\sqrt{x}$, căn bậc $n$, hệ phương trình có dấu ngoặc nhọn $\begin{cases}...\end{cases}$, số mũ lũy thừa, chỉ số dưới, tích phân, giới hạn $\lim$, ma trận, v.v.

##### Cách viết trong SVG (2 Dạng chuẩn):

**Dạng A — Công thức nội dòng (Inline Formula):**
- Đặt thuộc tính `data-pptx-inline-formula="[Mã_LaTeX]"` trên thẻ `<tspan>` lá (không lồng thẻ con, không chứa tọa độ x/y riêng, không chứa `$` bao quanh).
- Cỡ chữ khuyến nghị: **22pt – 24pt** (để phân số hoặc số mũ trong dòng không bị bé).

```xml
<text x="80" y="320" font-size="24" fill="#1B3A6B" font-family="Times New Roman, serif">
  ▸ Nghiệm phương trình: <tspan data-pptx-inline-formula="x = \frac{-b \pm \sqrt{\Delta}}{2a}">x = (-b ± √Δ)/(2a)</tspan> (với Δ > 0)
</text>
```

**Dạng B — Khối công thức độc lập (Block Formula):**
- Áp dụng cho: Công thức trọng tâm, hệ phương trình, bài toán phân số nhiều tầng, công thức đóng khung chốt kiến thức.
- Sử dụng group `<g id="..." data-pptx-replace-with="formula">` kèm một thẻ con `<metadata type="application/json">` khai báo: `latex`, `display: "block"`, `font_size` (từ 28 đến 36pt), `color`, `align: "center"`.
- Đi kèm thẻ `<text>` preview tượng trưng bên dưới để hiển thị khi xem trực tiếp file SVG.

```xml
<g id="ct_phuong_trinh_bac_hai" data-pptx-replace-with="formula"
   data-pptx-x="200" data-pptx-y="320"
   data-pptx-width="880" data-pptx-height="130"
   data-pptx-bounds="200 320 880 130">
  <metadata type="application/json"><![CDATA[
    {"latex":"x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}",
     "display":"block","font_size":32,"color":"#1B3A6B","align":"center"}
  ]]></metadata>
  <!-- Preview trực quan trong lúc xem bản SVG -->
  <text x="640" y="390" text-anchor="middle" font-size="28" fill="#1B3A6B" font-family="Times New Roman, serif">
    x = (-b ± √(b² - 4ac)) / (2a)
  </text>
</g>
```

**Mẫu khối hệ phương trình bậc nhất hai ẩn:**
```xml
<g id="ct_he_phuong_trinh" data-pptx-replace-with="formula"
   data-pptx-x="250" data-pptx-y="300"
   data-pptx-width="780" data-pptx-height="140"
   data-pptx-bounds="250 300 780 140">
  <metadata type="application/json"><![CDATA[
    {"latex":"\\begin{cases} 2x + 3y = 7 \\\\ 4x - y = 5 \\end{cases}",
     "display":"block","font_size":30,"color":"#854D0E","align":"center"}
  ]]></metadata>
  <text x="640" y="375" text-anchor="middle" font-size="26" fill="#854D0E" font-family="Times New Roman, serif">
    { 2x + 3y = 7 ; 4x - y = 5 }
  </text>
</g>
```

---

#### Cấp độ 2 — Công thức đơn giản (Inline Unicode): ✅ Nhanh gọn, không cần cấu hình
Dùng cho các công thức hóa học đơn giản, ký hiệu vật lý một dòng trong văn bản thông thường:
- Chỉ số dưới hóa học: `H₂SO₄`, `CO₂`, `NaHCO₃`, `Ca(OH)₂`
- Số mũ vật lý: `v₀`, `s = v₀t + ½at²`, `E = mc²`
- Ký hiệu toán học thông dụng: `→`, `⇌`, `±`, `≤`, `≥`, `≈`, `≠`, `∈`, `∉`, `⊂`, `∪`, `∩`, `⋮`, `∤`
- Ký hiệu Hy Lạp: `Δ`, `α`, `β`, `λ`, `ω`, `μ`, `π`, `θ`, `φ`, `Ω`

---

#### Cấp độ 3 — Công thức vẽ đồ họa SVG (Interactive / Step-by-step Math): ✅ Dành cho bài tập tương tác
Khi thiết kế slide bài giảng có hoạt động học sinh điền số, hiệu ứng từng bước xuất hiện đáp án hoặc các hộp màu sắc phân biệt tử số và mẫu số:
- Dùng các thẻ `<rect>`, `<line>`, `<text>` bo góc với màu sắc tương phản.
- Gán animation click từng bước để hiện tử số trước, gạch phân số, rồi đến mẫu số hoặc kết quả.

---

#### Cấp độ 4 — Công thức phức tạp đặc thù (TikZ / Matplotlib 300 DPI): ⭐ Cho hình vẽ thí nghiệm & Đồ thị
Khi bài học cần kèm theo **sơ đồ cấu trúc hóa hữu cơ (vòng Benzen, mạch nhánh)**, **đồ thị hàm số có tiệm cận xiên / bảng biến thiên**, hoặc **sơ đồ mạch điện KHTN**:
- Sử dụng công cụ vẽ Matplotlib hoặc TikZ Engine để xuất hình ảnh kỹ thuật sắc nét 300 DPI.
- Nhúng vào slide qua thẻ `<image href="...">`.

---

#### 📊 Bảng quyết định chọn công nghệ công thức trên slide:

| Dạng công thức / Môn học | Ví dụ điển hình | Công nghệ ưu tiên | Đặc điểm hiển thị |
| :--- | :--- | :---: | :--- |
| **Công thức đại số, phân số, căn thức** | $\frac{x-1}{x+2} = 3$, $x = \frac{-b \pm \sqrt{\Delta}}{2a}$ | ⭐ **Native OMML** | Chỉnh sửa trực tiếp 100%, nét vector siêu đẹp |
| **Hệ phương trình, phương trình chứa ẩn ở mẫu** | $\begin{cases} ax+by=c \\ a'x+b'y=c' \end{cases}$ | ⭐ **Native OMML (Block)** | Căn lề chuẩn mực, ngoặc nhọn lớn chuẩn SGK |
| **Ký hiệu hóa học, công thức vật lý 1 dòng** | $H_2SO_4 + 2NaOH$, $F = ma$, $P = UI$ | **Inline Unicode** | Gõ trực tiếp trong text, nhẹ nhàng, tương thích cao |
| **Bài tập điền từ/số vào phân số** | Điền tử số/mẫu số có ô màu vàng | **Đồ họa SVG** | Có animation click hiện từng số, trực quan sinh động |
| **Đồ thị hàm số, bảng biến thiên, mạch điện** | Bảng biến thiên Toán 12, Sơ đồ mạch điện | **TikZ / Matplotlib** | 300 DPI chính xác tuyệt đối từng tọa độ |

---

### Bước kỹ thuật 6: Kiểm định & Xuất File PowerPoint (.pptx) Chuẩn Mực Sư Phạm

Trợ lý kiểm tra môi trường hiện tại và thực hiện xuất file PPTX theo 1 trong 2 cơ chế:

#### Cơ chế 1 — Môi trường Studio Đầy đủ (Khi có thư mục `skills/ppt-master`):
1. **Kiểm tra chất lượng SVG**:
   ```bash
   python3 skills/ppt-master/scripts/svg_quality_checker.py <project_path> --canonical-authoring --stage final --json
   ```
2. **Xuất PowerPoint Native (tự động đọc `animations.json` & OMML)**:
   ```bash
   python3 skills/ppt-master/scripts/svg_to_pptx.py <project_path>
   ```
3. **Vá font Times New Roman**:
   ```bash
   python3 skills/ppt-master/scripts/patch_fonts.py <đường_dẫn_file.pptx>
   ```
4. **Kiểm tra hiệu ứng sư phạm**:
   ```bash
   python3 tools/vi/kiem_hieu_ung.py <duong_dan_file.pptx> --muc vua
   ```

#### Cơ chế 2 — Môi trường Độc lập trên máy Giáo viên (Khi không có `skills/ppt-master`):
Trợ lý AI **tự động viết script Python sử dụng thư viện `python-pptx`** (đã được cài đặt sẵn qua `cai_dat_tu_dong.bat`) để tạo trực tiếp file `.pptx` bài giảng với đầy đủ các tiêu chuẩn sư phạm vàng:
- Tỉ lệ màn hình 16:9 (`slide_width = Inches(13.333)`, `slide_height = Inches(7.5)`).
- Font chữ toàn bài chuẩn 100% `Times New Roman`.
- Cỡ chữ to rõ: Tiêu đề 22pt, Đề mục 20pt, Thân bài/Câu hỏi 18pt, Ghi chú 14pt.
- Bố cục 3 bước trực quan: Khung Kênh hình (ảnh SGK/thực tế), Khung Câu hỏi thảo luận phát vấn, Khung Nổi bật Em cần ghi nhớ.
- Tự động ghi lời giảng chi tiết của giáo viên vào phần **Notes** (Ghi chú) của từng slide để hỗ trợ giảng dạy hoặc đọc lồng tiếng.

5. **Đặt tên thân thiện & Bàn giao**:
   - Đặt tên file: `[Mon][Khoi]_[TenBai]_ChuanSuPham.pptx` (Ví dụ: `Toan6_Bai13_UCLN_BCNN_ChuanSuPham.pptx`).
   - Cung cấp link mở file trực tiếp cho giáo viên bằng cú pháp: `[Tên_File.pptx](file:///đường/dẫn/tuyệt/đối/file.pptx)`.

---

### Bước kỹ thuật 7: Xuất Video Bài Giảng E-learning MP4 từ PowerPoint (Tự động hoặc Thủ công)

Khi giáo viên có nhu cầu làm video bài giảng E-learning trình chiếu, gửi học sinh ôn bài hoặc làm video tư liệu:

#### 1. Cơ chế 1 — Trợ lý AI thực hiện trọn gói trong khung chat (Khuyên dùng nhất):
Khi giáo viên yêu cầu trong khung chat: *"Em viết lời bình và xuất video bài giảng [5 / 10 / 15 phút], lồng tiếng giọng [Cô Hoài My / Thầy Nam Minh] giúp tôi nhé!"*:
- **Bước A (Căn chỉnh thời lượng lời bình chuẩn xác)**:
  + Video 5 phút (~6–8 slide): Viết ~500–600 từ (ngắn gọn, cô đọng).
  + Video 10 phút (~8–12 slide): Viết ~1.000–1.300 từ (giảng giải cặn kẽ từng bước, dẫn dắt câu hỏi, ví dụ).
  + Video 15 phút (~12–16 slide): Viết ~1.500–1.800 từ (chuyên sâu, giải bài tập chi tiết).
- **Bước B (Nạp lời bình vào Notes)**:
  Chạy lệnh: `python "<ĐƯỜNG_DẪN_SKILL>/scripts/them_loi_binh_pptx.py" "<file.pptx>" --inject-json "<file_notes.json>"`
- **Bước C (Lồng tiếng AI phát thanh viên)**:
  Chạy lệnh: `python "<ĐƯỜNG_DẪN_SKILL>/scripts/long_tieng_pptx.py" "<file_CoLoiBinh.pptx>" --voice "1"` (hoặc `"2"`) $\to$ Xuất ra `[TenBai]_DaLongTieng.pptx`.
- **Bước D (Render Video MP4 Full HD)**:
  Chạy lệnh: `python "<ĐƯỜNG_DẪN_SKILL>/scripts/xuat_video_pptx.py" "<file_DaLongTieng.pptx>"`
- **Bước E (Bàn giao cho giáo viên)**:
  Gửi link mở file video trực tiếp: `[Tên_Video_Bài_Giảng.mp4](file:///đường/dẫn/tuyệt/đối/video.mp4)`.

#### 2. Cơ chế 2 — Giáo viên tự chạy 1-Click bằng file công cụ trên máy:
1. Lồng tiếng AI: Kéo thả file `.pptx` vào **`LONG_TIENG_AI.bat`** $\to$ Chọn giọng Cô Hoài My hoặc Thầy Nam Minh.
2. Xuất video MP4: Kéo thả file `_DaLongTieng.pptx` vào **`XUAT_VIDEO_TU_PPTX.bat`** $\to$ PowerPoint tự động render video Full HD 1080p.

#### 3. Cơ chế 3 — Giáo viên tự thu âm giọng thật & bật Camera ở góc (Chuẩn thi E-learning cấp Huyện/Tỉnh):
1. Mở file `.pptx` bằng Microsoft PowerPoint $\to$ Vào menu **Slide Show** $\to$ Bấm **Record**.
2. Bật Camera máy tính $\to$ Lời bình AI đã viết sẽ hiện trên đỉnh màn hình để đọc theo như máy nhắc chữ.
3. Giảng xong bấm **Stop** $\to$ Vào **File $\to$ Export $\to$ Create a Video** $\to$ Bấm **Create Video**.

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

---

## IX. CẨM NANG BỎ TÚI DÀNH CHO GIÁO VIÊN: 5 CÁCH SỬ DỤNG "HAY & TIỆN NHẤT" MÀ KHÔNG CẦN GIỎI CÔNG NGHỆ

Rất nhiều thầy cô giáo băn khoăn: *"Tôi không rành về tin học, không biết viết câu lệnh (prompt) phức tạp, vậy làm sao để dùng hệ thống này cho hay và hiệu quả?"*

Dưới đây là triết lý **"3 Không — 3 Dễ"** và **5 công thức 1 dòng** giúp bất kỳ giáo viên nào cũng có thể tạo ra những bài giảng xuất sắc chỉ trong vài phút:

### 1. Triết lý "3 Không — 3 Dễ"
* ❌ **Không cần học câu lệnh phức tạp** $\to$ ✅ **Cứ nói tiếng Việt tự nhiên** như đang trao đổi với một giáo viên thực tập/đồng nghiệp tổ chuyên môn giỏi việc.
* ❌ **Không cần gõ lại nội dung bài học** $\to$ ✅ **Thấy gì gửi nấy**: Kéo thả file Word giáo án cũ, file PDF SGK, hoặc lấy điện thoại chụp ngay trang sách rồi gửi vào ô chat.
* ❌ **Không sợ làm hỏng hay đè bài** $\to$ ✅ **Xem duyệt kịch bản trước**: Hệ thống luôn đưa bảng tóm tắt từng slide để thầy cô xem lướt và góp ý trước khi xuất file.

---

### 2. Bộ câu lệnh "Thần chú 1 dòng" giáo viên dùng hàng ngày:

| Tình huống thực tế trên lớp | Câu lệnh mẫu ngắn gọn giáo viên chỉ cần gửi | Kết quả nhận được |
| :--- | :--- | :--- |
| **Soạn bài giảng tiết mới** | *"Soạn bài giảng cho bài này từ file giáo án tôi gửi, làm theo tiến trình 3 bước, chữ to rõ nhé."* | Slide 16:9 chuẩn mực, lọc sạch mục tiêu rườm rà, có ảnh minh họa & khung ghi nhớ. |
| **Làm sơ đồ tư duy ôn tập** | *"Tạo cho tôi 1 slide sơ đồ tư duy dạng tỏa tròn tổng kết bài [Tên bài], có mẹo nhớ nhanh."* | Infographic Radial Mindmap đối xứng, màu sắc đẹp mắt, hiệu ứng bung tỏa từ tâm. |
| **Soạn bài toán có công thức** | *"Tạo slide hướng dẫn giải bài toán trong ảnh này, dùng công thức OMML to rõ để học sinh dễ chép."* | Slide lời giải từng bước, công thức phân số/căn thức chuẩn Native OMML, click đúp sửa được ngay. |
| **Làm trò chơi / Bài tập điền từ** | *"Làm slide bài tập điền từ vào chỗ trống, các từ khuyết bấm vào sẽ chạy lên vị trí đúng."* | Slide bài tập tương tác chia 2 cột/khung, học sinh lên bảng bấm hoặc GV click chuột đáp án nhảy lên. |
| **Làm video mở đầu tiết học** | *"Lên kịch bản và prompt video khởi động 60s dẫn dắt vào bài học này cho học sinh lớp 6."* | Kịch bản sư phạm hấp dẫn, gợi mở vấn đề thực tế, sẵn sàng đưa vào Veo 3 dựng video. |

---

### 3. Quy trình 3 bước nhàn nhã cho giáo viên:
1. **Bước 1 — Gửi tài liệu & Nói mong muốn**: Thả file giáo án Word hoặc ảnh chụp SGK vào, kèm 1 câu mong muốn (ví dụ: *"lớp 6, học sinh trung bình, cần nhiều ví dụ thực tế"*).
2. **Bước 2 — Duyệt lướt kịch bản (1 phút)**: Xem qua bảng phân chia từng slide. Thầy cô chỉ cần gõ: *"Đồng ý, làm đi"* hoặc *"Thêm cho tôi 1 bài tập nữa ở slide 4"*.
3. **Bước 3 — Nhận file PowerPoint tải về**: Mở file `.pptx` lên trình chiếu F5 ngay trên lớp, hoặc nhấp đúp vào bất kỳ dòng chữ/công thức nào để chỉnh sửa theo thói quen giảng dạy riêng của mình.

---

### 4. Tại sao công thức OMML là "cứu tinh" cho giáo viên Toán – KHTN:
* **Không phụ thuộc MathType**: Máy tính ở trường không cài MathType vẫn mở ra bình thường, không bao giờ bị lỗi ô vuông, dấu hỏi chấm `?` hay mất công thức.
* **Chỉnh sửa click đúp**: Nhấp đúp chuột vào công thức là sửa số liệu ngay trên thanh công cụ *Equation* quen thuộc của Microsoft PowerPoint.
* **Nét chữ sắc sảo trên máy chiếu**: Công thức là vector toán học nguyên bản, học sinh ngồi dãy bàn cuối cùng nhìn lên bảng vẫn thấy rõ từng nét gạch ngang phân số, dấu căn và số mũ lũy thừa.
