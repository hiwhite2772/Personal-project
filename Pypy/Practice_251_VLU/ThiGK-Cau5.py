#Code
n = int(input("Nhap n = "))
print("Day Fibonacci:", end=" ")
a, b = 0, 1
for __ in range(n):
    print(a, end=" ")
    c = a + b
    a = b 
    b = c


#Mã Giả:
#B1: Bắt đầu
#B2: Nhập số n 
#B3: in ra Day Fibonacci
#B4: a, b = 0, 1
#B5: for i in range(n) 
#B6: print(a, end=" ")
#    c = a + b
#    a = b 
#    b = c
#B7: Kết thúc