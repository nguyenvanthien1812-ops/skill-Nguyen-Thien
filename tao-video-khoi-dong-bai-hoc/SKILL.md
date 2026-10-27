---
name: tao-video-khoi-dong-bai-hoc
description: >-
  Tạo kịch bản và prompt Veo 3 cho video khởi động bài học (warm-up video) dài 60–80 giây,
  đồng nhất nhân vật thầy/cô giáo trẻ trung xuyên suốt tất cả các clip.
  Kích hoạt khi giáo viên nói: "tôi muốn tạo kịch bản video mở đầu bài học", "tôi muốn làm video", "tôi muốn viết kịch bản video", "tạo video bài học",
  "làm video khởi động", "viết prompt veo 3", "tạo kịch bản video", "làm video mở đầu bài", "tạo video mở đầu bài học", "tạo prompt video",
  "viết kịch bản cho video", "làm video cho bài học", "tôi cần video khởi động", "lên kịch bản video", "kịch bản video mở đầu".
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

## ⚡ PHẢN HỒI KHI GIÁO VIÊN NÓI: "TÔI MUỐN TẠO KỊCH BẢN VIDEO MỞ ĐẦU BÀI HỌC..."

Khi giáo viên gửi câu lệnh mở đầu như *"tôi muốn tạo kịch bản video mở đầu bài học"*, *"tôi muốn làm video"*, *"tôi muốn viết kịch bản video..."* (mà chưa gửi thông tin bài học cụ thể), AI **PHẢI** ngay lập tức phản hồi mẫu hướng dẫn thân thiện và cung cấp form mẫu kèm câu lệnh sẵn để giáo viên điền:

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

## 📋 TIÊU CHUẨN XUẤT PROMPT: ĐỊNH DẠNG "ALL-IN-ONE SINGLE CODE BLOCK" (BẮT BUỘC)

> [!IMPORTANT]
> **QUY TẮC VÀNG VỀ TRẢI NGHIỆM NGƯỜI DÙNG CHO GIÁO VIÊN:**
> Tuyệt đối **KHÔNG tách rời** lời thoại tiếng Việt, đặc điểm nhân vật, hay bối cảnh ra ngoài các ô code khiến giáo viên phải copy - paste chắp vá nhiều lần.
> Mọi clip xuất ra cho giáo viên **BẮT BUỘC** phải được đóng gói thành **ĐÚNG 1 Ô CODE DUY NHẤT CHO MỖI CLIP (Single Code Block per Clip)**. Giáo viên chỉ cần click 1 lần nút "Copy" trên góc ô code là nạp thẳng vào AI (Veo 3, Kling AI, Runway Gen-4, Sora...) mà không cần chỉnh sửa!

### 📐 Công thức cấu trúc 1 Prompt hoàn chỉnh cho mỗi clip:
```text
[CHARACTER CONSISTENCY SEED]. Setting: [Bối cảnh phòng lab/lớp học tự nhiên]. Action: [Thao tác nhân vật & đạo cụ trực quan, an toàn chính sách]. Camera & Lighting: [Góc máy, chuyển động mượt, ánh sáng điện ảnh, 4K, 16:9, 24fps]. Spoken dialogue in clear [tone] Vietnamese: "[Lời thoại tiếng Việt sư phạm dưới 30 từ, đọc thong thả trong 8.5-9s]". Visual constraints: No on-screen text, no letters, no words, clean minimalist visuals, no subtitles.
```

