#7
def main():
    try:
        a = int(input())
        b = int(input())
        print(a / b)
    except ValueError:
        print("Lỗi: giá trị không hợp lệ!")        
    except ZeroDivisionError:
        print("Không thể chia cho 0")
main()
#8
def main2():
    try:
        age = int(input())
        print(age)
    except ValueError:
        print("Lỗi: giá trị không hợp lệ!")
main2()