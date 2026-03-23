x = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))

def la_nam_nhuan(n):
    return (n%400==0) or (n%4==0 and n%100!=0)

if x in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {x} có 31 ngày")
elif x in [4, 6, 9, 11]:
    print(f"Tháng {x} có 30 ngày")
elif x == 2:
    if la_nam_nhuan(nam):
        print(f"Tháng 2 năm {nam} có 29 ngày (năm nhuận)")
    else:
        print(f"Tháng 2 năm {nam} có 28 ngày (năm không nhuận)")
else:
    print("Tháng không hợp lệ, vui lòng nhập tháng từ 1 đến 12")
