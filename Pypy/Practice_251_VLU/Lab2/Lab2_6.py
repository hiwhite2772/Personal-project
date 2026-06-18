quet_nha = 2000
lau_nha = 2000
rua_chen = 1000
ui_quan_ao = 1000
giat_phoi_qa = 2000

anh_ca = (quet_nha + rua_chen + ui_quan_ao) * 4
co_em = (quet_nha + lau_nha + giat_phoi_qa) * 3

print(f"Anh cả nhận được {anh_ca} VND")
print(f"Cô em nhận được {co_em} VND")
print(f"Tổng tiền bố mẹ trả: {anh_ca+co_em} VND")

if anh_ca >= 15000:
    print("Đủ tiền mua chiếc balo")
else:
    print("Không đủ rồi!")
