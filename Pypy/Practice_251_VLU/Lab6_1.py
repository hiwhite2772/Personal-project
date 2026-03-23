while True:
    n = input("Nhập số n = ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        break
    else:
        print("Không hợp lệ!")

i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

