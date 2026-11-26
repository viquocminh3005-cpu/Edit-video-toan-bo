# Chữ nhấn + hiệu ứng động

> **Chủ kênh chốt 2026-10-20:** KHÔNG hiệu ứng lấp lánh — engine đã tắt hạt sáng, vòng sóng lan, tia sáng quét, vệt sáng (`NO_SPARKLE = True`); các mô tả "sóng lan", "hạt sáng" bên dưới không còn hiện. KHÔNG minh họa — nhịp 8–10s chỉ bằng chữ nhấn. KHÔNG chữ xoay/lật 3D — `flip3d`/`swing3d`/`tilt3d` tự đổi sang `reveal` (trừ khi plan `"allow_3d": true`).

Chữ nhấn dùng đúng **mẫu chữ khối** (xem mau-chu-khoi.md). Nhịp: **một chữ nhấn mỗi 8–10s**.

## Chọn câu
- Bám **đúng lúc người nói nói ra cụm đó** (lấy `s` của từ đầu trong `words.json`, trừ 0.1–0.2s). Dài 1.4–2.6s.
- Chọn: kết luận, con số, cảm xúc mạnh, 2 vế đối lập, câu hỏi tu từ. Không chọn câu dẫn.
- 2–6 từ, dòng màu 1–3 từ.

## Kiểu vào (`fx`)
| fx | Diễn biến | SFX tự động | Dùng khi |
|---|---|---|---|
| **`reveal`** (ưu tiên) | mask reveal: từng dòng trồi lên từ sau mép che vô hình, chậm dần (ease-out 0.36s), dòng sau trễ 0.08s, rồi đứng yên | whoosh nhỏ + impact nhẹ | hầu hết câu nhấn — gọn, chuyên nghiệp |
| **`pop`** | nở nhanh 86% → 100% (0.23s), không xoay, không nhòe, không nảy | swish + impact nhẹ | câu ngắn, xen kẽ với reveal |
| `slam` (mặc định) | dòng trắng rơi xuống; dòng màu đập vào từ 165% → 96% → 100% + nhòe→nét; chớp sáng nhẹ, **sóng lan**, **hạt sáng bắn ra**, **zoom punch 7%** | whoosh + impact | câu đinh, kết luận |
| `zoom` | dòng màu phóng từ 30% → 108% → 100%; sóng lan, hạt, zoom punch | riser (trước 0.7s) + impact | con số, cao trào |
| `stagger` | từng từ trượt lên theo nhịp 0.11s | swish + pop mỗi từ | liệt kê, câu có nhịp |
| `wipe` | từng dòng lộ trái→phải | whoosh + impact nhẹ | tên khái niệm, tiêu đề phần |
| `type` | gõ từng ký tự | tick | câu hỏi, suy nghĩ |
| `rise` | nở nhẹ 88% → 100% | whoosh nhỏ | câu nhẹ, nội tâm |
| `flip3d` | **3D** — lật thẻ quanh trục ngang, phối cảnh thật; sóng lan, hạt, zoom punch | swish + impact nhẹ | câu đinh, kết luận, bước ngoặt |
| `swing3d` | **3D** — xoay vào như cánh cửa quanh trục dọc | whoosh + pop | so sánh, chuyển ý, hành động |
| `tilt3d` | **3D** — nghiêng sâu rồi dựng lại, giữ chút chiều sâu khi đứng | whoosh + impact nhẹ | câu hỏi lớn, suy ngẫm, cao trào |

Tùy chọn mỗi chữ nhấn: `"punch": false` (tắt zoom) hoặc số (VD `1.1`), `"flash": false`, `"particles": false`, `"sfx": "none"`.

## Biến thể (`variant`)
| variant | Cỡ tối đa | Nền | fx mặc định |
|---|---|---|---|
| `impact` | 330 | tối 22% | slam |
| `whisper` | 190 | không tối | rise (không zoom punch, whoosh nhỏ) |
| `chapter` | 250 | tối 45% | wipe (dùng `"kicker": "CHƯƠNG 01"` làm dòng trắng) |

## Phối để không nhàm (chủ kênh chốt 2026-10-20)
- Chủ đạo `reveal` + `pop` xen kẽ (~70%), `wipe` / `stagger` điểm xuyết; `slam` chỉ cho 1 câu chốt mạnh nhất; `zoom` cho con số.
- KHÔNG `flip3d` / `swing3d` / `tilt3d` (chữ xoay/lật trông nghiệp dư).
- Không dùng cùng fx 3 lần liên tiếp.
- Zoom punch không quá 1 lần / 8s.
