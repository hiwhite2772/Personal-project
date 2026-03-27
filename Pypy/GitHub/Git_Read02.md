
# ❓ 1. Xoá file trên GitHub → máy có tự xoá không?

👉 **KHÔNG tự động**

Nếu bạn xoá file trên GitHub (web), thì:

* GitHub: ✅ file bị xoá
* Máy bạn: ❌ vẫn còn file cũ

---

## ✅ Muốn đồng bộ về máy

Bạn phải chạy:

```bash
git pull
```

👉 Lúc này:

* Git sẽ kéo thay đổi từ GitHub về
* File bị xoá trên web → sẽ bị xoá trên máy

---

# ❓ 2. Xoá file trên máy → GitHub có tự xoá không?

👉 **Cũng KHÔNG tự động**

Bạn phải làm đủ 3 bước:

```bash
git add .
git commit -m "delete file"
git push
```

👉 Sau đó:

* GitHub mới xoá file đó

---

# ❓ 3. Sửa code trên GitHub → máy có tự cập nhật không?

👉 **KHÔNG tự động luôn**

Bạn phải chạy:

```bash
git pull
```

👉 thì code mới trên GitHub mới về máy

---

# 🧠 Tư duy đúng (cực kỳ quan trọng)

👉 Git **KHÔNG phải Google Drive**

Nó KHÔNG tự sync

---

# 🔑 Quy tắc vàng

| Hành động              | Cần làm    |
| ---------------------- | ---------- |
| Lấy code mới từ GitHub | `git pull` |
| Đẩy code lên GitHub    | `git push` |

---

# 🔥 Ví dụ dễ hiểu

## Trường hợp 1:

Bạn xoá file trên GitHub

👉 máy bạn vẫn còn → chạy:

```bash
git pull
```

---

## Trường hợp 2:

Bạn sửa file trên máy

👉 GitHub chưa có → chạy:

```bash
git add .
git commit -m "update"
git push
```

---

# ⚠️ Cảnh báo quan trọng

👉 Nếu bạn:

* sửa code trên máy
* rồi lại `git pull`

💥 Có thể bị **conflict**

---

# 🚀 Thói quen chuẩn (rất nên làm)

Mỗi lần code:

```bash
git pull
# code
git add .
git commit -m "..."
git push
```

---

# 🎯 Tóm lại 1 câu

> 🔑 Git chỉ đồng bộ khi bạn dùng `pull` hoặc `push` — không tự động
