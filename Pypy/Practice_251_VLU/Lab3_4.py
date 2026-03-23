import math

a = float(input("Nhập a = "))
b = float(input("Nhập b = "))
c = float(input("Nhập c = "))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Tam giác đều")
    elif a==b or a==c or b==c:
        print("Tam giác cân")
    elif abs(a**2 - (b**2 + c**2)) < 1e-10 or abs(b**2 - (a**2 + c**2)) < 1e-10 or abs(c**2 - (a**2 + b**2)) < 1e-10:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Ba cạnh không tạo thành tam giác")