class SanPham:
    def __init__(self, ma_sp, ten_sp, gia, so_luong):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.gia = gia
        self.so_luong = so_luong

    def gia(self):
        return self.gia
    
    def gia(self, value):
        if value < 0:
            print("Loi! Gia khong duoc am")
        else:
            self.gia = value
            
    def thanh_tien(self):
        #Gia tien nhan voi so luong sp
        return self.gia * self.so_luong
    
    def xuat(self):
        print("=====Thong tin san pham=====")
        print(f"Ma SP: {self.ma_sp}")
        print(f"Ten SP: {self.ten_sp} VND")
        print(f"Gia SP: {self.gia:,}") #Cai dau phay hien hang nghin. VD: 15000 -> 15,000
        print(f"So luong SP: {self.so_luong}")
        print(f"Thanh tien: {self.thanh_tien():,} VND")
        print("-"*30)

sp1 = SanPham("001", "IELTS", 199000, 2)
sp2 = SanPham("211", "TOEIC", 99000, 4)

sp1.xuat()
sp2.xuat()

sp1.gia = -12000 #Neu co canh bao
sp1.gia = 50000 #Neu cap nhat hop le

print(f"Gia moi sp1: {sp1.gia:,} VND")