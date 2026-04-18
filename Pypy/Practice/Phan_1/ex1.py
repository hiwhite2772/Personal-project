#1
def sum_two(a, b):
    return a + b

def main():
    while True:
        try:
            a, b = map(int, input("Nhập 2 số a và b: ").split())
            if a >= 0 and b >= 0:
                break
            print("Vui lòng nhập 2 số đều là số dương")
        except ValueError:
            print("Vui lòng nhập dữ liệu")
    print(sum_two(a, b))
main()

#2
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False
    
def main():
    n = int(input("Nhập số nguyên: "))
    print(is_even(n))
    print(is_odd(n))
main()

#3
def find_max(a, b, c):
    return max(a, b, c)
print(find_max(4, 9, 2))

#4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(4))

