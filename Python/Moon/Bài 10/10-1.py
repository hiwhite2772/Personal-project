#1 Tính tổng 2 số nguyên a và b
def tinh_tong(a, b):
    return (a + b)
print(tinh_tong(-1, 5))

#2
def chu_vi_hcn(chieu_dai, chieu_rong):
    if chieu_dai <= 0 or chieu_rong <= 0:
        return
    chu_vi = (chieu_dai + chieu_rong)*2
    return chu_vi
print(chu_vi_hcn(3, 10))

#3
x = -4
y = 1.55
print("|x| =", abs(x))
print("|y| =", abs(y))

#4
my_list = [1, 2, 4, 10, -2, -5, 10, 11, 20]
print("Giá trị lớn nhất:", max(my_list))
print("Giá trị nhỏ nhất:", min(my_list))

#5
hoaqua = ['táo', 'chuối', 'cam', 'kiwi', 'mãng cầu', 'dừa']
hoaqua_sx = sorted(hoaqua)
print("DS ban đầu:", hoaqua)
print("DS sau khi sắp xếp:", hoaqua_sx)

#6
old_list = [1, 2, 3, '10', 'abc', 7, 10]
print("DS ban đầu: ", old_list)
f = lambda x: (isinstance(x, int) or isinstance(x, float)) and x%2==0
new_list = list(filter( f, old_list))
print("DS sau khi lọc:", new_list)

#7
input_str = input("Nhập vào các số nguyên, cách nhau bởi dấu cách: ")
num_list = list(map(int, input_str.split()))
num_list = list(map(lambda x: x*x, num_list))
print(num_list)