#1
import numpy as np
arr = np.array([1, 3, 5, 7, 9, 11, 13, 15])
ba_ptu_dautien = arr[:3]
vitri2_5 = arr[1:5]
reverse_arr = arr[::-1]
print("Ba phần tử đầu tiên là:", ba_ptu_dautien)
print("Vị trí từ thứ 1 đến thứ 4 là:", vitri2_5)
print("Đảo ngược là:", reverse_arr)
#2
arr2 = np.array([120, 150, 90, 200, 180, 130, 160])
max_val = arr2.max()
min_val = arr2.min()
avg_val = arr2.mean()
sum_val = arr2.sum()
print("Doanh thu cao nhất:", max_val)
print("Doanh thu nhỏ nhất:", min_val)
print("Doanh thu trung bình trong tuần:", avg_val)
print("Tổng doanh thu cả tuần:", sum_val)
#3
arr3 = np.array([5, 2, 9, 1, 7, 10, 3])
arg_max = np.argmax(arr3)
arg_min = np.argmin(arr3)
print("Vị trí của phần tử lớn nhất:", arg_max)
print("Vị trí của phần tử nhỏ nhất:", arg_min)
#4
arr4 = np.array([25, 32, 18, 40, 15, 22, 35])
lon_hon_30 = arr4[arr4 > 30]
giua_20_30 = arr4[(arr4 >= 20) & (arr4 <= 30)]
print("Nhiệt độ lớn hơn 30 độ là:", lon_hon_30)
print("Nhiệt độ nằm trong từ khoảng 20 và 30 độ:", giua_20_30)
#5
mark = np.array([4, 7, 3, 9, 5, 2, 8])
mark[mark < 5] = 5
mark[mark % 2 == 0] = -1
print("Điểm số:", mark)
#6
import numpy as np
arr = np.random.randint(1, 101, 10)
sorted_arr = np.sort(arr)
mean_val = arr.mean()
greater_mean = arr[arr > mean_val]
print("Mảng số ngẫu nhiên:", arr)
print("Mảng sắp xếp theo thứ tự:", sorted_arr)
print("Giá trị trung bình của mảng:", mean_val)
print("Phần tử lớn hơn giá trị trung bình của mảng:", greater_mean)
#7
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.concatenate((x, y))
sum_odd_index = z[1::2].sum()
print("Nối mảng:", z)
print("Tổng các phần tử ở vị trí theo số lẻ:", sum_odd_index)
