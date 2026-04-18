#1
print("Xin chào mọi người Việt Nam!")
print("1945 - 2025 =",80)
print("Chúc mừng 80 năm ngày Quốc Khánh Việt Nam!")

#2
character_name = "Hi White"
character_age = "18"
print(f"anh trai tên là {character_name}")
print(f"anh trai {character_age} tuổi")
character_name = "parents"
character_age = "55"
print(f"gia đình tên là {character_name}")
print(f"gia đình {character_age} tuổi")

#3
# Ask user for username and password
username = input("Enter username: ")
password = input("Enter password: ")

# Check simple login
if username == "hilusic" and password == "207027":
    print("Login successful!")
else:
    print("Login failed!")

#4
diem = float(input("Nhập điểm lần 1 của bạn: "))
if diem >=5:
    diem_moi = diem + 2
else:
    diem_moi = diem + 5
diem_chinh = round(min(diem_moi, 10), 1)
print("Điểm lần 2 của bạn là:", diem_chinh)

#5
#Greatest Common Divisor - Phân số
from math import gcd
a, b = map(int, input("a, b = ").split())
g = gcd(a, b)  #Phân số
a_new = a // g
b_new = b // g
print(a_new, b_new)

#6
t = int(input("Số lượt nhập: "))
for _ in range(t):
    s = input("Nhập chuỗi ký tự: ").strip()
    print(f"Số ký tự: {len(s)}")