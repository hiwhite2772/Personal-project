#Sắp xếp thứ tự tăng dần
numbers = input("Nhập các số nguyên phải cách nhau:").split()
numbers = [int(num) for num in numbers]
numbers.sort()
print("Danh sách số nguyên đã sắp xếp:", numbers)

#Đảo ngược của dãy số
numbers = [1,2,3,4,5,6]
numbers.reverse()
for number in numbers:
    print(number, end=" ")

#Bản sao, đảo ngược của các dãy số
ds1 = [2,4,6,8,10]
ds2 = ds1.copy()
ds2.reverse()
print("Danh sách các số ban đầu:", ds1)
print("Danh sách các số có đảo ngược:", ds2)

#Đếm số lần xuất hiện của số cần đếm 
so = [1,2,4,2,3,3,1,3,2,2,1,1,4,5,2,1,4,5]
scd = int(input("Nhập số cần đếm (1 đến 5): "))
slxh = so.count(scd)
print("Số lần xuất hiện của", scd, "trong dãy số là:", slxh)

#Mở rộng 1 list
sn = [1, 2, 3]
st = [4.5, 5.25, 6.75]
snmr = sn.copy()
snmr.extend(st)
print("List sau khi mở rộng:", snmr)