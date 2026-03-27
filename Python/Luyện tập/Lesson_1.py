#1
f = "INPUT1.TXT"
file = open(f, "r")
i = list(map(int,file.read().split()))
file.close()

fw = open("OUTPUT1.TXT", "w")
fw.write(str(min(i)))
fw.close()

#2
f2_i = open("INPUT2.TXT", "r")
i2 = list(map(int, f2_i.read().split()))
f2_i.close()

f2_o = open("OUTPUT2.TXT", "w")
total = sum(i2)
f2_o.write(str(total))
f2_o.close()

#3
f = open("INPUT3.TXT", "r")
sapxep = list(map(int, f.read().split()))
f.close()
sapxep.sort(reverse=True)

f = open("OUTPUT3.TXT", "w")
for i in sapxep:
    f.write(str(i) + " ")
f.close()

#4
f = open("INPUT4.TXT", "r")
sochan = list(map(int, f.read().split()))
f.close()

tong = 0
for i in sochan:
    if i % 2 == 0:
        tong += 1

fw = open("OUTPUT4.TXT", "w")
fw.write(str(tong))
fw.close()

#5
f = open("INPUT5.TXT", "r")
tbc = list(map(int, f.read().split()))
f.close()

tbc_ds = sum(tbc) / len(tbc)

fw = open("OUTPUT5.TXT", "w")
fw.write(str(tbc_ds))
fw.close()

#TEST - CODE NGẮN GỌN (TỰ ĐÓNG FILE)
with open("data.txt", "r") as f:
    numbers = list(map(int, f.read().split()))
solon = max(numbers)
with open("data2.txt", "w") as f:
    f.write(str(solon))
