---
name: tao-video-khoi-dong-bai-hoc
description: >-
  Tạo kịch bản và prompt Veo 3 cho video khởi động bài học (warm-up video) dài 60–80 giây,
  đồng nhất nhân vật thầy/cô giáo trẻ trung xuyên suốt tất cả các clip.
  Kích hoạt khi giáo viên nói: "tôi muốn làm video", "tôi muốn viết kịch bản video", "tạo video bài học",
  "làm video khởi động", "viết prompt veo 3", "tạo kịch bản video", "làm video mở đầu bài", "tạo prompt video",
  "viết kịch bản cho video", "làm video cho bài học", "tôi cần video khởi động", "lên kịch bản video".
  Quy trình gồm 3 bước: (1) Phản hồi form hướng dẫn & gợi ý 3–5 ý tưởng kịch bản → (2) Giáo viên chọn ý tưởng →
  (3) Viết CHARACTER SEED + toàn bộ prompt Veo 3 từng clip (áp dụng mẹo không chữ & an toàn chính sách).
---

# 🎬 SKILL: Tạo Video Khởi Động Bài Học với Veo 3

## MÔ TẢ TỔNG QUAN

Skill này hỗ trợ giáo viên tạo video khởi động bài học (warm-up video) sinh động,
chuyên nghiệp để chiếu ở đầu tiết học nhằm tạo hứng thú và kích thích tò mò cho học sinh.
Video dài **60–80 giây**, chia thành các **clip 10 giây** (6–8 clip),
sử dụng **Veo 3** (hoặc Kling AI, Runway Gen-4) để tạo từng clip,
sau đó ghép lại bằng **CapCut**.

---

## ⚡ PHẢN HỒI KHI GIÁO VIÊN NÓI: "TÔI MUỐN VIẾT KỊCH BẢN VIDEO..."

Khi giáo viên gửi câu lệnh mở đầu như *"tôi muốn làm video"*, *"tôi muốn viết kịch bản video..."* (mà chưa gửi thông tin bài học cụ thể), AI **PHẢI** ngay lập tức phản hồi mẫu hướng dẫn thân thiện và cung cấp form mẫu kèm câu lệnh sẵn để giáo viên điền:

```markdown
Chào Thầy/Cô! Rất vui được đồng hành cùng Thầy/Cô tạo video khởi động bài học bằng Veo 3.

Để video đạt hiệu quả sư phạm cao nhất, hình ảnh đồng nhất và đúng chuẩn, Thầy/Cô hãy gửi ảnh chụp SGK / file PDF hoặc sao chép mẫu dưới đây, điền thông tin và gửi lại cho tôi nhé:

---
📝 **MẪU ĐIỀN THÔNG TIN BÀI HỌC:**
- Môn học: [Toán / Lý / Hóa / Sinh / Công nghệ / KHTN / ...]
- Lớp: [6 / 7 / 8 / 9 / 10 / 11 / 12]
- Tên bài: [...]
- Nội dung trọng tâm: [Khái niệm cốt lõi cần học sinh tò mò]
- Tình huống mở đầu trong SGK: [Mô tả ngắn hoặc gửi ảnh chụp SGK]
- Nhân vật trong video: [Thầy giáo (khoảng 28-35 tuổi) / Cô giáo (khoảng 25-28 tuổi)]
- Thời lượng mong muốn: [60s (6 clip) / 70s (7 clip) / 80s (8 clip)]
---

👉 Ngay khi nhận được thông tin, tôi sẽ gợi ý 3–5 Ý TƯỞNG KỊCH BẢN độc đáo để Thầy/Cô lựa chọn trước khi viết trọn bộ Prompt Veo 3!
```

---

## 🗺️ QUY TRÌNH CHUẨN 3 BƯỚC

