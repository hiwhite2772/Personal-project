#Kiểu dữ liệu chuỗi
vn = input("Hãy cho 1 câu nói về bản thân: ")
print(vn)
print("Số từ:", len(vn))

#Các phương thức chuỗi
#hàm len() và split()
word = input("Đặt câu chủ ngữ và vị ngữ: ")
words = len(word.split())
print("Số từ trong câu là:", words)
#hàm replace()
s = "Học Toán rất dễ"
r = s.replace("Toán", "Lập Trình")
print("Ban đầu:", s)
print("Đổi mới:", r)
#hàm upper() và lower()
text = "tHế kỶ 21 là mỘt nơI hIỆn ĐạI tRêN ToàN ThẾ GiớI."
print("Ban đầu:", text)
print("Viết thường:", text.lower())
print("Viết hoa:", text.upper())
#hàm strip()
name = "   Nguyễn Trần Vĩnh Phong   "
print(name.strip())
#hàm isdigit() và lstrip() và count()
string = input("Nhập chuỗi ký tự số: ")
def check_number(s):
    if s.lstrip('-').isdigit():       # Kiểm tra số nguyên (âm hoặc dương)
        print(f"{s} là một số nguyên")
    elif s.count('.') == 1 and s.replace('.', '').lstrip('-').isdigit():     # Kiểm tra số thực (âm hoặc dương)
        print(f"{s} là một số thực")
    else:
        print(f"{s} không phải là một số")
check_number(string)
