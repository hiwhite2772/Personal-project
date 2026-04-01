# Nhập điểm tổng kết học phần
diem = float(input("Nhập điểm tổng kết học phần: "))

# Xác định điểm chữ
if diem >= 9.0 and diem <= 10:
    diem_chu = "A"
elif diem >= 8.5:
    diem_chu = "B+"
elif diem >= 8.0:
    diem_chu = "B"
elif diem >= 7.0:
    diem_chu = "C+"
elif diem >= 6.5:
    diem_chu = "C"
elif diem >= 5.5:
    diem_chu = "D+"
elif diem >= 5.0:
    diem_chu = "D"
else:
    diem_chu = "F"

print(f"Điểm chữ tương ứng: {diem_chu}")

