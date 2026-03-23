#Code
n = int(input("Nhap so n = "))
print("Cac so nguyen to la:", end=" ")
for i in range(2, n + 1):
    isprime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        print(i, end=" ")


#Mã Giả:
#B1: Bắt đầu
#B2: Nhập số n 
#B3: for i in range(2, n + 1) --> isprime = True
#B4: for j in range(2, i) 
#B5: if i % j == 0 --> isprime = False --> Break
#B6: if isprime
#B7: in ra các số nguyên tố theo số n
#B8: Kết thúc