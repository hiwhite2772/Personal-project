#Bài 1
def kiem_tra(a):
    if a>0:
        return True
    else:
        return False
a = 2
if kiem_tra(a):
    print("a là số dương")
else:
    print("a là số âm")

#Bài 2
def kiemtra_so_nguyen_to(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True
a = 12
if kiemtra_so_nguyen_to(a):
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")

#Bài 3
def nhiet_do_f(f):
    c = 5*(f-32)/9
    print("Nhiệt độ C là", round(c, 1))
nhiet_do_f(88)

#Bài 4
def mot_thang(m):
    if m < 1 or m > 12:
        print("Không hợp lệ. Vui lòng nhập (1-12)")
    elif m <= 3:
        print("Mùa Xuân")
    elif m <= 6:
        print("Mùa Hạ")
    elif m <= 9:
        print("Mùa Thu")
    else:
        print("Mùa Đông")
mot_thang(7)

#Bài 5
def ban_kinh(R):
    PI = 3.142
    S = PI*R*R
    C = 2*PI*R
    print("Diện tích hình tròn:", round(S, 1))
    print("Chu vi hình tròn:", round(C,1))
ban_kinh(3)

#Bài 6
def mot_nam(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("Đó là năm nhuận")
    else:
        print("Không phải là năm nhuận")
mot_nam(2028)

#Bài 7
def trung_binh_cong(a, b):
    tbc = 0
    for i in range (a, b + 1):
        tbc += i
    tbc = (tbc)/(b - a + 1)
    return tbc
print(trung_binh_cong(1, 4)) # 2.5
# (1 + 2 + 3 + 4)/4 = 10/4
# #--Em không biết làm này, em làm ý tưởng cấu trúc này.--

#Bài 8
#--Em không biết làm này.--