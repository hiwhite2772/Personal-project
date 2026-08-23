def cong_2so(a, b):
    return a + b
def tru_2so(a,b):
    return a - b
def nhan_2so(a, b):
    return a * b
def chia_2so(a, b):
    if a % b == 0:
      return a // b
    return a / b

operations = {"1":cong_2so, "2":tru_2so, "3":nhan_2so, "4":chia_2so}
while True:
    print("1. Cong hai so")
    print("2. Tru hai so")
    print("3. Nhan hai so")
    print("4. Chia hai so")
    print("5. Thoat")

    choice = input().strip()
    if choice == "5":
        print("Tam biet!")
        break

    if choice not in operations:
        print("Lua chon khong hop le!")
        continue

    a = int(input().strip())
    b = int(input().strip())

    result = operations[choice](a, b)
    print(result)