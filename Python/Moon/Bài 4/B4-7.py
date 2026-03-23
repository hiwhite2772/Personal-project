#Thực hành
#Câu 1
r = int(input("Nhập bán kính hình tròn: "))
PI = 3.14
c = 2*PI*r
print(f"Chu vi hình tròn là: {c}")

#Câu 2
x = int(input("Nhập số x: "))
print(oct(x))

#Câu 3
x = float(input("Nhập số x: "))
y = 5*x**2 + 3*x + 2
print(f"y = {round(y,2)}")

#Câu 4
x = float(input("Nhập số x: "))
if x >= 1:
    f = 2**x + 3*x + 4
if x < 1:
    f = 3**x +2*x + 1
print("f(x) = ", f)

#Câu 5
x = input("Nhập chuỗi x: ")
print( "a" in x )