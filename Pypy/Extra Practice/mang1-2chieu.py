import numpy as np

#Bài 1
_list = [10, 20, 30, 40]
arr = np.array(_list)
print(arr)
print("dtype:", arr.dtype) #int64
print("size:", arr.size) #4
print("shape:", arr.shape) #(4,)

#Bài 2
A = np.array([1, 2, 3, 4])
B = np.array([10, 20, 30, 40])
tong = A + B
hieu = B - A
tich = A * B
A_binh_phuong = A**2
print("A:", A) #[1 2 3 4]
print("B:", B) #[10 20 30 40]
print("Tổng của A và B:", tong) #[11 22 33 44]
print("Hiệu của B và A:", hieu) #[ 9 18 27 36]
print("Tích của A và B:", tich) #[ 10  40  90 160]
print("Bình phương của A:", A_binh_phuong) #[ 1  4  9 16]

#Bài 3
_list = [5, 8, 9, 4, 10, 7, 3, 8, 6, 9]
diem = np.array(_list)
dtb = diem.mean()
diem_gioi = diem[diem >= 8]
diem[diem < 5] = 5
print("Điểm TB:", dtb) #6.9
print("Điểm >= 8:", diem_gioi) #[ 8  9 10  8  9]
print("DS sau khi có chỉnh điểm:", diem) #[ 5  8  9  5 10  7  5  8  6  9]