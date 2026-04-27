score_10 = float(input("Nhập điểm thang 10 của bạn: "))
score_4 = round(score_10 * 0.4, 2)
print("Sau quy đổi thành điểm thang 4:", score_4)
if score_4 >= 3.6:
    print("Điểm chữ: (A+)")
elif score_4 >= 3.4:
    print("Điểm chữ: (A)")
elif score_4 >= 3.2:
    print("Điểm chữ: (B)")
elif score_4 >= 2.8:
    print("Điểm chữ: (B)")
elif score_4 >= 2.6:
    print("Điểm chữ: (C+)")
elif score_4 >= 2.2:
    print("Điểm chữ: (C)")
elif score_4 >= 2.0:
    print("Điểm chữ: (D)")
elif score_4 >= 0.0:
    print("Điểm chữ: (F)")
else:
    print("Điểm không hợp lệ.")