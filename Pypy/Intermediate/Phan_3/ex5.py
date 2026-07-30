with open("input.txt", "r") as f:
    data = list(map(int, f.read().split()))
    print(data)

#Tinh tong cac so chia het so 3
total_three = sum(i for i in data if i % 3 == 0)

with open("output.txt", "w") as f:
    f.write(str(total_three))

with open("output.txt", "r") as f:
    print(f"Tong cac so chia het cho 3: {f.read()}")