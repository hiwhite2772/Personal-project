#1
import math

def S(x, n):
    tong = 0
    for i in range(1, n+1):
        tong = tong + (x**i) / math.factorial(i)
    return tong

while True:
    try:
        x, n = map(int, input("Nhap x và n: ").split())

        if x >= 0 and n > 0:
            break
        print("Vui lòng nhập x>=0 và n>0")

    except ValueError:
        print("Vui lòng nhập dữ liệu!")

ket_qua = S(x, n)
print(f"S =", ket_qua)

#2
import os

ten_file = "data.txt"

if os.path.exists(ten_file):
    with open(ten_file, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)

else:
    print("File không tồn tại! File có thể tự động tạo và ghi mới...")

    with open(ten_file, "w", encoding="utf-8") as f:
        f.write(f"Kết quả từ câu 1: {str(ket_qua)}")
        print("Đã ghi file!")

    with open(ten_file, "r", encoding="utf-8") as f:
        print(f.read())


#3
def de_quy(n):
    if n < 10:
        return 1
    return 1 + de_quy(n // 10)

def khu_de_quy(n):
    if n < 10:
        return 1
    count = 0
    while abs(n) > 0:
        n //= 10
        count += 1
    return count
    
def main():
    while True:
        try:
            n = int(input("Nhập số nguyên: "))
            if n > 0:
                break
            dq = de_quy(n)
            kdq = khu_de_quy(n)
            print(f"De quy = {dq}")
            print(f"Khu de quy = {kdq}")       
        except ValueError:
            print("Vui lòng nhập dữ liệu!")
main()

#4
class NhanVien:
    def __init__(self, ma_so, ho_ten, luong_co_ban, he_so_luong):
        self.ma_so = ma_so
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban
        self.he_so_luong = he_so_luong
    
    def inputInfor(self):
        while True:
            self.ma_so = input("Nhập mã số nhân viên: ").strip()
            if self.ma_so != 0:
                break
            print("Vui lòng nhập mã số nhân viên!")
        while True:
            self.ho_ten = input("Nhập họ và tên: ").strip()
            if self.ho_ten != 0:
                break
            print("Vui lòng nhập họ và tên!")
        while True:
            try:
                self.luong_co_ban = float(input("Nhập số tiền lương cơ bản: ").strip())
                if self.luong_co_ban > 0:
                    break
                print("Vui lòng nhập số lớn hơn 0!")
            except ValueError:
                print("Vui lòng nhập số!")
        while True:
            try:
                self.he_so_luong = float(input("Nhập hệ số lương: ").strip())
                if self.he_so_luong > 0:
                    break
                print("Vui lòng nhập số lớn hơn 0!")
            except ValueError:
                print("Vui lòng nhập số!")
     
    
    def tinh_luong_nv(self):
        return self.he_so_luong * self.luong_co_ban
    
    def printInfor(self):
        print("\n------Thông tin nhân viên------")
        print(f"Mã số NV: {self.ma_so}")
        print(f"Họ và tên: {self.ho_ten}")
        print(f"Lương nhận: {self.tinh_luong_nv()}")
        
#Tạo 3 đối tượng khác nhau
nv1 = NhanVien("123456", "USA", 1900000, 10)
nv2 = NhanVien("223344", "China", 700000, 7)
nv3 = NhanVien("553214", "India", nv2.luong_co_ban, nv1.he_so_luong)

nv1.printInfor()
nv2.printInfor()
nv3.printInfor()

#Nhân viên có hệ số lương cao nhất trong 3 nhân viên
max_nv = nv1
if nv2.he_so_luong > max_nv.he_so_luong:
    max_nv = nv2
if nv3.he_so_luong > max_nv.he_so_luong:
    max_nv = nv3

print("\n-----Hệ số lương cao nhất-----")
max_nv.printInfor()

#Nhập danh sách NV
n = int(input("\nNhập số lượng nhân viên: "))
ds = []
for i in range(n):
    print(f"\nNhập nhân viên thứ {i+1}:")
    nv = NhanVien("", "", 0, 0)
    nv.inputInfor()
    ds.append((nv))

#Xuất danh sách
for nv in ds:
    nv.printInfor()