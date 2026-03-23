#1
def so_lon_nhat(a, b, c):
    return max(a, b, c)

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print("Số lớn nhất là", so_lon_nhat(a, b, c))

#2
def kiemtra_tontai(lst, x):
    if x in lst:
        print("Có trong danh sách")
        return True
    else:
        print("Không có trong danh sách")
        return False

lst = [1, 4, 7, 5, 8, 9]
x = int(input("Nhập số cần kiểm tra: "))
kiemtra_tontai(lst, x)

#3
def ham_ngoai(lst):
    def ham_trong(i, j):
        lst[i], lst[j] = lst[j], lst[i]
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                ham_trong(i, j)
    return lst
lst = [5, 2, 9, 1, 44, 6]
print("Danh sách ban đầu là", lst)
print("Danh sách có sắp xếp thứ tự là", ham_ngoai(lst))

#4
def my_map(func, lst):
    return list(map(lambda x: func(x), lst))
def square(x):
    return x*x
lst = [1, 2, 3, 4, 5]
print("Danh sách ban đầu là", lst)
print("Danh sách có bình phương là", my_map(square, lst))

#5
def statistics(data, stats):
    stats["sum"] = sum(data)
    stats["average"] = sum(data) / len(data)
    stats["max"] = max(data)
    stats["min"] = min(data)
    return stats
data = [2, 4, 6, 8, 10]
result = {}
statistics(data, result)
print("Thống kê dữ liệu:", result)