class NhanVien:
    def __init__ (self, name="", age=0, address="", salary=0, total_working_hours=0):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.total_working_hours = total_working_hours
    
    def inputInfo(self):
        self.name = input("Nhap ho va ten: ")
        self.age = int(input("Nhap tuoi: "))
        self.address = input("Nhap dia chi: ")
        self.salary = int(input("Nhap so tien luong: "))
        self.total_working_hours = int(input("Nhap tong so gio lam: "))
    
    def printInfo(self):
        print("\n\t-----Thong tin nhan vien-----\n")
        print(f"Ho va ten: {self.name}")
        print(f"Tuoi: {self.age}")
        print(f"Dia chi: {self.address}")
        print(f"Tien luong: {self.salary}")
        print(f"Tong so gio lam: {self.total_working_hours}")
        print(f"So tien thuong: {dilam.tinhThuong()}")

    def tinhThuong(self):
        if self.total_working_hours >= 200:
            bone = self.salary * 0.2
        elif 100 <= self.total_working_hours < 200:
            bone = self.salary * 0.1
        else:
            bone = 0
        return bone

dilam = NhanVien()
dilam.inputInfo()
dilam.printInfo()
