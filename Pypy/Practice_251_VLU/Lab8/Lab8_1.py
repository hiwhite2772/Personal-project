#1
subject = ["KNCDTC", "CSLT", "NMCNTT", "Geograph"]
print("DS ban đầu:", subject)

subject.append("AI")
print("DS đã thêm môn học:", subject)

subject.insert(2, "Math")
print("DS đã thêm môn ở vị trí số 2", subject)

subject.pop(4)
print("DS đã xóa môn ở vị trí số 4", subject)

#2
trai_cay = []
print("Nhập tên trái cây (gõ 'stop' để dừng)")

while True:
    namefruit = input("Nhập tên một loại trái cây: ")
    if namefruit == "stop":
        break
    trai_cay.append(namefruit)

print("Tổng số loại trái cây đã nhập:", len(trai_cay))
print("Toàn bộ danh sách trái cây:", trai_cay)