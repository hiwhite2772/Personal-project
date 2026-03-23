#exception định nghĩa bởi người dùng
'''
class MyException(BaseException):
    def __init__(self, message = None):
        if (message is None):
            message = "Đã có lỗi xảy ra"
        super().__init__(message)
Để ném ra exception, người dùng phải chủ động ném ra bằng từ khoá raise.
'''

#1
class NegativeNumberError(BaseException):
    def __init__(self, message = None):
        if (message is None):
            message = "Lỗi: Số không được âm"
        super().__init__(message)
def square_root(num):
    if num < 0:
        raise NegativeNumberError()
    else:
        return num ** 0.5
try:
    n = int(input("n = "))
    result = square_root(n)
    print(result)
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên")
except NegativeNumberError as e:
    print(e)
finally:
    print("Chương trình đã kết thúc!")

#2
import math
class RadiusError(BaseException):
    def __init__(self, message = None):
        if (message is None):
            message = "Lỗi: Bán kính không hợp lệ."
        super().__init__(message)

def tinh_chu_vi_hinh_tron(r):
    if isinstance(r, (int, float)):
        if (r <= 0):
            raise RadiusError()
    else:
        raise RadiusError("Bán kính phải là số")
    return 2 * math.pi * r

try:
    n = int(input("n = "))
    print(tinh_chu_vi_hinh_tron(n))
except RadiusError as e:
    print(e)
finally:
    print("Chương trình đã kết thúc!")
