n = int(input("Nhập chọn bảng chữ cái (in hoa - 1 hoặc in thường - 2): "))

#Xác định điểm bắt đầu trong bảng mã ASCII (A hoặc a)
if n == 1:
    start = ord("A")
elif n == 2:
    start = ord("a")
else:
    print("Không hợp lệ! Vui lòng nhập số 1 hoặc 2!")
    exit()  #Thoát để tránh lỗi biến 'start' chưa được gán

print("Danh sách các chữ cái:", end=" ")
for i in range(26):
    print(chr(start + i), end=" ")  #Chuyển mã ASCII về ký tự
