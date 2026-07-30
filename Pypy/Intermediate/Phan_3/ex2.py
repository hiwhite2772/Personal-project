du_lieu = """Nguyen Van A, 7.5
Le Thi B, 8
Tran Minh K, 6.45
To Hai N, 3
Dang Ngoc T, 4"""

with open("sinhvien.txt", "w") as f:
    f.write(du_lieu)

print("\n=======Thong tin sinh vien=======")
with open("sinhvien.txt", "r") as f:
    for i in f:
        i = i.strip()
        if i:
            ho_ten, diem = i.split(",")
            print(f"{ho_ten}:{diem}")

print("\n=======Sinh vien dat diem 5 tro len=======")
with open("sinhvien.txt", "r") as fr:
    with open("dau.txt", "w") as fw:
        for dong in fr:
            dong = dong.strip()
            if dong:
                ho_ten, diem = dong.split(",")
                if float(diem) >= 5:
                    fw.write(dong + "\n")
                    print(f"{ho_ten}:{diem}")
                    
print("\nDa ghi vao file dau.txt thanh cong!")