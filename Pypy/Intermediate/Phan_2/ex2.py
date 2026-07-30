def main():
    try:
        n = int(input())
        if n <= 0:
            print("Số phải lớn hơn 0")
        else:
            print("Số nguyên dương")
    except ValueError:
        print("Lỗi: phải nhập số")
main()

def main2():
    try:
        numbers = [10, 20, 30, 40]
        i = int(input())
        gia_tri = numbers[i]
        print(gia_tri)
    except ValueError:
        print("Phải nhập số!")
    except IndexError:
        print("Index không hợp lệ!")
main2()

def main3():
    try:
        with open("demo.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Không tìm thấy file!")
main3()

def main4():
    data = ["10", "20", "abc", "40"]
    total = 0
    for i in data:
        try:
            num = int(i)
            total += num
        except ValueError:
            pass
    print("Tổng:", total)
main4()

def main5():
    try:
        pw = input()
        if len(pw) < 6:
            raise ValueError("Password quá ngắn")
        else:
            print("Password hợp lệ")
    except ValueError as e:
        print(e)
main5()