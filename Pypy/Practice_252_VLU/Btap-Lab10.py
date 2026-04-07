#1
def tinh_chi_so_bmi(can_nang, chieu_cao):
    bmi = can_nang / chieu_cao**2
    return round(bmi, 2)

def phan_loai_bmi(bmi):
    if bmi < 18:
        return "Dưới chuẩn"
    elif bmi <= 24.9:
        return "Chuẩn"
    elif bmi <= 29.9:
        return "Thừa cân"
    elif bmi <= 39.9:
        return "Béo, cần giảm cân"
    else:
        return "Rất béo, cần giảm cân ngay"

def main():
    w = float(input("Nhập cân nặng: "))
    h = float(input("Nhập chiều cao: "))
    bmi = tinh_chi_so_bmi(w, h)
    kq = phan_loai_bmi(bmi)
    print(f"\nCân nặng: {w}. Chiều cao: {h}")
    print(f"BMI: {bmi} => Kết quả: {kq}")

main()

#2
def tinh_tong_de_quy(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + tinh_tong_de_quy(n-1)
    else:
        return tinh_tong_de_quy(n-1)

def tinh_tong_khu_de_quy(n):
    tong = 0
    for i in range(0, n+1, 2):
        tong += i
    return tong

n = int(input("Nhập n: "))
dq = tinh_tong_de_quy(n)
kdq = tinh_tong_khu_de_quy(n)

print(dq)
print(kdq)

#3
def ghi_file(fw):
    with open(fw, "w", encoding="utf-8") as f:
        for i in range(5):
            try:
                n = int(input(f"Nhập giá trị thứ {i+1}: "))
                f.write(str(n) + "\n")
            except ValueError:
                print("Không hợp lệ!")

def doc_file(fr):
    tong = 0
    with open(fr, "r", encoding="utf-8") as f:
        for i in f.readlines():
            tong += int(i)
    print(f"Kết quả: {tong}")

file = "data.txt"
ghi_file(file)
doc_file(file)

#4
class SinhVien:
    def __init__(self, ma_sinh_vien, ho_ten, diem_lt, diem_th):
        self.ma_sinh_vien = ma_sinh_vien
        self.ho_ten = ho_ten
        self.diem_lt =diem_lt
        self.diem_th = diem_th

    def hien_thi(self):
        print("\n======THÔNG TIN SINH VIÊN======")
        print(f"Mã sinh viên: {self.ma_sinh_vien}")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm LT: {self.diem_lt}")
        print(f"Điểm TH: {self.diem_th}")
        
    def tinh_diem_trung_binh(self):
        return (self.diem_lt + self.diem_th) / 2

def main():
    while True:
        try:
            n = int(input("Nhập số lượt sinh viên: "))
            if n > 0:
                break
            print("Vui lòng nhập số lớn hơn 0!")
        except ValueError:
                    print("Vui lòng nhập số!")

    ds = []
    for i in range(n):
        print(f"\nNhập thông tin sinh viên {i+1}")
        while True:
            mssv = input("Nhập mã sinh viên: ").strip()
            if len(mssv) != 0:
                break
            print("Vui lòng nhập lại!")
        while True:
            ten = input("Nhập họ tên: ").strip()
            if len(ten) != 0:
                break
            print("Vui lòng nhập lại!")
        while True:
            try:
                diem_lt = float(input("Nhập điểm LT: ").strip())
                if 0 <= diem_lt <= 10:
                    break
                print("Vui lòng nhập số từ 0-10!")
            except ValueError:
                print("Vui lòng nhập số")
        while True:
            try:
                diem_th = float(input("Nhập điểm TH: ").strip())
                if 0 <= diem_th <= 10:
                    break
                print("Vui lòng nhập số từ 0-10!")
            except ValueError:
                print("Vui lòng nhập số")

        sv = SinhVien(mssv, ten, diem_lt, diem_th)
        ds.append((sv))

    for sv in ds:
        sv.hien_thi()
        print(f"Điểm trung bình: {sv.tinh_diem_trung_binh():.2f}")

if __name__ == "__main__":
    main()