#Xoá một phần tử trong set
#VD1
bd = {'red', 'blue', 'yellow'}
print("color capable:", bd)
color = input("Nhập loại màu cần xoá: ")
bd.remove(color)
print("Sau khi tên màu đã xoá, hiện có sau đây:", bd)
#VD2
numbers = {'1', '2', '3', '4'}
print("Các số ban đầu:", numbers)
number = input("Nhập số cần xoá: ")
numbers.discard(number)
print("Sau khi đã xoá, hiện số này là:", numbers)
