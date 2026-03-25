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
