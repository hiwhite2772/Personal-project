#1 - Bảng cửu nhân từ 0 đến 30 - Dùng for
n = int(input("Nhập số: "))
for i in range(31):
    print(f"{n} x {i} = {n * i}")
    
#2 - Bảng cửu nhân từ số lần ý muốn - dùng for
n = int(input("Nhập số nhân: "))
l = int(input("Nhập số lần: "))
for i in range(l+1):
    #Độ rộng tối thiểu (kiểu các dòng thẳng hàng)
    print(f"{n:2}  x {i:2} = {n*i:3}")
    
#3 - Dùng while
n = int(input("n = "))
l = int(input("l = "))

i = 0  #Từ số 0
while i <= l:
    print(f"{n} x {i} = {n*i}")
    i += 1
