numbers = [10,5,20,15,30,7,42,-5]

numbers.sort()
print("DS sắp xếp theo thứ tự tăng dần:", numbers)

numbers.sort(reverse=True)
print("DS sắp xếp theo thứ tự giảm dần:", numbers)

x = int(input("Nhập số cần đếm: "))
print(f"Số {x} có xuất hiện là {numbers.count(x)} lần trong danh sách.")

print("Có số 42 trong DS không?", "=>", 42 in numbers)
