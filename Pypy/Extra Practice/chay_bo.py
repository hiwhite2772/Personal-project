# #Công thức đơn giản
t = int(input("Nhập số bộ test: "))
for _ in range(t):
    n = int(input("Nhập số ngày: "))
    print("Sau khi đã chạy số km:", n*(n+1)//2)

#Dệ quy
def tong(n):
    if n == 1:
        return 1
    return n + tong(n-1)
t = int(input("Nhập số bộ test: "))
for _ in range(t):
    n = int(input("Nhập số ngày: "))
    print("Sau khi đã chạy số km:", tong(n))