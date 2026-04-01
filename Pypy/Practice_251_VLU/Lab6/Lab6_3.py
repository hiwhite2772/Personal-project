import math

def expr1(n):
    S = 0
    for i in range(n+1):
        S += 1 / math.factorial(i)
    return S

def expr2(x, n):
    S = 0
    for i in range(n+1):
        numerator = x**(2*i + 1)
        denominator = math.factorial(2*i + 1)
        term = ((-1)**i) * (numerator / denominator)
        S += term
    return S

def expr3(x, n):
    S = 0
    for i in range(n+1):
        numerator = x**(2*i)
        denominator = math.factorial(2*i)
        term = ((-1)**i) * (numerator / denominator)
        S += term
    return S

n = int(input("Nhập n (số số hạng): "))
x = float(input("Nhập x (tham số): "))

print(f"Giá trị biểu thức 1 với n = {n} là: {expr1(n)}")
print(f"Giá trị biểu thức 2 với x = {x}, n = {n} là: {expr2(x, n)}")
print(f"Giá trị biểu thức 3 với x = {x}, n = {n} là: {expr3(x, n)}")
