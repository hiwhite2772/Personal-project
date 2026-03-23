#1
n = int(input("Nhập n(kWh): "))
bill = 0
if n <= 50:
    bill = n * 1678
elif n <= 100:
    bill = 50*1678 + (n-50)*1734
else:
    bill = 50*1678 + 50*1734 + (n-100)*2014
print(f"Số tiền điện phải trả: {bill} VNĐ.")
#2
t = float(input("Tổng tiền thưởng: "))
n = int(input("Số nhân viên: "))
if n <= 0:
    print("Không hợp lệ!")
else:
    moi_ng_nhan = int(t//n)
    so_tien_du = int(t%n)
    print("Mỗi nhân viên nhận được:", moi_ng_nhan, "VNĐ")
    print("Số tiền dư là:", so_tien_du, "VNĐ")
#3
dtb = float(input("Nhập điểm trung bình: "))
if dtb < 5:
    print("Học lực: Yếu")
elif 5 <= dtb < 6.5:
    print("Học lực: Trung bình")
elif 6.5 <= dtb < 8:
    print("Học lực: Khá")
else:
    print("Học lực: Giỏi")
#4
age = int(input("Nhập tuổi: "))
thu_nhap = float(input("Nhập thu nhập hàng tháng (triệu đồng): "))
if age >= 21 and thu_nhap >= 10:
    print("Đủ điều kiện vay vốn")
else:
    print("Không đủ điều kiện vay vốn")
#5
n = int(input("Nhập số nguyên dương n: "))
if n % 2 == 0 and n % 3 == 0:
    print(f"{n} chia hết cho 2 và 3.")
elif n % 2 == 0:
    print(f"{n} chỉ chia hết cho 2.")
elif n % 3 == 0:
    print(f"{n} chỉ chia hết cho 3.")
else:
    print(f"{n} không chia hết cho 2 và 3.")
#6
n = int(input("Nhập số năm: "))
if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print(f"{n} là năm nhuận.")
else:
    print(f"{n} không phải là năm nhuận.")
#7
n = float(input("Nhập số km: "))
bill = 0
if n <= 1:
    bill = n * 15000
elif n <= 5:
    bill = 15000+ (n - 1) * 13000
else:
    bill = 15000 + 4*13000 + (n - 5) * 11000
print(f"Số tiền cước taxi là: {bill} VNĐ.")
#8
lcb = float(input("Nhập lương cơ bản: "))
snc = int(input("Nhập số ngày công: "))
l = 0
if snc >= 26:
    l = lcb * snc * 1.1
else:
    l = lcb * snc
print("Lương tháng là:", round(l, 2), "VNĐ")
#9
a = float(input("a = "))
b = float(input("b = "))
if b == 0:
    print("Không hợp lệ!")
else:
    print("Kết quả a/b =", a/b)
#10
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a <= 0 or b <= 0 or c <= 0:
    print("Không hợp lệ!")
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Ba cạnh tạo thành tam giác vuông.")
elif a == b == c:
    print("Ba cạnh tạo thành tam giác đều.")
elif a== b or b==c or a==c:
    print("Ba cạnh tạo thành tam giác cân.")
else:
    print("Ba cạnh tạo thành tam giác thường.")
