import turtle
import math

# ==========================================
# BƯỚC 1: Tạo màn hình
# ==========================================
wn = turtle.Screen()
wn.title("Cờ Tổ Quốc Việt Nam")
wn.bgcolor("white")

# Tạo "cây bút" để vẽ
pen = turtle.Turtle()
pen.speed(3)  # Tốc độ vẽ (1=chậm, 10=nhanh, 0=tức thì)


# ==========================================
# BƯỚC 2: Hàm vẽ hình chữ nhật (nền đỏ)
# ==========================================
def draw_rectangle(color, width, height):
    pen.color(color)        # Chọn màu
    pen.begin_fill()        # Bắt đầu tô màu
    for _ in range(2):      # Lặp 2 lần → vẽ 4 cạnh (2 cạnh dài + 2 cạnh ngắn)
        pen.forward(width)  # Vẽ cạnh ngang
        pen.right(90)       # Quay phải 90 độ
        pen.forward(height) # Vẽ cạnh dọc
        pen.right(90)       # Quay phải 90 độ
    pen.end_fill()          # Kết thúc tô màu


# Dịch bút đến góc trên trái, rồi vẽ hình chữ nhật đỏ
pen.penup()             # Nhấc bút lên (không vẽ khi di chuyển)
pen.goto(-150, 100)     # Di chuyển đến tọa độ góc trên trái
pen.pendown()           # Đặt bút xuống (bắt đầu vẽ)
draw_rectangle("red", 300, 200)


# ==========================================
# BƯỚC 3: Hàm vẽ ngôi sao vàng
# ==========================================
def draw_star(x, y, size):
    pen.penup()  # Nhấc bút lên trước khi di chuyển

    # --- Tính 5 ĐỈNH NGOÀI (đỉnh nhọn của sao) ---
    outer = []
    for i in range(5):
        # Bắt đầu từ 90 độ (đỉnh trên cùng), mỗi đỉnh cách nhau 72 độ (360/5)
        angle = math.radians(90 + i * 72)
        px = x + size * math.cos(angle)  # Tọa độ X
        py = y + size * math.sin(angle)  # Tọa độ Y
        outer.append((px, py))

    # --- Tính 5 ĐỈNH TRONG (chỗ lõm vào giữa các cánh sao) ---
    inner = []
    inner_size = size * 0.382  # Tỉ lệ vàng: điểm trong nhỏ hơn điểm ngoài ~2.6 lần
    for i in range(5):
        # Lệch thêm 36 độ so với đỉnh ngoài (nằm đúng giữa 2 cánh sao)
        angle = math.radians(90 + 36 + i * 72)
        px = x + inner_size * math.cos(angle)
        py = y + inner_size * math.sin(angle)
        inner.append((px, py))

    # --- Xen kẽ điểm ngoài và điểm trong ---
    # Kết quả: [ngoài0, trong0, ngoài1, trong1, ngoài2, trong2, ...]
    # → Tạo ra hình sao 10 đỉnh liên tục, không bị hở giữa
    star_points = []
    for i in range(5):
        star_points.append(outer[i])  # Đỉnh nhọn
        star_points.append(inner[i])  # Đỉnh lõm

    # --- Vẽ ngôi sao ---
    pen.goto(star_points[0])  # Di chuyển đến điểm đầu tiên
    pen.pendown()             # Đặt bút xuống, bắt đầu vẽ
    pen.color("yellow")       # Màu vàng
    pen.begin_fill()          # Bắt đầu tô màu vàng

    for pt in star_points[1:]:  # Đi qua tất cả các điểm còn lại
        pen.goto(pt)

    pen.goto(star_points[0])  # Quay về điểm đầu để khép kín hình

    pen.end_fill()  # Tô kín toàn bộ ngôi sao (kể cả phần giữa) ✅

    
# ==========================================
# BƯỚC 4: Chạy chương trình
# ==========================================
draw_star(0, 0, 50)  # Vẽ sao tại tâm (0,0), kích thước 50

pen.hideturtle()  # Ẩn con rùa sau khi vẽ xong
wn.mainloop()     # Giữ cửa sổ mở, chờ người dùng đóng


"""
```Tóm tắt luồng chạy:```

Tạo màn hình
    ↓
Vẽ nền đỏ (hình chữ nhật)
    ↓
Tính 5 đỉnh ngoài (nhọn)
    ↓
Tính 5 đỉnh trong (lõm)
    ↓
Xen kẽ 10 điểm → vẽ & tô kín
    ↓
Ẩn bút, giữ cửa sổ
"""
