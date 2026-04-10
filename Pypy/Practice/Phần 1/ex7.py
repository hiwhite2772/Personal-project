#1
def de_quy(n):
    if n == 1:
        return n
    return n + de_quy(n-1)

def khu_dq(n):
    tong = 0
    for i in range(1, n+1):
        tong += i
    return tong

def main():
    while True:
        try:
            n = int(input("Nhập số nguyên: "))
            if n > 0:
                break
            print("Vui lòng nhập lớn hơn 0.")
        except ValueError:
            print("Vui lòng nhập số nguyên")
    print(f"Đệ quy: {de_quy(n)}")
    print(f"Khử đệ quy: {khu_dq(n)}")
main()

#2
def giai_thua_de_quy(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_de_quy(n-1)

def giai_thua_khu_dq(n):
    if n == 0:
        return 1
    tong = 1
    for i in range(1, n+1):
        tong *= i
    return tong

def main2():
    while True:
        try:
            n = int(input("Nhập số nguyên: "))
            if n >= 0:
                break
            print("Vui lòng nhập lớn hơn hoặc bằng 0.")
        except ValueError:
            print("Vui lòng nhập số nguyên")
    print(f"Đệ quy: {giai_thua_de_quy(n)}")
    print(f"Khử đệ quy: {giai_thua_khu_dq(n)}")
main2()

#3
def dq(n):
    if n == 1:
        return 1/2
    return 1/(2*n) + dq(n-1)
def kdq(n):
    tong = 0
    for i in range(1, n+1):
        tong = tong + 1/(2*i)
    return tong

def main3():
    while True:
        try:
            n = int(input("Nhập số nguyên: "))
            if n > 0:
                break
            print("Vui lòng nhập lớn hơn 0.")
        except ValueError:
            print("Vui lòng nhập số nguyên")
    print(f"Đệ quy: {dq(n)}")
    print(f"Khử đệ quy: {kdq(n)}")
main3()

#4
def binh_phuong_dq(x, n):
    if n == 1:
        return x**2
    return x**(2*n) + binh_phuong_dq(x, n-1)

def binhphuong_kdq(x, n):
    tong = 0
    for i in range(1, n+1):
        tong += x**(2*i)
    return tong

def main4():
    while True:
        try:
            x = int(input("Nhập số nguyên: "))
            if x >= 0:
                break
            print("Vui lòng nhập lớn hơn hoặc bằng 0.")
        except ValueError:
            print("Vui lòng nhập số nguyên")

    while True:
        try:
            n = int(input("Nhập số nguyên: "))
            if n >= 0:
                break
            print("Vui lòng nhập lớn hơn hoặc bằng 0.")
        except ValueError:
            print("Vui lòng nhập số nguyên")
    print(f"Đệ quy: {binh_phuong_dq(x, n)}")
    print(f"Khử đệ quy: {binhphuong_kdq(x, n)}")
main4()

#5
def tichsole_dq(n):
    if n == 0:
        return 1
    digit = n % 10
    if digit % 2 != 0:
        return digit * tichsole_dq(n // 10)
    return tichsole_dq(n // 10)    

def tichsole_kdq(n):
    multi = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            multi *= digit
        n //= 10
    return multi

def main5():
    while True:
        try:
            n = int(input("Nhập số nguyên: "))
            if n > 0:
                break
            print("Vui lòng nhập lớn hơn 0.")
        except ValueError:
            print("Vui lòng nhập số nguyên")
    print(f"Đệ quy: {tichsole_dq(n)}")
    print(f"Khử đệ quy: {tichsole_kdq(n)}")
main5()
