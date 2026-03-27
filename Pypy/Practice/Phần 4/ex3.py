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