### 📦 2 Định dạng xuất dữ liệu chuẩn khi hoàn thành kịch bản:
Khi kết thúc Bước 3, AI luôn cung cấp cho giáo viên 2 lựa chọn tiện lợi:
1. **BẢN 1: MASTER PROMPT TOÀN DIỆN (All-in-One Master Storyboard):** Gộp toàn bộ kịch bản từ nhân vật, bối cảnh, 6–8 phân cảnh và lời thoại vào đúng 1 khung code duy nhất (dành cho giáo viên muốn copy 1 lần để lưu trữ hoặc dùng cho các AI hỗ trợ multi-scene prompt).
2. **BẢN 2: BỘ PROMPT TỪNG CLIP (Clip-by-Clip Single Code Blocks):** Mỗi clip là 1 ô code hoàn chỉnh độc lập theo công thức chuẩn ở trên, kèm theo ô Negative Prompt ngắn gọn để giáo viên copy - paste render từng clip 10 giây.

---

## 🌟 VÍ DỤ THỰC CHIẾN MẪU (BENCHMARK CASE STUDY)
*Chủ đề: Sinh học / KHTN 6 — Bài 4: Sử dụng kính hiển vi quang học (6 clip x 10s = 60s, Thầy giáo ~35 tuổi)*

### Clip 1 (00:00 – 00:10): Chiếc lá xanh & Câu hỏi mở đầu
```text
A charismatic Vietnamese male teacher in his mid-30s, neat styled short black hair, clean-shaven refined face, wearing modern titanium wire-frame eyeglasses, dressed in a sharp slate-blue button-up shirt with sleeves neatly rolled to elbows, charcoal tailored trousers, leather watch strap, warm confident smile, inspiring educator demeanor. Setting: A bright modern biology science laboratory with soft morning sunlight streaming onto a clean wooden lab table. Action: The teacher stands by the desk, gently holding a fresh vibrant green leaf on his open palm, presenting it towards the camera with welcoming curiosity. Camera & Lighting: Medium shot, slow gentle push-in, shallow depth of field, cinematic natural lighting, photorealistic 4K, 16:9 aspect ratio, 24fps. Spoken dialogue in clear warm Vietnamese: "Chào các em! Chiếc lá xanh quen thuộc này ẩn chứa điều gì bên trong? Chúng ta thấy được gân lá, nhưng liệu có thấy được các tế bào sống?". Visual constraints: No on-screen text, no letters, no words, clean minimalist visuals, no subtitles.
```

### Clip 2 (00:10 – 00:20): Giới hạn của chiếc kính lúp
```text
A charismatic Vietnamese male teacher in his mid-30s, neat styled short black hair, clean-shaven refined face, wearing modern titanium wire-frame eyeglasses, dressed in a sharp slate-blue button-up shirt with sleeves neatly rolled to elbows, leather watch strap. Setting: Close-up on the polished wooden lab table in the bright biology laboratory. Action: His gentle hands hold an elegant round handheld magnifying glass over the fresh green leaf. Through the magnifying glass lens, the delicate network of leaf veins is optically magnified with crystal clarity, but the microscopic plant cells remain invisible to the naked eye. Camera & Lighting: Smooth macro tracking pan, soft studio lighting, photorealistic 4K, shallow depth of field, 16:9 aspect ratio, 24fps. Spoken voiceover in thoughtful engaging Vietnamese: "Một chiếc kính lúp giúp ta thấy rõ từng đường gân lá tinh xảo. Nhưng để nhìn sâu hơn vào từng tế bào nhỏ bé, mắt thường đành bất lực!". Visual constraints: No on-screen text, no letters, no words, clean background, no labels.
```

### Clip 3 (00:20 – 00:30): Xuất hiện "Cỗ máy quang học kỳ diệu"
```text
A charismatic Vietnamese male teacher in his mid-30s, neat styled short black hair, clean-shaven refined face, wearing modern titanium wire-frame eyeglasses, dressed in a sharp slate-blue button-up shirt with sleeves neatly rolled to elbows, charcoal tailored trousers, leather watch strap, warm enthusiastic smile. Setting: Bright biology laboratory next to a sleek modern optical compound microscope with polished metal and black matte finishes. Action: The teacher stands proudly beside the microscope, gesturing with an open welcoming palm toward the optical instrument, introducing it with excitement. Camera & Lighting: Smooth cinematic pan from the teacher's inspiring smile to the gleaming microscope, soft rim lighting, photorealistic 4K, 16:9 aspect ratio, 24fps. Spoken dialogue in inspiring Vietnamese: "Và đây chính là chiếc chìa khóa mở ra thế giới vi mô: Kính hiển vi quang học, cỗ máy có thể phóng đại hình ảnh lên tới hàng nghìn lần!". Visual constraints: No on-screen text, no labels, no alphabet, no subtitles.
```

