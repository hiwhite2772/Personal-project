#Thực hành:
#1
try:
    a, b = map(float, input("a, b = ").split(","))
    print(a + b)
except ValueError:
    print("Lỗi: không phải số!")
#2
class MaxError(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "Lỗi: Danh sách rỗng"
        super().__init__(message)
def tim_max(ls):
    if not isinstance(ls, list):
        raise TypeError("Truyền vào danh sách")
    if len(ls) == 0:
        raise MaxError()
    return max(ls)

try:
    s = input().strip()
    if s == "":
        lst = []
    else:
        lst = list(map(int, s.split(",")))
    print(tim_max(lst))
except ValueError:
    print("Vui lòng nhập số!")
except TypeError as e:
    print(e)
except MaxError as e:
    print(e)
#3
while True:
    try:
        n = int(input("n = "))
        if n < 0:
            raise ValueError()
        else:
            print(bin(n)[2:])
            break
    except ValueError:
        print("Lỗi: vui lòng nhập số!")
        continue
#4
class NegativeNumberError(Exception):
    def __init__(self, message = None):
        if message is None:
            message = "Lỗi: Số không được âm."
        super().__init__(message)
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n-1)
try:
    try:
        i = int(input("n = "))
    except ValueError:
        raise TypeError("Lỗi - n phải là số nguyên")
    if i < 0:
        raise NegativeNumberError()
    else:
        print(giai_thua(i))
except TypeError as e:
    print(e)
except NegativeNumberError as e:
    print(e)