n = int(input("Nhập số sinh viên: "))
students = {}
# Nhập dữ liệu
for i in range(n):
    name = input("Nhập tên sinh viên: ")
    score = float(input("Nhập điểm trung bình: "))
    students[name] = score
# In danh sách sinh viên
print("Danh sách sinh viên:")
for name in students:
    print(name,":",students[name]) 
# Tìm sinh viên có điểm cao nhất
max_name = ""
max_score = -1
for name in students:
    if students[name] > max_score:
        max_score = students[name]
        max_name = name
print("Sinh viên có điểm cao nhất:", 
      max_name,":",max_score)