with open("input.txt", "w") as fw:
    fw.write("1 2 3 4 5.5 6.5")

with open("input.txt", "r") as f:
    n = list(map(float, f.read().split()))

tong = sum(n)

with open("output.txt", "w") as f:
    f.write(str(tong))

with open("output.txt", "r") as fr:
    print(fr.read())
 