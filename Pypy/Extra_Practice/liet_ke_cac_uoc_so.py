# LIỆT KÊ CÁC ƯỚC SỐ
n = int(input("Nhập số n: "))

ds = []
a = abs(n)  # Lấy giá trị tuyệt đối để xét ước số dương

# Nếu bằng 0 thì có vô số ước
if n == 0:
    print("INF")
    exit()  # Thoát để tránh lỗi in danh sách rỗng

else:
    # Duyệt i từ 1 đến căn bậc hai của a
    for i in range(1, int(a**0.5) + 1):
        #Nếu i là ước của n thì thêm vào danh sách
        if n % i == 0:
            ds.append(i)
            # Thêm ước đối xứng nếu khác i (tránh trùng khi i*i = a)
            if i != a // i:
                ds.append(a // i)

# Danh sách sắp xếp theo thứ tự giảm dần
ds.sort(reverse=True)

print("Danh sách các ước số:", " ".join(map(str, ds)))