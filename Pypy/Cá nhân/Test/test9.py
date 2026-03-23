# lấy danh sách số chẵn 
n = int(input("Nhập số lượng phần tử: "))
lst = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    lst.append(x)
    
# Tạo danh sách mới chứa số chẵn
chan = []
for x in lst:
    if x % 2 == 0:
        chan.append(x)
print("Danh sách số chẵn:", chan)


# Đếm chữ hoa, chữ thường và chữ số trong chuỗi
s = input("Nhập chuỗi: ")
chu_hoa = chu_thuong = chu_so = 0
for ch in s:
    if ch.isupper():
        chu_hoa += 1
    elif ch.islower():
        chu_thuong += 1
    elif ch.isdigit():
        chu_so += 1
print("Chữ hoa:", chu_hoa)
print("Chữ thường:", chu_thuong)
print("Chữ số:", chu_so)

#Đếm số lần xuất hiện
lst = list(map(int, input("n = ").split(",")))
x = int(input("m = "))
count = 0
for i in lst:
    if i == x:
        count += 1
print("Danh sách hiện là:", lst)
print(f"Số {x} có xuất hiện trong ds là {count} lần")