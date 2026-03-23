#1
def is_positive(n):
    if n <= 0:
        return False
    return True
t = int(input("Nhap so nguyen: "))
print("Ket qua:", is_positive(t))
#2
def count_even_digits(n):
    if n < 10:
        if n % 2 == 0:
            return 1
        else:
            return 0
    last_digit = n % 10
    if last_digit % 2 == 0:
        return 1 + count_even_digits(n // 10)
    else:
        return count_even_digits(n // 10)
def count_even_digits_2(n):
    if n < 10:
        return 1 if n % 2 == 0 else 0
    return (1 if (n % 10) % 2 == 0 else 0) + count_even_digits_2(n // 10)
i = int(input("Nhap so nguyen: "))
print("Dem chu so chan:", count_even_digits(i))
print("Dem chu so chan:", count_even_digits_2(i))
#3
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)
i = int(input("Nhap so: "))
print("Tong cac chu so:",sum_digits(i))
#4
def sum_squares(n):
    if n == 1:
        return 1
    return n**2 + sum_squares(n-1)
i = int(input("Nhap so: "))
print("Tong binh phuong:", sum_squares(i))
#5
def sum_reciprocal(n):
    if n == 0:
        return 0
    return 1/n + sum_reciprocal(n-1)
print(sum_reciprocal(2))
#Lỗi chỗ sum_reciprocal(n) trả về vượt qua lớn. Nên sửa thành sum_reciprocal(n-1) vì n-1 giảm mạnh á