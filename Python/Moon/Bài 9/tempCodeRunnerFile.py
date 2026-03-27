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