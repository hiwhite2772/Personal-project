money = 59786
print("Hàng đơn vị:", money % 10)
print("Hàng chục:", (money // 10) % 10)
print("Hàng trăm", (money // 100) % 10)
print("Hàng nghìn:", (money // 1000) % 10)
print("Hàng chục nghìn:", (money // 10000) % 10)
