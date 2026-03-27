#Thực hành:

#Câu 1
a = float(input("Nhập số a: "))
if a > 0:
    s = a**2
    print(f"Diện tích hình vuông = ", round(s,3))
else:
    print("Lỗi. a phải là số dương")

#Câu 2
y = int(input("Nhập số năm: "))
if y < 1582:
    print("Không tính theo lịch Gregory")
elif (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(y, "là năm nhuận")
else:
    print(y, "không phải là năm nhuận")

#Câu 3
gpa4 = float(input("Nhập GPA thang điểm 4: "))
if gpa4 < 0 or gpa4 > 4:
    print("không thoả mãn điều kiện")
else:
    gpa10 = gpa4 * 2.5
    print ("GPA thang điểm 10 =", round(gpa10,2))

#Câu 4
a, b = map(float, input("a, b = ") . split(","))
if a == 0 and b == 0:
    print("Phương trình vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm")
else:
    x = -b/a
    print(f"Phương trình có 1 nghiệm x = {x}")

#Câu 5
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0:
    print("không hợp lệ")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép x1 = x2 = {x}")
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt x1 = {x1}, x2 = {x2}")
#Câu 6
h = int(input("Nhập số giờ: "))
m = int(input("Nhập số phút: "))
if (h < 0 or h > 23):
    print("Thời gian giờ không hợp lệ")
elif (m < 0 or m > 59):
    print("Thời gian phút không hợp lệ")
else:
    if (h == 12):
        print(f"{h}:{m} PM")
    elif (h > 12):
        h = h % 12
        print(f"{h}:{m} PM")
    else:
        print(f"{h}:{m} AM")