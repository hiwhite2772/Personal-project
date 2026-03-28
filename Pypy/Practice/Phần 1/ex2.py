#1
def nhap_diem(n):
    ds = []
    for i in range(n):
        while True:
            try:
                diem = float(input(f"Nhập điểm thứ {i+1}: "))
                if 0 <= diem <= 10:
                    ds.append(diem)
                    break
                else:
                    print("vui lòng nhập điểm từ 0 - 10")
            except ValueError:
                print("Vui lòng nhập dữ liệu!")
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
    while True:
        try:
            n = int(input("Nhập số môn học: "))
            if n > 0:
                break
            print("Vui lòng nhập số dương")
        except ValueError:
            print("Vui lòng nhập dữ liệu!")

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

#Khử đệ quy
def khu_dq(n):
    if n == 0 or n == 1:
        return n
    
    a, b = 0, 1

    for _ in range(2, n+1):
        a, b = b, a+b
    return b

def main():
    while True:
        try:
            n = int(input("Nhập số nguyên: "))
            if n >= 0:
                break
            print("Vui lòng nhập số dương!")
            
        except ValueError:
            print("Vui lòng nhập dữ liệu!")

    print(f"n = {n}\n-> Đệ quy: {fib_de_quy(n)}\n-> Khử DDQ: {khu_dq(n)}")
        
main()