trai_cay = []
print("Nhập tên trái cây (gõ 'stop' để dừng)")

while True:
    namefruit = input("Nhập tên một loại trái cây: ")
    if namefruit == "stop":
        break
    trai_cay.append(namefruit)

print("Tổng số loại trái cây đã nhập:", len(trai_cay))
print("Toàn bộ danh sách trái cây:", trai_cay)