class DIEN_THOAI:
    def __init__(self, ma_may, ten_may, don_gia, so_luong):
        self.ma_may = ma_may
        self.ten_may = ten_may
        self.don_gia = don_gia
        self.so_luong = so_luong

    def tinh_thanh_tien(self):
        return self.don_gia * self.so_luong
    
    def hien_thi(self):
        print("\n------Thong tin dien thoai------")
        print(f"Ma may: {self.ma_may}")
        print(f"Ten may: {self.ten_may}")
        print(f"Don gia: {self.don_gia}")
        print(f"So luong: {self.so_luong}")
        print(f"Tong thanh: {self.tinh_thanh_tien()}")
dienthoai = DIEN_THOAI("IOS2026","Iphone 19 promax", 42300040, 2)
dienthoai.hien_thi()