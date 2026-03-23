quan_ly_san_pham = { 
"SP01": {"ten_sp": "Laptop","so_luong": 50,"don_gia": 10000000}, 
"SP02": {"ten_sp": "Chuột","so_luong": 200,"don_gia": 150000}, 
"SP03": {"ten_sp": "Bàn phím","so_luong": 100,"don_gia": 330000} 
}
for masp, thongtin in quan_ly_san_pham.items():
    print("Sản phẩm:", thongtin["ten_sp"])
ma_sp = input("Nhập mã sản phẩm cần bán: ").strip().upper()
so_luong_ban = int(input("Nhập số lượng bán: "))

if ma_sp in quan_ly_san_pham:
    quan_ly_san_pham[ma_sp]["so_luong"] -= so_luong_ban
    print(f"Đã cập nhật là {ma_sp}: {quan_ly_san_pham[ma_sp]}")
else:
    print("Mã sản phẩm không tồn tại trong kho")