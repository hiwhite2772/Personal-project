class HocSinh:
    def __init__(self, maHS, tenHS, diemToan, diemVan, diemAnh):
        self.maHS = maHS
        self.tenHS = tenHS
        self.diemToan = diemToan
        self.diemVan = diemVan
        self.diemAnh = diemAnh
    def diemtrungbinh(self):
        return (self.diemToan + self.diemVan +self.diemAnh) / 3
    def xeploai(self):
        if self.diemtrungbinh() >= 8:
            return "Gioi"
        elif self.diemtrungbinh() >= 6.5:
            return "Kha"
        else:
            return "Trung Binh"
    def xuat_tt(self):
        print(f"Ma HS: {self.maHS}")
        print(f"Ten HS: {self.tenHS}")
        print(f"Diem trung binh: {self.diemtrungbinh():.2f}")
        print(f"Xep loai: {self.xeploai()}")
    
def main():
    try:
        t = int(input("Nhap so luong hoc sinh: "))
        if t < 0:
            print("So luong phai lon hon 0!")
    except ValueError:
        print("Vui long nhap so nguyen!")

    ds = []
    for _ in range (t):
        while True:
            maHS = input("Nhap ma HS: ")
            if len(maHS) > 0:
                break
            print("Vui long nhap ma HS!")
        while True:
            tenHS = input("Nhap ten HS: ")
            if len(tenHS) > 0:
                break
            print("Vui long nhap ten HS!")
        while True:
            try:
                diemToan = float(input("Nhap diem Toan: "))
                if 0 <= diemToan <= 10:
                    break
                print("Diem Toan phai tu 0 den 10!")
            except ValueError:
                print("Vui long nhap so!")
        while True:
            try:
                diemVan = float(input("Nhap diem Van: "))
                if 0 <= diemVan <= 10:
                    break
                print("Diem Van phai tu 0 den 10!")
            except ValueError:
                print("Vui long nhap so!")
        while True:
            try:
                diemAnh = float(input("Nhap diem Anh: "))
                if 0 <= diemAnh <= 10:
                    break
                print("Diem Anh phai tu 0 den 10!")
            except ValueError:
                print("Vui long nhap so!")
        
        hs = HocSinh(maHS, tenHS, diemToan, diemVan, diemAnh)
        ds.append(hs)
        
        dem = 0
        for hs in ds:
            dem += 1
            print(f"\nThong tin hoc sinh ({dem}):")
            #Đây là xuất thông tin của từng học sinh đó.
            hs.xuat_tt()
        
        #Tìm học sinh có điểm trung bình cao nhất
        dtb_caonhat = max(ds, key = lambda x: x.diemtrungbinh())    
        
        print(f"\nHoc sinh co diem trung binh cao nhat")
        dtb_caonhat.xuat_tt()
        print()

main()