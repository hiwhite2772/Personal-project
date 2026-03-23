#Số Fibonacci
def so_fibonacci(n):
    if n == 0 or n == 1:
        return n
    return so_fibonacci(n-1)+so_fibonacci(n-2)
x = int(input("Nhập số: "))
print("F(n) =", so_fibonacci(x))

def so_fibonacci(x):
    a = 0
    b = 1
    if x == 0:
        return a
    if x == 1:
        return b
    for i in range(2, n+1, 1):
        c = a + b
        a = b
        b = c
    return b
n = int(input("n = "))
print(so_fibonacci(n))

#Chuyển đổi cơ số - hệ nhị phân
def dec_to_binary_recursion(n1):
    if n1 == 0:
        return "0"
    if n1 == 1:
        return "1"
    return dec_to_binary_recursion(n1//2)+str(n1%2)
def dec_to_binary(n2):
    if n2 == 0:
        return "0"
    result = ""
    while n2 != 0:
        result = str(n2%2)+result
        n2 = n2//2
    return result
def main():
    n1 = int(input("Nhập số cho đệ quy = "))
    n2 = int(input("Nhập số cho vòng lặp = "))
    print(dec_to_binary_recursion(n1))
    print(dec_to_binary(n2))
main()

#Đếm số chữ số của số N
def dem_chu_so(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + dem_chu_so(n//10)
print(dem_chu_so(0))

#Tổng chữ số của số N
def tong_chu_so(n):
    if n < 10:
        return n
    return n%10 + tong_chu_so(n//10)
print(tong_chu_so(666))