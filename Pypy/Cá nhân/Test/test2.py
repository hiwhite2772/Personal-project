import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
p = (a + b + c) / 2.0
cv = 2 * p
dt = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Nửa chu vi p = {p}")
print(f"Chu vi = {cv}")
print(f"Diện tích = {dt}")


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
    print("Ba cạnh tạo thành một tam giác.")
else:
    print("Ba cạnh KHÔNG tạo thành một tam giác.")