#Hỏi x là số dương hay âm
x = int(input("Nhập số x = "))
if x == 0:
    print("x là số ko âm không dương")
if x > 0:
    print("x là số dương")
if x < 0:
    print("x là số âm")

#Hỏi x là số chẵn hay lẻ
x = int(input("Nhập số x = "))
if x%2 == 0:
    print(x, "là số chẵn")
else:
    print(x, "là số lẻ")