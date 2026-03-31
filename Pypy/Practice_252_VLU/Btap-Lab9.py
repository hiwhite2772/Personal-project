class Person:
    def __init__(self, name, s, dob, address):
        self.name = name
        self.s = s
        self.dob = dob
        self.address = address
    
    def inputInfor(self):
        while True:
            self.name = input("Nhap ten: ").strip()
            if len(self.name) != 0:
                break
            print("Vui long nhap ten!")
        while True:
            self.s = input("Nhap gioi tinh (Nam/Nu): ").strip().lower()
            if (self.s != 0) and (self.s in ['nam', 'nu']):
                break
            print("Vui long nhap gioi tinh (Nam/Nu)")
        while True:
            self.dob = input("Nhap ngay sinh: ").strip()
            try:
                d, m, y = map(int, self.dob.split("/"))
                if 1 <= d <= 31 and 1 <= m <= 12 and y > 1900:
                    break
                print("Ngay sinh khong hop le!")
            except:
                print("Vui long nhap theo dang (dd/mm/yyyy)!")
        while True:
            self.address = input("Nhap dia chi: ").strip()
            if len(self.address) != 0:
                break
            print("Vui long nhap dia chi!")
    
    def showInfor(self):
        print(f"Ten: {self.name}")
        print(f"Gioi tinh: {self.s}")
        print(f"Ngay sinh: {self.dob}")
        print(f"Dia chi: {self.address}")

class Student(Person):
    def __init__(self, mssv, mail, dtb):
        super().__init__("","","","")
        self.mssv = mssv
        self.mail = mail
        self.dtb = dtb
    
    def inputInfor(self):
        super().inputInfor()
        while True:
            self.mssv = input("Nhap MSSV: ").strip()
            if len(self.mssv) != 0:
                break
            print("Vui long nhap MSSV!")
        while True:
            self.mail = input("Nhap email: ").strip()
            if len(self.mail) != 0:
                break
            print("Vui long nhap email!")
        while True:
            try:
                self.dtb = float(input("Nhap diem trung binh: "))
                if 0 <= self.dtb <= 10:
                    break
                print("Diem trung binh khong hop le")
            except:
                print("Vui long nhap diem trung binh!")

    def showInfor(self):
        print("\n=====THONG TIN SINH VIEN=====")
        super().showInfor()
        print(f"MSSV: {self.mssv}")
        print(f"Email: {self.mail}")
        print(f"Diem trung binh: {self.dtb}")
        print(f"Ket qua: {self.hoc_bong()}")
    
    def hoc_bong(self):
        if self.dtb >= 8:
            return "Ban nhan duoc hoc bong!"
        return "Rat tiec! Ban khong the nhan hoc bong!"

class Teacher(Person):
    def __init__(self, lopday, luong1gio, sogioday):
        super().__init__("","","","")
        self.lopday = lopday
        self.luong1gio = luong1gio
        self.sogioday = sogioday
    
    def inputInfor(self):
        super().inputInfor()
        while True:
            self.lopday = input("Nhap ten lop day: ").strip().upper()
            if len(self.lopday) != 0 and self.lopday[0] in ['G', 'H', 'I', 'K', 'L', 'M']:
                break
            print("Ten lop day khong tim thay!")

        while True:
            try:
                self.luong1gio = int(input("Nhap so tien luong: ").strip())
                if self.luong1gio > 0:
                    break
                print("Vui long nhap so tien luong!")
            except:
                print("Vui long nhap du lieu!")
        while True:
            try:
                self.sogioday = int(input("Nhap so gio day: ").strip())
                if self.sogioday > 0:
                    break
                print("Vui long nhap so gio day!")
            except:
                print("Vui long nhap du lieu!")

    def showInfor(self):
        print("\n=====THONG TIN GIANG VIEN=====")
        super().showInfor()
        print(f"Lop day: {self.lopday}")
        print(f"Luong 1 gio day: {self.luong1gio}")
        print(f"So gio day: {self.sogioday}")
        print(f"Luong thuc nhan: {self.luong_thuc_nhan()} VND")
    
    def luong_thuc_nhan(self):
        if self.lopday[0] in ['G', 'H', 'I', 'K'] :
            return self.luong1gio * self.sogioday
        elif self.lopday[0] in ['L', 'M']:
            return (self.luong1gio * self.sogioday) + 200000

def main():
    print("\n=====NHAP THONG TIN SV=====")
    sv = Student("","","")
    sv.inputInfor()
    sv.showInfor()

    print("\n=====NHAP THONG TIN GV=====")
    gv = Teacher("","","")
    gv.inputInfor()
    gv.showInfor()

if __name__ == "__main__":
    main()
