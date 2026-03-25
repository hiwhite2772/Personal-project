chuoi = input("Nhập chuỗi ký tự: ")
ts = {}
for char in chuoi:
    if char != '':
        if char in ts:
            ts[char] += 1
        else:
            ts[char] = 1
print(ts)