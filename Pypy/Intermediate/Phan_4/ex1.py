class SinhVien:
    #Thuộc tính
    def __init__(self, mssv, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.mssv = mssv
        self.__ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    #Nếu thuộc tính: họ tên
    def get_ho_ten(self):
        return self.__ho_ten
    
    #Nếu có thay đổi họ tên thì coi tên mới đó
    def set_ho_ten(self, ho_ten_moi):
        self.__ho_ten = ho_ten_moi

    #Tính điểm trung binh của 3 môn
    def tinh_tb(self):
        return (self.diem_toan + self.diem_ly + self.diem_hoa) / 3
    
    #Xuất thông tin
    def xuat_thongtin(self):
        print("\n"+"-"*20)
        print("Thong tin sinh vien")
        print("-"*20)
        print(f"MSSV: {self.mssv}")
        print(f"Ho va ten: {self.__ho_ten}")
        print(f"Diem mon toan: {self.diem_toan}")
        print(f"Diem mon ly: {self.diem_ly}")
        print(f"Diem mon hoa: {self.diem_hoa}")
        print(f"Diem trung binh: {self.tinh_tb():.2f}")
        print("-"*20)

sv1 = SinhVien(20261235, "Uta", 9.6, 9.4, 9.23)
sv2 = SinhVien(20264535, "Zero", 8.6, 9.8, 9.1)
sv3 = SinhVien(20269775, "Senun", 8.8, 9.6, 9)
sv1.xuat_thongtin()
sv2.xuat_thongtin()
sv3.xuat_thongtin()

sv1.set_ho_ten("Tom")
print(f"Ten moi: {sv1.get_ho_ten()}")