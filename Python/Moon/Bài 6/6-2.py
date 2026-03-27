#Vòng lặp while

#VD1
t = 0
i = 1
while (i <= 50):
    if ( i % 2 != 0):
        t = t + i
    i = i + 1
print("tổng t = ", t)

#VD2
s = None
while (True):
    s = input("Nhập chuỗi: ")
    if(s != "exit"):
        print("Chuỗi viết hoa:", s.upper())
    else:
        break