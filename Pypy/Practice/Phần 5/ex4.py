class HOCSINH:
    def __init__(self, maHS, tenHS, diemToan, diemVan):
        #Thuoc tinh: maHS, tenHS, diemToan, diemVan
        self.maHS = maHS
        self.tenHS = tenHS
        self.diemToan = diemToan
        self.diemVan = diemVan
    
    def diem_tb(self):
        #Tinh diem trung binh co 2 mon toan va van
        return (self.diemToan + self.diemVan) / 2
    
    def xuat_tt(self):
        #Xuat ra thong tin hoc sinh
        print(f"Ma HS: {self.maHS}")
        print(f"Ten HS: {self.tenHS}")
        print(f"Diem trung binh: {self.diem_tb():.2f}")

def main():
    try:
        t = int(input("Nhap so luot hoc sinh: "))
        ds = []
        for i in range(t):
            print(f"\n----NHAP THONG TIN HS ({i+1})----")

            while True:
                mhs = input("Nhap ma HS: ")
                if len(mhs) != 0:
                    break
                print("Vui long nhap ma HS!")

            while True:
                ths = input("Nhap ten HS: ")
                if len(ths) != 0:
                    break
                print("Vui long nhap ten HS!")

            while True:
                try:
                    diemtoan = float(input("Nhap diem toan: "))
                    if 0 <= diemtoan <= 10:
                        break
                    print("Vui long nhap diem toan tu 0 den 10!")
                except ValueError:
                    print("Vui long nhap so!")    
                            
            while True:
                try:
                    diemvan = float(input("Nhap diem van: "))
                    if 0 <= diemvan <= 10:
                        break
                    print("Vui long nhap diem van tu 0 den 10!")
                except ValueError:
                    print("Vui long nhap so!")

            hs = HOCSINH(mhs, ths, diemtoan, diemvan)
            ds.append(hs)

        for hs in ds:
            print("\n------THONG TIN HOC SINH------")
            hs.xuat_tt()

        dtb_cao_nhat = max(ds, key = lambda x: x.diem_tb())
        print("\nHoc sinh co diem trung binh cao nhat:")
        dtb_cao_nhat.xuat_tt()
    
    except ValueError:
        print("Vui long nhap so nguyen!")
main()