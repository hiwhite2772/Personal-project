
# 🚀 Cách gửi nhiều file cùng lúc lên GitHub

👉 **Chỉ cần 1 lệnh:**

```bash
git add .
```

✔ Dấu `.` nghĩa là:

> “lấy **TẤT CẢ file và thư mục** trong project”

---

# 🧠 Quy trình đầy đủ (chuẩn)

```bash
git add .
git commit -m "update project"
git push origin main
```

---

# 🔥 Hiểu đơn giản

| Lệnh         | Ý nghĩa          |
| ------------ | ---------------- |
| `git add .`  | gom toàn bộ file |
| `git commit` | lưu lại          |
| `git push`   | gửi lên GitHub   |

---

# ⚡ Ví dụ thực tế

Bạn có:

* 10 file Python
* 3 folder

👉 Chỉ cần:

```bash
git add .
```

💥 Git sẽ tự động:

* lấy hết 13 thứ đó
* không cần add từng file

---

# ⚠️ Lưu ý nhỏ (quan trọng)

👉 Trước khi commit, luôn check:

```bash
git status
```

→ xem có file nào chưa được add không

---

# 🎯 1 câu chốt (cực dễ nhớ)

> 🔑 **Muốn gửi nhiều file → dùng `git add .`**
