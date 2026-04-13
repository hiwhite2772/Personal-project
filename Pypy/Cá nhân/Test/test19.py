import math
class Tamgiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def inputInfo(self):
        while True:
            try:
                self.a = float(input("Nhap a: "))
                if self.a > 0:
                    break
                print("Vui long nhap so duong")
            except ValueError:
                print("Khong hop le!")

        while True:
            try:
                self.b = float(input("Nhap b: "))
                if self.b > 0:
                    break
                print("Vui long nhap so duong")
            except ValueError:
                print("Khong hop le!")

        while True:
            try:
                self.c = float(input("Nhap c: "))
                if self.c > 0:
                    break
                print("Vui long nhap so duong")
            except ValueError:
                print("Khong hop le!")

    def printInfo(self):
        print(f"a = {self.a}")
        print(f"b = {self.b}")
        print(f"c = {self.c}")

    def chuvi(self):
        return self.a + self.b + self.c

    def nuachuvi(self):
        return self.chuvi() / 2

    def dientich(self):
        p = self.nuachuvi()
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "Ba cạnh không thể tạo thành tam giác!"
        return math.sqrt(p * ((p - self.a) * (p - self.b) * (p - self.c)))

tg = Tamgiac("", "", "")
tg.inputInfo()
tg.printInfo()
print("Chu vi:", tg.chuvi())
print("Nua chu vi:", tg.nuachuvi())
print("Dien tich:", tg.dientich())