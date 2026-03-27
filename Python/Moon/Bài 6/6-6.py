#Thực hành:

#câu 1:
n = int(input("n = "))
if n < 1:
    print("không hợp lệ")
else:
    t = 0
    for i in range(1, n+1):
        if (i % 2 == 0):
            t += i
    print(f"{t:,}")

#câu 2:
s = input("Nhập từ khoá: ")
k = len(s)
for i in range(k-1, -1, -1):
    print(s[i], end="")


#câu 3:
n = int(input("Nhập n = "))
x = float(input("Nhập x = "))
if n >= 0:
    t = 0
    for i in range(0, n+1):
        t += x**i
    print(f"f(x) = {t}")

#câu 4:
n = int(input("Nhập n = "))
if n < 0:
    print("Không hợp lệ!")
else:
    t = 1
    for i in range(1, n+1):
        t = t * i
        print(f"{n}! = {t}")

#câu 5:
from math import sqrt
n = int(input("n = "))
if n < 1:
    print("Không hợp lệ")
elif n == 1:
    print("1 không phải là số nguyên tố")
else:
    result = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result = False
            break
    if result:
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")

#câu 6:
from math import sqrt
n = int(input("n = "))
t = 0
for j in range (1, n+1):
    if j == 1:
        continue
    result = True
    for i in range(2, int(sqrt(j))+1):
        if j % i == 0:
            result = False
            break
    if result:
        t += 1
        print(f"có {t} số nguyên tố [1, {n}]")