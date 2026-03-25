#1
so_dien_nang_tieu_thu = int(input("Nhập số điện năng tiêu thụ (kWh): "))
if 0 < so_dien_nang_tieu_thu < 50:
    tien_dien = so_dien_nang_tieu_thu * 1800
elif 51 < so_dien_nang_tieu_thu < 100:
    tien_dien = so_dien_nang_tieu_thu * 2000
elif 101 < so_dien_nang_tieu_thu < 200:
    tien_dien = so_dien_nang_tieu_thu * 2500
elif so_dien_nang_tieu_thu >= 200:
    tien_dien = so_dien_nang_tieu_thu * 3000
else:
    print("Số điện năng tiêu thụ không hợp lệ!")
    exit()
tien_dinh_dang = f"{tien_dien:,}".replace(",", ".")
print("Tiền điện phải trả:", tien_dinh_dang, "VND")

#2
don_gia = int(input("Nhập số giá: "))
so_luong = int(input("Nhập số lượng: "))
gia_tri_thanh_tien = don_gia*so_luong
if gia_tri_thanh_tien <= 500000:
    tong = gia_tri_thanh_tien
elif gia_tri_thanh_tien <= 1000000:
    tong = gia_tri_thanh_tien*0.95
elif gia_tri_thanh_tien <= 2000000:
    tong = gia_tri_thanh_tien*0.9
elif gia_tri_thanh_tien > 2000000:
    tong = gia_tri_thanh_tien*0.85
else:
    print("Không hợp lệ")
print(f"Sau khi đã giảm, số tiền phải trả: {tong} VND")

#3
score = float(input("Nhập điểm trung bình: "))
if score < 5:
    print("Học sinh Yếu!")
elif 5 < score < 6.5:
    print("Học sinh Trung bình!")
elif 6.5 < score < 8:
    print("Học sinh Khá!")
elif 8 < score < 9:
    print("Học sinh Giỏi!")
elif 9 < score < 10:
    print("Học sinh Xuất sắc!")
else:
    print("Không hợp lệ!")

#4
tong_tien = int(input("Nhập tổng số tiền: "))
print("Bạn có thẻ thành viên hay không?")
print("Vui lòng ấn số 1 - Có; 0 - Không")
the = int(input("Nhập nhấn số: "))  # 1 hoặc 0
if the == 1:
    if tong_tien >= 1000000:
        tong = tong_tien * 0.8
    else:
        tong = tong_tien * 0.9
else:
    if tong_tien >= 1000000:
        tong = tong_tien * 0.9
    else:
        tong = tong_tien
print(f"Sau khi đã giảm thì phải trả tiền: {tong} VND")