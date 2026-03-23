#1
def count_non_zero_digit(n):
    if n < 10:
        return 0 if n == 0 else 1
    last = n % 10
    if last != 0:
        return 1 + count_non_zero_digit(n // 10)
    else:
        return count_non_zero_digit(n // 10)
i = int(input("Nhap so: "))
print(count_non_zero_digit(i))
#2
def so_lon_nhat(n):
    if n < 10:
        return n
    last = n % 10
    return max(last, so_lon_nhat(n // 10))
i = int(input("Nhap so: "))
print("So lon nhat trong cac chu so la", so_lon_nhat(i))
#3
def tong_day_so_chan(x):
    if x == 0:
        return 0
    if x == 1:
        return 2
    return 2*x + tong_day_so_chan(x-1)
i = int(input("Nhap so: "))
print("Tong day so chan:", tong_day_so_chan(i))
#4
def count_divisible_by_3(n):
    if n == 0:
        return 0
    if n % 3 == 0:
        return 1 + count_divisible_by_3(n - 1)
    else:
        return count_divisible_by_3(n - 1)
d = int(input("Nhap so: "))
print("Dem so chia het cho 3:", count_divisible_by_3(d))
#5
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n//10)
o = int(input("Nhap so: "))
print(count_digits(o))