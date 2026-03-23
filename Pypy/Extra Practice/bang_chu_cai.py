n = int(input("Nhập chọn bảng chữ cái (in hoa - 1 hoặc in thường - 2): "))

if n == 1:
    start = ord('A')
else:
    start = ord('a')
    
for i in range(26):
    print(chr(start + i), end = " ")
