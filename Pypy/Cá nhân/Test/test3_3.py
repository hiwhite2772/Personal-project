#Tam giác vuông và tam giác cân bằng dấu sao (*)
n = 6
#Tam giác vuông từ bên trái
for i in range(1, n+1):
    print("*"*i)
print()
#Tam giác vuông từ bên phải
for i in range(1, n+1):
    print(" "*(n-i) + "*"*i) 
print()
#Tam giác vuông từ bên trái ngược xuống
for i in range(1, n+1):
    print("*"*(n-i+1))
print()
#Tam giác vuông từ bên phải ngược xuống
for i in range(1, n+1):
    print(" "*(i-1) + "*"*(n-i+1))
print()
#Tam giác cân ở đỉnh trên
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))
print()
#Tam giác cân ở đỉnh ngược xuống
for i in range(1, n+1):
    print(" "*(i-1) + "*"*(2*(n-i+1)-1))
print()
#Tam giác rỗng từ trái lên
n = int(input("Nhập số s = "))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")
#Tự nhập k = đổi dấu hình
n = int(input("Nhập số: "))
k = input("Nhập dấu: ")
for i in range(1, n + 1):
    print(k * i)
