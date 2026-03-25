diem10 = float(input("Nhập điểm thang 10 của bạn: "))
diem4 = round(diem10 * 0.4, 2)
print("Sau quy đổi thành điểm thang 4:", diem4)
if diem4 >= 3.6:
    print("Điểm chữ: (A+)")
elif diem4 >= 3.4:
    print("Điểm chữ: (A)")
elif diem4 >= 3.2:
    print("Điểm chữ: (B)")
elif diem4 >= 2.8:
    print("Điểm chữ: (B)")
elif diem4 >= 2.6:
    print("Điểm chữ: (C+)")
elif diem4 >= 2.2:
    print("Điểm chữ: (C)")
elif diem4 >= 2.0:
    print("Điểm chữ: (D)")
elif diem4 >= 0.0:
    print("Điểm chữ: (F)")
else:
    print("Điểm không hợp lệ.")