#Vòng lặp for - else

#VD
my_list = [1,13,55,2,3,77,54,12,10]
x = int(input("x = "))
for i in my_list:
    if (x == i):
        print(f"Có {x} trong danh sách")
        break
else:
    print(f"không có {x} trong danh sách")