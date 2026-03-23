totalSale = float(input("Nhập tổng doanh số bán hàng (USD): "))

if totalSale <= 100:
    hoa_hong = totalSale * 0.05
elif totalSale <= 300:
    hoa_hong = totalSale * 0.10
else:
    hoa_hong = totalSale * 0.20

print(f"Hoa hồng: {hoa_hong}")
