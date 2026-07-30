class Sach:
    def __init__(self, ma_sach, ten_sach, gia_ban, so_luong):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.gia_ban = gia_ban
        self.so_luong = so_luong
    def hien_thi(self):
        print("\n=====HOA DON=====")
        print(f"Ma sach: {self.ma_sach}")
        print(f"Ten sach: {self.ten_sach}")
        print(f"Gia ban: {self.gia_ban}")
        print(f"So luong: {self.so_luong}")
        print(f"Phan loai sach: {self.loai_sach()}")
        print(f"Tong thanh toan: {self.thanh_tien()}")
    def loai_sach(self):
        if self.gia_ban > 100000:
            return "Sach cao cap"
        elif self.gia_ban >= 50000:
            return "Sach trung binh"
        return "Sach gia re"
    def thanh_tien(self):
        if self.loai_sach() == "Sach cao cap":
            return (self.gia_ban * self.so_luong) - (self.gia_ban * self.so_luong * 0.1)
        elif self.loai_sach() == "Sach trung binh":
            return (self.gia_ban * self.so_luong) - (self.gia_ban * self.so_luong * 0.05)
        return self.gia_ban * self.so_luong
    
def main():
    print("\n=====NHAP THONG TIN=====")
    while True:
        try:
            ma_sach = int(input("Nhap ma sach: "))
            if ma_sach > 0:
                break
            print("Vui long nhap so lon hon 0!")
        except ValueError:
            print("Vui long nhap so nguyen!")
    while True:
        ten_sach = input("Nhap ten sach: ").strip()
        if len(ten_sach) != 0:
            break
        print("Vui long khong duoc rong!")
    while True:
        try:
            gia_ban = float(input("Nhap gia sach: "))
            if gia_ban > 0:
                break
            print("Vui long nhap so lon hon 0!")
        except ValueError:
            print("Vui long nhap so thuc!")
    while True:
        try:
            so_luong = int(input("Nhap so luong: "))
            if so_luong >= 0:
                break
            print("Vui long nhap so lon hon hoac bang 0!")
        except ValueError:
            print("Vui long nhap so nguyen!")
    
    sach = Sach(ma_sach,ten_sach,gia_ban,so_luong)
    sach.hien_thi()

if __name__ == "__main__":
    main()