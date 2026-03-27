#Tạo 1 tuple các phần tử
#1
food = ("pizza", "bread", "Salad", "Snack")
for eat in food:
    print(eat)
#2
so1 = [1,2,3,4,5]
so2 = tuple(so1)
print(so2)

#Truy cập các phần tử trong tuple
food = ("ice-cream", "pho", "bread")
print(food[-1])
print(food[1])

#Duyệt qua các phần tử trong tuple
#1
drink = ("coca", "pepsi", "7up", "water")
for uong in drink:
    print(uong, end=" ")
#2
drink = ("coca", "pepsi", "7up", "water")
for i in range(len(drink)):
    print(drink[i], end=" ")

#Các hàm trong tuple
#1
tk = input("Nhập tìm hoa quả: ")
fruits = ("táo", "chuối", "dưa lưới", "nho")
print(f"\'{tk}\' ở vị trí {fruits.index(tk)} ")
