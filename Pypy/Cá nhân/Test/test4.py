a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print("Giá trị lớn nhất là:", max_val)


lst = list(map(int, input("Nhập các số phải dấu phẩy: ").split(",")))
max_val = lst[0]
for x in lst:
    if x > max_val:
        max_val = x
print("Giá trị lớn nhất là:", max_val)


lst = list(map(int, input("Nhập các số phải dấu phẩy: ").split(",")))
x = int(input("Nhập số: "))
count = 0
for i in lst:
    if i == x:
        count += 1
print(f"Số lần xuất hiện của số {x}: {count}")

