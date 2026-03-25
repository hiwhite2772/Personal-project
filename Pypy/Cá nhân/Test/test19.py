class Student:
    def __init__(self, mssv="", dtb=0.0, tuoi=0, lop=""):
        self.mssv = mssv
        self.dtb = dtb
        self.tuoi = tuoi
        self.lop = lop

    def inputInfo(self):

        while True:
            self.mssv = input("Nhập mã sinh viên: ")
            if len(self.mssv) == 8:
                break
            print("Vui lòng nhập mã sinh viên đủ 8 ký tự!")

        while True:
            try:
                self.dtb = float(input("Nhập điểm trung bình: "))
                if 0.0 <= self.dtb <= 10.0:
                    break
                print("Vui lòng nhập điểm số từ 0.0 đến 10.0")
            except ValueError:
                print("Vui lòng nhập điểm số!")

        while True:  
            try:
                self.tuoi = int(input("Nhập số tuổi: "))
                if self.tuoi >= 18:
                    break
                print("Vui lòng đủ 18 tuổi trở lên!")
            except ValueError:
                print("Vui lòng nhập số tuổi!")

        while True:
            self.lop = input("Nhập tên lớp: ")
            if self.lop and self.lop[0].upper() in ["A", "C"]:
                break                
            print(f"Tên lớp không hợp lệ.")

    def showInfo(self):
        print("\n------Thông tin sinh viên------")
        print(f"Mã sinh viên: {self.mssv}")
        print(f"Điểm trung bình: {self.dtb}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Lớp: {self.lop}")

    def hocbong(self):
        if self.dtb >= 8.0:
            return "Bạn nhận được học bổng!"
        return "Bạn chưa đủ điều kiện học bổng"

sinhvien = Student()
sinhvien.inputInfo()
sinhvien.showInfo()

print("\n------Thông báo------")
print(sinhvien.hocbong())
print()