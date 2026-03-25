#1
def nhap_diem(n):
    ds = []
    for i in range(n):
        while True:
            diem = float(input(f"Nhập điểm thứ {i+1}: "))
            if 0 <= diem <= 10:
                ds.append(diem)
                break
            else:
                print("vui lòng nhập điểm từ 0 - 10")
    return ds

def tinh_tb(ds_diem):
    return sum(ds_diem) / len(ds_diem)

def xep_loai(dtb):
    if dtb >= 8.0:
        return "Giỏi"
    elif dtb >= 6.5:
        return "Khá"
    elif dtb >= 5:
        return "Trung bình"
    else:
        return "Yếu"
    
def main():
    n = int(input("Nhập số môn học: "))
    ds_diem = nhap_diem(n)
    dtb = tinh_tb(ds_diem)
    xl = xep_loai(dtb)
    print(f"Điểm trung bình: {dtb:.2f}")
    print(f"Xếp loại: {xl}")
main()

#2
#Hàm đệ quy
def fib_de_quy(n):
    if n == 0 or n == 1:
        return n
    return fib_de_quy(n-1) + fib_de_quy(n-2)
print([fib_de_quy(i) for i in range(11)])

#Khử đệ quy
def khu_dq(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b
print([khu_dq(i) for i in range(11)])

print(f"n = 10 -> Đệ quy: {fib_de_quy(10)}. Khử DDQ: {khu_dq(10)}")