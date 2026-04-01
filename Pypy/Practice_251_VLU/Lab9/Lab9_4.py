quan_ly_san_pham = { 
"SP01": {"ten_sp": "Laptop", "so_luong": 50, "don_gia": 15000000}, 
"SP02": {"ten_sp": "Chuột", "so_luong": 200, "don_gia": 150000}, 
"SP03": {"ten_sp": "Bàn phím", "so_luong": 100, "don_gia": 350000} 
}
tong_gia_tri = 0
for masp in quan_ly_san_pham.values():
    gia_tri_sp = masp["so_luong"]*masp["don_gia"]
    tong_gia_tri += gia_tri_sp
print("Tổng giá trị tồn kho:", tong_gia_tri, "VNĐ")