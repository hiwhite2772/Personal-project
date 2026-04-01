#1
a = int(input("Nhập số thứ 1: "))
b = int(input("Nhập số thứ 2: "))

if a > b:
    print("Số thứ 1 lớn hơn số thứ 2")
else:
    print("Số thứ 1 bé hơn số thứ 2")

#2
totalSale = float(input("Nhập tổng doanh số bán hàng (USD): "))

if totalSale <= 100:
    hoa_hong = totalSale * 0.05
elif totalSale <= 300:
    hoa_hong = totalSale * 0.1
else:
    hoa_hong = totalSale * 0.2

print(f"Hoa hồng: {hoa_hong}")

#3
phut_goi = int(input("Nhập số phút gọi: "))
phi_thue_bao = 25_000 

if phut_goi <= 50:
    phi_goi = phut_goi * 600
elif phut_goi <= 200:
    phi_goi = 50 * 600 + (phut_goi - 50) * 400
else:
    phi_goi = 50 * 600 + 150 * 400 + (phut_goi - 200) * 200
    
tong_cuoc = phi_thue_bao + phi_goi

print(f"Tổng cước điện thoại: {tong_cuoc} đồng")
