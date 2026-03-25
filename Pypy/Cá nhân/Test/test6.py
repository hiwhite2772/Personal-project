#1
n = int(input("n = "))
if n > 0:
    print("Số dương")
elif n < 0:
    print("Số âm")
else:
    print("Bằng không")
#2
a = int(input("a = "))
if a % 2 == 0 and a != 10:
    print("Thoả mãn")
else:
    print("Không thoả mãn")
#3
n = int(input("n = "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
#4
n = int(input("n = "))
while n >= 0:
    n = int(input("n = "))
#5
n = int(input("n = "))
tong = 0
for i in range(1, n+1):
    if i % 3 != 0:
        tong += i
print("Tổng =", tong)
#6
s = input("Nhập chuỗi: ")
if not s.isdigit():
    print("Đây không phải là chuỗi số")
else:
    print("Đây là chuỗi số")
#7 - Kiểm tra chẵn lẻ bằng hàm def
def kiemtra(n):     
    if n % 2 == 0:
        return f"{n} là số chẵn"
    else:
        return f"{n} là số lẻ"
num = int(input("Nhập số nguyên: "))
print(kiemtra(num))