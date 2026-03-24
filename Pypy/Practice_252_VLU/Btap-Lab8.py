#1
class SoHoc:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def getNumber1(self):
        return self.number1
    def getNumber2(self):
        return self.number2

    def setNumber1(self, number1):
        self.number1 = number1
    def setNumber2(self, number2):
        self.number2 = number2
        
    def inputInfo(self):
        self.number1 = float(input("Number 1: "))
        self.number2 = float(input("Number 2: "))

    def printInfo(self):
        print(f"Number 1 = {self.getNumber1()}")
        print(f"Number 2 = {self.getNumber2()}")

    def addition(self):
        tong = self.getNumber1() + self.getNumber2()
        print(f"Tong: {tong}")

    def subtract(self):
        hieu = self.getNumber1() - self.getNumber2()
        print(f"Hieu: {hieu}")
        
    def multi(self):
        tich = self.getNumber1() * self.getNumber2()
        print(f"Tich: {tich}")

    def division(self):
        try:
            thuong = self.getNumber1() / self.getNumber2()
            print(f"Thuong: {thuong}")
        except ZeroDivisionError:
            print("Thuong: Loi khong the chia cho 0")

sh = SoHoc("", "")
sh.inputInfo()
sh.printInfo()
sh.addition()
sh.subtract()
sh.multi()
sh.division()

#2
class NhanVien:
    def __init__(self, ten, tuoi, diachi, tienluong, tongsogiolam):
        self.ten = ten
        self.tuoi = tuoi
        self.diachi = diachi
        self.tienluong = tienluong
        self.tongsogiolam = tongsogiolam
    
    def inputInfo(self):
        
        while True:
            self.ten = input("Nhap ho va ten: ")
            if len(self.ten) != 0:
                break
            print("Vui long nhap lai!")

        while True:
            try:
                self.tuoi = int(input("Nhap tuoi: "))
                if self.tuoi > 0:
                    break
                print("Vui long nhap so duong!")
            except ValueError:
                print("Khong hop le!")

        while True:
            self.diachi = input("Nhap dia chi: ")
            if len(self.diachi) != 0:
                break
            print("Vui long nhap lai!")

        while True:
            try:
                self.tienluong = int(input("Nhap so tien luong: "))
                if self.tienluong > 0:
                    break
                print("Vui long nhap so duong!")
            except ValueError:
                print("Khong hop le!")

        while True:
            try:
                self.tongsogiolam = int(input("Nhap tong so gio lam: "))
                if self.tongsogiolam > 0:
                    break
                print("Vui long nhap so duong!")
            except ValueError:
                print("Khong hop le!")

    def printInfo(self):
        print("\n------Thong Tin Nhan Vien------")
        print(f"Ho va ten: {self.ten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Dia chi: {self.diachi}")
        print(f"Tien luong: {self.tienluong}")
        print(f"Tong so gio lam: {self.tongsogiolam}")
    
    def tinhthuong(self):
        if self.tongsogiolam >= 200:
            thuong = self.tienluong * 0.2
        elif self.tongsogiolam >= 100:
            thuong = self.tienluong * 0.1
        else:
            thuong = 0
        print(f"Nhan thuong: {thuong}")

nv = NhanVien("", "", "", "", "")
nv.inputInfo()
nv.printInfo()
nv.tinhthuong()

#3
class Student:
    def __init__(self, mssv, dtb, tuoi, lop):
        self.mssv = mssv
        self.dtb = dtb
        self.tuoi = tuoi
        self.lop = lop
    def inputInfo(self):
        while True:
            try:
                self.mssv = int(input("Nhap ma sinh vien: "))
                if len(str(self.mssv)) == 8:
                    break
                print("Vui long nhap day du 8 ki tu!")
            except ValueError:
                print("Khong hop le!")

        while True:
            try:
                self.dtb = float(input("Nhap diem trung binh: "))
                if 0.0 <= self.dtb <= 10.0:
                    break
                print("Vui long nhap diem tu 0.0 den 10.0!")
            except ValueError:
                print("Khong hop le!")
        
        while True:
            try:
                self.tuoi = int(input("Nhap so tuoi: "))
                if self.tuoi >= 18:
                    break
                elif self.tuoi < 0:
                    print("Vui long nhap so duong!")
                    continue
                print("Vui long du tuoi 18 tro len!")
            except ValueError:
                print("Khong hop le!")
        
        while True:
            self.lop = input("Nhap ten lop: ")
            if self.lop and self.lop[0].upper() in ["A", "C"]:
                break
            print(f"Lop {self.lop} khong tim thay!")
    def showInfo(self):
        print("\n------Thong tin sinh vien------")
        print(f"MSSV: {self.mssv}")
        print(f"Diem trung binh: {self.dtb}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Lop: {self.lop}")
    def hocbong(self):
        if self.dtb >= 8.0:
            print("Ban nhan duoc hoc bong!")
        print("Rat tiec, ban ko nhan dc hoc bong!")

sinhvien = Student("", "", "", "")
sinhvien.inputInfo()
sinhvien.showInfo()
sinhvien.hocbong()