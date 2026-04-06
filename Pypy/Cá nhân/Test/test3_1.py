#1
n = int(input("Nhập n = "))
for i in range(1, n+1):
    print("*"*i)
#2
n = int(input("Nhập n = "))
k = input("Nhập ký tự k = ")
for i in range(1, n+1):
    print(k*i)
#3
n = int(input("Nhập n = "))
for i in range(n, 0, -1): #cach 1
    print("*"*i)
for i in range(1, n+1): #cach 2
    print("*"*(n-i+1))
#4
n = int(input("Nhập n = "))
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(2*i-1))
#5
n = int(input("Nhập n = "))
k = input("Nhập ký tự k = ")
for i in range(1,n+1):
    print(" "*(n-i)+k*(2*i-1))
#6
m = int(input("Nhập m = "))
n = int(input("Nhập n = "))
for i in range(m):
    print("*"*n)
#7 - Hình chữ nhật rỗng
m = int(input("Nhập m = ")) 
n = int(input("Nhập n = "))
for i in range(m):
    if i == 0 or i == m-1:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
#8 - Hình chữ X
n = int(input("Nhập n = "))
for i in range(n):
    for j in range(n):
        if j == i or j == n-i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#9 - Tam giác số
n = int(input("Nhập n = "))
for i in range(1, n+1):
    print(str(i)*i)
for i in range(1,n+1):
    print(" "*(n-i)+str(i)*i)
#10
n = int(input("Nhập n = "))
k = input("Nhập ký tự k = ")
for i in range(1, n+1):
    print(k*(n-i+1))
for i in range(1, n+1):
    print(" "*(i-1)+k*(n-i+1))