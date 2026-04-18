#1
with open("numbers.txt", "w") as fw:
    fw.write("1\n2\n3\n4\n5\n6")

tong = 0
with open("numbers.txt", "r") as fr:
    for line in fr:
        so = int(line.strip())
        if so % 2 == 0:
            tong += so

with open("ketqua.txt", "w") as fw:
    fw.write(str(tong))

#2
with open("data.txt", "w") as fw:
    fw.write("10 15 22 33 40 55")

with open("data.txt", "r") as fr:
    data = list(map(int, fr.read().strip().split()))
    print(data)

tong = 0
for line in data:
    n = int(line)
    if n % 5 == 0:
        tong += n

with open("output.txt", "w") as fw:
    fw.write(str(tong))

with open("output.txt", "r") as fr:
    print(tong)