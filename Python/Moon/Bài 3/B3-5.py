#bài tập thực hành (ôn tập về biến và kiểu dữ liệu)
#bài toán về nhập 2 số ra tổng 2 số
x = int(input("a =  "))
y = int(input("b =  "))
print("Tổng a + b = ", x + y)

#bài toán về hoán đổi giá trị của 2 biến
x = int(input("x =  "))
y = int(input("y =  "))
tmp = x 
x = y
y = tmp
print(f"x = {x}, y = {y}")

#bài toán về tính độ C sang độ F
c = float(input("Nhập độ C: "))
f = 1.8 * c + 32
print(f"{c} *c bằng {f} *f")

#bài toán về tính diện tích hình chữ nhật
D = float(input("Nhập chiều dài hình chữ nhật: "))
R = float(input("Nhập chiều rộng hình chữ nhật: "))
S = D * R
print(f"Diện tích hình chữ nhật là: {S} cm²")

#bài toán về thay vào phương trình bậc ba
x = float(input("Nhập x: "))
f = 2*x**3 + 3*x**2 + 5**x - 1
print(f"F({x}) = {round(f,2)}")

#bài toán về số phức
from math import sqrt
z = complex(input("Nhập số phức a: "))
a = z.real
b = z.imag
t = sqrt(a**a + b**b)
print(t)