```
[BƯỚC 1] Giáo viên gửi thông tin bài học (hoặc gửi ảnh/PDF SGK)
              ↓
[BƯỚC 2] AI gợi ý 3–5 Ý TƯỞNG kịch bản + Bảng so sánh + Câu lệnh bước tiếp theo
              ↓
[BƯỚC 3] Giáo viên chọn ý tưởng → AI viết CHARACTER SEED + PROMPT VEO 3 TỪNG CLIP
```

---

## 💡 TẬP HỢP CÁC MẸO VÀNG KHI VIẾT PROMPT VEO 3 (PROMPT TIPS)

### 1️⃣ Mẹo Loại Bỏ Hoàn Toàn Chữ Trong Video (No Text / Pure Visuals)
- **Vấn đề:** Các mô hình AI video (Veo 3, Kling, Runway) khi tạo chữ viết tiếng Việt hoặc ký hiệu toán học thường bị lỗi: méo mó, biến dạng chữ, tạo chữ vô nghĩa hoặc sai chính tả.
- **Giải pháp:** 
  - Trong prompt Veo 3, **tuyệt đối không yêu cầu tạo chữ, bảng viết chữ hay công thức toán dài**.
  - Thay thế chữ bằng **hiệu ứng thị giác thuần túy**: đốm sáng, dải sáng laser, mô hình 3D, thanh ray, hình học trừu tượng phát sáng.
  - Thêm cụm từ vào prompt: `No text, no letters, no words, clean minimalist visuals`.
  - Thêm vào Negative Prompt: `text, words, letters, typography, alphabet, subtitles, watermark, labels, blackboard writing`.
  - **Khâu hậu kỳ:** Thầy/Cô dùng **CapCut** chèn chữ tiêu đề bài học, tên điểm, tên định lý tiếng Việt đè lên. Video sẽ sắc nét 100% chuẩn đồ họa truyền hình!

### 2️⃣ Mẹo Đồng Nhất Nhân Vật (Character Consistency)
- Luôn tạo một đoạn **CHARACTER SEED cố định** mô tả chi tiết: độ tuổi, kiểu tóc, trang phục, màu áo, phụ kiện (kính, đồng hồ, hoa tai), phong thái.
- **Bắt buộc dán CHARACTER SEED vào đầu MỌI prompt clip** (Clip 1 đến Clip 8).
- **Kỹ thuật Reference Image:** Sau khi tạo xong Clip 1, chụp màn hình cận cảnh gương mặt và trang phục của nhân vật → Upload ảnh đó vào ô **Reference Image / Subject Reference** của Veo 3 khi render Clip 2 đến Clip 8.

### 3️⃣ Mẹo Vượt Bộ Lọc An Toàn Chính Sách (Safety Policy Bypass)
- Veo 3 có bộ lọc kiểm duyệt cực kỳ gắt gao. Hãy tuân thủ bảng chuyển đổi từ ngữ:

| ❌ CÁC TỪ DỄ BỊ CHẶN | ✅ TỪ THAY THẾ AN TOÀN TUYỆT ĐỐI |
|---|---|
| cut, scissors, knife, blade | places, arranges, slides, positions |
| folds violently, tears paper | gently displays, demonstrates, holds |
| grabs, snatches, strikes | holds gently, presents with open palm |
| laser weapon, shoot, gun | educational optical pointer pen, glowing light ray |
| arbitrary sharp corners | smooth triangular tiles, geometric models |
| complex hand twists | pointing gently, welcoming hand gestures |

### 4️⃣ Mẹo Sư Phạm: Không Spoil Đáp Án Trước (Keep The Mystery)
- Video khởi động là chiếc móc câu (Hook) tạo sự tò mò.
- **Tuyệt đối không tiết lộ công thức, định lý hay đáp số** (ví dụ: không nói trước `tổng bằng 180°`, `chỉ có duy nhất 1 đường thẳng`...).
- Chỉ dừng lại ở việc phát hiện ra **hiện tượng kỳ lạ** và đặt ra **câu hỏi lớn mở ra bài học**.

