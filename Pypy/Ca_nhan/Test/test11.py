#For - While
#1
n = int(input("Nhập số nguyên dương: "))
tong = 0
for i in range(1, n+1):
    if n % 2 == 0 and n % 4 != 0:
        tong += i
print("Tổng các số chẵn:", tong)

#2
n = int(input("Nhập số nguyên dương: "))
dem = 0
while n > 0:
    dem += 1
    n //= 10
print("Đếm chữ số:", dem)

#3
n = int(input("Nhập số nguyên dương: "))
tich = 1
while n > 0:
    tich *= n % 10
    n //= 10
print("Tích các số:", tich)

#4
n = int(input("Nhập số nguyên dương: "))
for i in range(n):
    so = 2 * i + 1
    if i % 2 == 1:
        so = -so
    print(so, end=" ")

#5
n = int(input("Nhập số nguyên dương: "))
tam = n
dao = 0
while n > 0:
    dao = dao * 10 + n % 10
    n//=10
if dao == tam:
    print("Đối xứng!")
else:
    print("Không đối xứng!")

#6
while True:
    n = int(input("Nhập n = "))
    if n % 7 == 0:
        break

#7
tong = 0
while tong < 100:
    n = int(input("Nhập số n = "))
    tong += n
print("Tổng:", tong)

#8
dem = 0
while True:
    x = int(input("Nhập số n = "))
    if x == 0:
        break
    if x < 0:
        dem += 1
print("Đếm số nguyên âm là", dem)

#9
tong = 0
dem = 0
while True:
    x = int(input("Nhập số n = "))
    if x <= 0:
        break
    tong += x
    dem += 1
if dem > 0:
    print("Trung bình cộng:", round(tong/dem, 2))
else:
    print("Không hợp lệ")

#10
dem = 0
while True:
    x = int(input("Nhập số d = "))
    dem += 1
    if x == 9:
        break
print(f"Bạn đã đoán sau {dem} lần")

#11
n = int(input("Nhập số nguyên n: "))
while n <= 0:
    n = int(input("Nhập lại n (n>0): "))
tong = 0
number = n
while number > 0:
    digit = number % 10
    tong += digit
    number //= 10
print(f"Tổng các số của {n} là: {tong}")
