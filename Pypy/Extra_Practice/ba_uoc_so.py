n = int(input())
count = 0  #Gán số đếm

#Xét từng số từ 1 đến n đều
for x in range(1, abs(n) + 1):
    #Gán số ước
    so_uoc = 0
    
    #Tìm các ước của số đó
    for i in range(1, x + 1):
        if x % i == 0:
            so_uoc += 1  #Nếu thấy số ước thì tăng lên 1
    
    #Kiểm tra có 3 ước số không
    if so_uoc == 3:
        count += 1

print(count)