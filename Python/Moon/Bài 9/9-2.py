#Thực hành 
#B1
s = input("Nhập cụm từ: ")
print("Số từ trong câu đó là:", len(s))
#B2
s = input("Nhập cụm từ: ")
l = list(s.split())
print("Danh sách các từ:", l)
#B3
s = input("Nhập cụm từ: ")
for i in range(0, len(s)):
    if i % 2 == 0:
        print(s[i].upper(), end="")
    else:
        print(s[i].lower(), end="")
#B4
s = "    Python is an interpreted, high-level, general-purpose programming language.    "
l = s.strip()
s = ''.join(l)
print(s)
#B5
s = input("Nhập chuỗi: ")
re = True
j = len(s) - 1
for i in range(0, len(s)):
    if i == j:
        break
    if s[i] != s[j]:
        re = False
        break
    j -= 1
print(re)