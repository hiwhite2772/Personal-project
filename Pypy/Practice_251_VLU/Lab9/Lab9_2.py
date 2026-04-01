#1
menu = {
    'Phở' : 35000,
    'Bún chả' : 30000,
    'Cơm tấm' : 30000,
    'Bánh mì' : 20000,
    'Gỏi cuốn' : 20000,
    'Hủ tiếu' : 35000,
}
for mon, gia in menu.items():
    print(f"Món: {mon}, Giá: {gia} VNĐ")


#2
chuoi = input("Nhập chuỗi ký tự: ")
ts = {}
for char in chuoi:
    if char != '':
        if char in ts:
            ts[char] += 1
        else:
            ts[char] = 1
print(ts)