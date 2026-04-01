bang_diem = [
    ["SV001", "An", 9.5],
    ["SV002", "Bình", 7.0],
    ["SV003", "Cúc", 8.0]
]

print("Tên của sinh viên thứ 2:", bang_diem[1][1])
print("Điểm của sinh viên thứ 3:", bang_diem[2][2])

bang_diem.append(["SV004","Dũng",8.5])
print("DS đã thêm sinh viên mới:", bang_diem)

print("Tên của các sinh viên có điểm >= 8.0")
for sv in bang_diem:
    if sv[2] >= 8.0:
        print(sv[1])