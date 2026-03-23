#Lệnh break và continue

#VD1
t = -1
for i in range(100, 0, -1):
    if(i % 7 == 0 and i % 3 == 0):
        t = i
        break

if(t != 0):
    print("Số cần tìm là:", t)
else:
    print("Không hợp lệ!")

#VD2
for i in range(1, 10):
    if (i % 4 ==0):
        continue
    print(i, end="\t")