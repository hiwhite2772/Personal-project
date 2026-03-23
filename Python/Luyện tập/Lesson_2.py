#1
with open("INPUT1.TXT", "r") as f:
    s = f.readline().strip()
    n = list(map(int, f.readline().split()))

avg = sum(n) / len(n)

with open("OUTPUT1.TXT", "w") as f:
    f.write(f"Ho va ten: {s}\n")
    f.write(f"Diem trung binh: {avg}")

#2
with open("INPUT2.TXT", "r") as f:
    s = f.readline().strip()
    n = list(map(int, f.readline().split()))

diem_cao_nhat = max(n)

with open("OUTPUT2.TXT", "w") as f:
    f.write(s + "\n")
    f.write(str(diem_cao_nhat))

#4
with open("INPUT4.TXT", "r") as f:
    f.readline()
    n = list(map(int, f.readline().split()))

so_lon_nhat = max(n)

with open("OUTPUT4.TXT", "w") as f:
    f.write(str(so_lon_nhat))

#5
with open("INPUT5.TXT", "r") as f:
    f.readline()
    n = list(map(int, f.readline().split()))
    
n.sort()

with open("OUTPUT5.TXT", "w") as f:
    f.write(" ".join(map(str, n)))  #Bỏ dấu ngoặc vuông và dấu phẩy sẽ coi kết quả như yêu cầu đề bài.

#6
with open("INPUT6.TXT", "r") as f:
    f.readline()
    n = list(map(int, f.readline().split()))

tong = 0
for i in n:
    if i % 2 == 0:
        tong += 1

with open("OUTPUT6.TXT", "w") as f:
    f.write(str(tong))

#3 - Cái này mình làm chút rồi, kết quả chắc ko ra dc, vì dữ liệu này khiến tôi ko nghĩ ra nên viết thế nào ra thôi.
with open("INPUT3.TXT", "r") as f:
    s = f.readline().strip()
    n = list(map(int, f.readline().split()))

rank = sum(n) / len(n)

if rank >= 8:
    rank = "Gioi"
elif rank >= 6.5:
    rank = "Kha"
elif rank >= 5:
    rank = "Trung binh"
else:
    rank = "Yeu"

with open("OUTPUT3.TXT", "w") as f:
    f.write(f"Ho va ten: {s} \n")
    f.write(f"Xep loai: {rank}")