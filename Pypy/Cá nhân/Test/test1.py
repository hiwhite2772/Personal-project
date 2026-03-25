#1
n = int(input("Nhập số nguyên: "))
if n != 0:
    print("Đây là số khác 0")
else:
    print("Đây là số bằng 0")
#2
password = input("Nhập mật khẩu: ")
if password != "hello123":
    print("Mật khẩu không đúng")
else:
    print("Đăng nhập thành công")
#3
n = int(input("Nhập số nguyên: "))
while n != 0:
    n = int(input("Nhập số nguyên: "))
#4
num = int(input("Nhập số nguyên: "))
if num != 5 and num != 10:
    print("Giá trị hợp lệ")
else:
    print("Giá trị không hợp lệ")
#5
n = int(input("Nhập số nguyên dương: "))
for i in range(1, n+1):
    if n != 3:
        print(i)
#6 - Tính tổng các số từ 1 đến n, trừ 5
n = int(input("Nhập số nguyên: "))
tong = 0                        #Khởi tạo biến tổng 
for i in range(1, n+1):
    if i != 5:
        tong += i
        print(i)
#7
n = input("Nhập chuỗi: ")
if n.strip() != "":
    print("Chuỗi hợp lệ")
else:
    print("Chuỗi không hợp lệ")