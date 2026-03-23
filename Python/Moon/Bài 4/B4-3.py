#Toán tử gán 
a = int(input("Nhập a = "))
b = int(input("Nhập b = "))

#giá trị vế phải gán được vế trái 
x = a
y = b
x = y
print("x1 = ", x)
print("y1 = ", y)

#giá trị vế trái gán được vế phải 
x = a
y = b
y = x
print("x2 = ", x)
print("y2 = ", y)
