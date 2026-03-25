#1
with open("data1.txt", "w") as fw:
    for i in range(1, 11):
        fw.write(str(i) + "\n")

#2
name = input("Họ và tên: ")
age = int(input("Tuổi: "))
with open("data2.txt", "w") as file2:
    file2.write(f"Ho va ten: {name}" + "\n")
    file2.write(f"Tuoi: {str(age)}")

#3
with open("INPUT3.TXT", "w") as fw:
    fw.write("1 2")

with open("INPUT3.TXT", "r") as f3:
    data = f3.read().split()

a = int(data[0])
b = int(data[1])
m = max(a, b)

with open("OUTPUT3.TXT", "w") as f3:
    f3.write(str(m))

#4
with open("INPUT4.TXT", "w") as f4:
    f4.write("Nguyen Van A")
    f4.write("8 9 10")

with open("INPUT4.TXT", "r") as f4:
    name = f4.readline().strip()
    scores = list(map(float, f4.readline().split()))

avg = sum(scores) / 3
if avg >= 9:
    rank = "Xuat sac"
elif avg >= 8:
    rank = "Gioi"
elif avg >= 7:
    rank = "Kha"
elif avg >= 5: 
    rank = "Trung binh"
else:
    rank = "Yeu"

with open("OUTPUT4.TXT", "w") as f4:
    f4.write(f"Fullname: {name}" + "\n")
    f4.write(f"Diem trung binh: {str(avg)}" + "\n")
    f4.write(f"Xep loai: {rank}")

#5
with open("INPUT5.TXT", "w") as f:
    f.write("5" + "\n")
    f.write("2 4 5 10 3 8")
with open("INPUT5.TXT", "r") as f:
    n = int(f.readline().strip())
    scores = list(map(int, f.readline().split()))

m_s = max(scores)

with open("OUTPUT5.TXT", "w") as f:
    f.write(str(m_s))

#6
with open("INPUT6.TXT", "w") as f:
    f.write("3 7 2 10 2 14")

with open("INPUT6.TXT", "r") as f:
    scores = list(map(int, f.readline().split()))

m_s = max(scores)

with open("OUTPUT6.TXT", "w") as f:
    f.write(str(m_s))

#7
with open("INPUT7.TXT", "w") as f:
    f.write("5" + "\n")
    f.write("8 7 2 3 1 5")
with open("INPUT7.TXT", "r") as f:
    sl = int(f.readline().strip())
    numbers = list(map(int, f.readline().split()))

numbers.sort()

with open("OUTPUT7.TXT", "w") as f:
    f.write(str(numbers))
