class Calculator:
    def tong(self, a, b):
        return a + b
    def hieu(self, a, b):
        return a - b
    def tich(self, a, b):
        return a * b
    def thuong(self, a, b):
        if b == 0:
            print("Lỗi ko thể chia cho 0")
            return None
        return a / b