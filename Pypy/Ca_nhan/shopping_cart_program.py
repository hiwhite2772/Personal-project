foods = []
prices = []
total = 0

while True:
    food = input("Nhập tên món ăn (Khi muốn dừng lại thì nhập 'E'): ")

    if food == "" or food.lower() == "e":
        break
    else:
        #Vòng lặp kiểm tra giá hợp lệ
        while True:
            try:
                price = int(input("Nhập giá món ăn (VND): "))
                if price <= 0:
                    print("Giá phải là số dương, vui lòng nhập lại!")
                else:
                    break  # Hợp lệ → thoát vòng lặp
            except ValueError:
                print("Không hợp lệ! Vui lòng chỉ nhập số nguyên.")

        foods.append(food)
        prices.append(price)

print("\n-----Hoá Đơn-----")

for i in range(len(foods)):
    print(f"{foods[i]}: {prices[i]} VND")

for y in prices:
    total += y

print(f"------------------")
print(f"Tổng cộng: {total} VND.")

"""
**Những thay đổi chính:**

| Vấn đề | Trước | Sau |
|---|---|---|
| Nhập chữ thay vì số | Báo lỗi nhưng vẫn append | Yêu cầu nhập lại |
| Nhập số âm hoặc bằng 0 | Không kiểm tra | Báo lỗi, nhập lại |
| `foods.append` bị gọi dù lỗi | Lỗi logic | Chỉ append khi hợp lệ |
| In hoá đơn | Chỉ in tên món | In cả tên + giá từng món |

Ví dụ khi chạy (running):
Nhập tên món ăn: Phở
Nhập giá món ăn: abc
Không hợp lệ! Vui lòng chỉ nhập số nguyên.
Nhập giá món ăn: -5
Giá phải là số dương, vui lòng nhập lại!
Nhập giá món ăn: 50000

-----Hoá Đơn-----
Phở: 50000 VND
------------------
Tổng cộng: 50000 VND.
"""