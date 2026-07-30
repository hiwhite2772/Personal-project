# Dạng bài: Xử lý các chữ số

# 1 - Tổng các chữ số
n = 12345
tong = 0
while n > 0:
    digit = n % 10
    tong += digit
    n //= 10
print("Tổng các chữ số:", tong)

# 2 - Tích các chữ số
n = 12345
tich = 1
while n > 0:
    digit = n % 10
    tich *= digit
    n //= 10
print("Tích các chữ số:", tich)

# 3 - Tổng các chữ số chẵn (lẻ)
n = 123456
chan = le = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        chan += digit
    if digit % 2 != 0:
        le += digit
    n //= 10
print("Tổng các chữ số chẵn:", chan)
print("Tổng các chữ số lẻ:", le)

# 4 - Tích các chữ số chẵn (lẻ)
n = 123456
chan = le = 1
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        chan *= digit
    if digit % 2 != 0:
        le *= digit
    n //= 10
print("Tích các chữ số chẵn:", chan)
print("Tích các chữ số lẻ:", le)


# 5 - Tổng bình phương của các chữ số
def de_quy(n):
    if n == 0:
        return 0
    return (n % 10) ** 2 + de_quy(n // 10)


def khu_de_quy(n):
    tong = 0
    while n > 0:
        digit = n % 10
        tong += (digit) ** 2
        n //= 10
    return tong


n = int(input("Nhap n: "))
print(f"Đệ quy: {de_quy(n)}")
print(f"Khử đệ quy: {khu_de_quy(n)}")


# 6 - Tích bình phương của các chữ số
def de_quy(n):
    if n == 1:
        return 1
    return (n % 10) ** 2 * de_quy(n // 10)


def khu_de_quy(n):
    tich = 1
    while n > 0:
        digit = n % 10
        tich *= (digit) ** 2
        n //= 10
    return tich


n = int(input("Nhap n: "))
print(f"Đệ quy: {de_quy(n)}")
print(f"Khử đệ quy: {khu_de_quy(n)}")


# 7 - Kiểm tra số đối xứng - Palindrome:
def palindrome_i(n):
    t = n
    s = 0
    while n > 0:
        digit = n % 10
        s = s * 10 + digit
        n //= 10
    return t == s


def palindrome_s(n):
    return n == n[::-1]


n = int(input("Nhap so: "))
print("Số đối xứng bằng số:", palindrome_i(n))  # True
print("Số đối xứng bằng chuỗi:", palindrome_s(str(n)))  # True
