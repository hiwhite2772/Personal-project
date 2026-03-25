menu = {"súp cua": 20,
        "bánh tráng trộn": 15,
        "trà tắc": 10,
        "trà đá": 5,
        "bánh mì": 12,
        "phở bò": 30}
cart = []
total = 0
print("----------- Menu -----------")
for k, v in menu.items():
    print(f"{k:16}: {v:.3f} VND")
print("----------------------------")
while True:
    food = input("Nhập món ăn muốn gọi (ấn q để thoát): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
print("-------- Your order --------")
print(", ".join(cart) + ".")  
for food in cart:
    total += menu[food]
print(f"Tổng tiền các món: {total:.3f} VND")