### Clip 4 (00:30 – 00:40): Đặt tiêu bản kính lên bàn kính
```text
A charismatic Vietnamese male teacher in his mid-30s, wearing a slate-blue button-up shirt with sleeves rolled to elbows and a brown leather watch strap. Setting: Modern biology lab, extreme focus on the optical microscope. Action: Close-up of his gentle refined hands carefully placing a transparent glass specimen slide onto the matte black mechanical stage of the optical microscope. His fingers smoothly slide the polished metal stage clips to secure the slide in place with precision. Camera & Lighting: Slow smooth dolly shot, warm laboratory lighting, photorealistic 4K, shallow depth of field, 16:9 aspect ratio, 24fps. Spoken voiceover in clear instructional Vietnamese: "Chỉ với một lát cắt thực vật cực mỏng đặt lên bàn kính, kẹp giữ nhẹ nhàng, chúng ta đã sẵn sàng cho chuyến thám hiểm kỳ thú.". Visual constraints: No on-screen text, no written labels on glass slide, clean transparent glass, no words.
```

### Clip 5 (00:40 – 00:50): Xoay đĩa vật kính & Luồng sáng bừng tỉnh
```text
A charismatic Vietnamese male teacher in his mid-30s, wearing a slate-blue shirt with sleeves rolled to elbows. Setting: Modern biology laboratory. Action: Angled cinematic close-up of the optical microscope. The teacher's hand gently rotates the circular revolving nosepiece, smoothly clicking an objective lens into the vertical optical axis. Simultaneously, the circular LED sub-stage light illuminates, projecting a brilliant, pure cone of glowing optical light directly upward through the condenser and the glass slide. Camera & Lighting: Atmospheric cinematic lighting, golden and soft blue optical reflections, shallow depth of field, photorealistic 4K, 16:9 aspect ratio, 24fps. Spoken voiceover in captivating Vietnamese: "Xoay nhẹ đĩa vật kính, luồng sáng xuyên qua tâm tiêu bản. Từng chi tiết cơ học và quang học phối hợp nhịp nhàng như một cỗ máy viễn tưởng!". Visual constraints: No on-screen text, no numbers on lens, no letters, no subtitles.
```

### Clip 6 (00:50 – 01:00): Chạm vào thế giới tế bào & Lời mời gọi
```text
A charismatic Vietnamese male teacher in his mid-30s, neat styled short black hair, clean-shaven refined face, wearing modern wire-frame eyeglasses, dressed in a sharp slate-blue button-up shirt with sleeves rolled to elbows. Setting: Modern biology laboratory. Action: He leans in gently to look through the microscope eyepiece with focused delight and wonder. The camera smoothly zooms through the optical lens into an artistic cinematic visualization of glowing emerald plant cells forming an intricate luminous living mosaic, then cuts back to the teacher looking up at the camera with an engaging smile and inviting hand gesture. Camera & Lighting: Cinematic climax, smooth push-in and pull-back, photorealistic 4K, shallow depth of field, 16:9 aspect ratio, 24fps. Spoken dialogue in enthusiastic welcoming Vietnamese: "Cả một thế giới tế bào sống động hiện ra trước mắt! Làm sao để các em tự tay điều khiển cỗ máy kỳ diệu này? Chúng ta cùng khám phá ngay sau đây!". Visual constraints: No on-screen text, no letters, no words, clean background.
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
