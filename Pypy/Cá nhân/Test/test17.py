class SoHoc:
    def __init__ (self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

    def getNumber1(self):
        return self.number1
    def setNumber1(self, number1):
        self.number1 = number1
    def getNumber2(self):
        return self.number2
    def setNumber2(self, number2):
        self.number2 = number2

    def inputInfo(self):
        self.number1 = float(input("Nhập số của A: "))
        self.number2 = float(input("Nhập số của B: "))

    def printInfo(self):
        print(f"A = {self.number1}")
        print(f"B = {self.number2}")

    def addition(self):
        return self.number1 + self.number2
    def subtract(self):
        return self.number1 - self.number2
    def multi(self):
        return self.number1 * self.number2
    def division(self):
        if self.number2 == 0:
            return "Lỗi không thể chia cho 0"
        return self.number1 / self.number2
    
toan_hoc = SoHoc()
toan_hoc.inputInfo()
toan_hoc.printInfo()

print("Tổng:", toan_hoc.addition())
print("Hiệu:", toan_hoc.subtract())
print("Tích:", toan_hoc.multi())
print("Thương:", toan_hoc.division())