### 5️⃣ Mẹo Chuyển Động Camera & Ánh Sáng Điện Ảnh
- Dùng từ khóa quay phim chuyên nghiệp: `medium shot`, `close-up tracking shot`, `smooth slow push-in`, `cinematic lighting`, `soft rim light`, `shallow depth of field`.
- Tỉ lệ khung hình (Aspect Ratio): `16:9` (chuẩn bài giảng / máy chiếu).
- Thời lượng mỗi clip: `10 seconds`.

---

## 🎭 BỘ CHARACTER SEED MẪU CHUẨN

### Nhân vật THẦY GIÁO (~35 tuổi - Chững chạc, truyền cảm hứng):
```
A charismatic Vietnamese male teacher in his mid-30s, 
neat styled short black hair, clean-shaven refined face, 
wearing modern titanium wire-frame eyeglasses, 
dressed in a sharp slate-blue button-up shirt with sleeves neatly rolled to elbows, 
charcoal tailored trousers, leather watch strap, 
warm confident smile, inspiring, intellectually sharp and approachable educator demeanor. 
Photorealistic, 4K, cinematic lighting, sharp focus.
```

### Nhân vật THẦY GIÁO TRẺ (~28 tuổi - Năng động, hiện đại):
```
A young Vietnamese male teacher in his late 20s, 
neat short modern black hair, clean-shaven, 
wearing a light pastel blue button-up dress shirt tucked into 
charcoal grey tailored trousers, stylish silver-rimmed glasses, 
warm energetic smile, approachable, smart and passionate educator demeanor. 
Photorealistic, 4K, cinematic lighting, sharp focus.
```

### Nhân vật CÔ GIÁO TRẺ (~25 tuổi - Tươi tắn, duyên dáng):
```
A young Vietnamese female teacher in her mid-20s, 
with long straight black hair worn down, 
wearing a light pastel pink button-up blouse tucked into 
white wide-leg trousers, small gold stud earrings, 
natural makeup with soft pink lips, warm bright smile, 
slim figure, approachable and energetic personality. 
Photorealistic, 4K, cinematic lighting, sharp focus.
```

---

## 📋 CẤU TRÚC PROMPT TỪNG CLIP CHUẨN KHI XUẤT CHO GIÁO VIÊN

```
[CHARACTER SEED — Dán nguyên văn]

[Mô tả cảnh quay bằng tiếng Anh]:
- Bối cảnh: Phòng học / Xưởng sáng tạo / Bàn thí nghiệm (không có chữ, không có khẩu hiệu).
- Đạo cụ: Mô hình, tia sáng, gạch màu, vật thể trực quan.
- Hành động: Nhẹ nhàng, tự nhiên, an toàn chính sách.
- Chuyển động camera & ánh sáng: 4K, cinematic, smooth movement.
- Ghi chú: No text, no words, clean visuals.

Lời thoại tiếng Việt (Thầy/Cô giáo):
"..." (Dưới 38 từ, đọc vừa vặn trong 8.5–9 giây)
```

---

## 🎬 HƯỚNG DẪN HẬU KỲ TRÊN CAPCUT DÀNH CHO GIÁO VIÊN

```
Bước 1: Tải các clip 10s từ Veo 3 về máy tính hoặc điện thoại.
Bước 2: Mở CapCut → Import toàn bộ các clip theo thứ tự Clip 1 → Clip cuối.
Bước 3: Tạo giọng đọc tiếng Việt bằng FPT.AI Speech (speech.fpt.ai) hoặc ElevenLabs.
Bước 4: Kéo các file âm thanh vào khớp với từng clip.
Bước 5: Thêm Text (Tiêu đề bài học, tên định lý, nhãn điểm...) bằng tính năng Văn bản của CapCut.
Bước 6: Thêm nhạc nền nhẹ nhàng (nhạc acoustic hoặc instrumental truyền cảm hứng).
Bước 7: Xuất video độ phân giải 1080p, tỉ lệ 16:9.
```
