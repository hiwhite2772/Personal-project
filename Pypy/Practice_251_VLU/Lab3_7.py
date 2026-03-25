tong_goi_ho_tro = 3_000_000_000  
so_sinh_vien = 5000

print("Chọn nhóm hỗ trợ của bạn:")
print("1 - Gia đình chính sách")
print("2 - Gia đình có công với cách mạng")
print("3 - Thành tích học tập/rèn luyện tốt")
print("4 - Sinh viên bình thường")

nhom = int(input("Nhập số nhóm của bạn (1-4): "))

ho_tro_ca_nhan = 0

if nhom == 1:
    ho_tro_ca_nhan = tong_goi_ho_tro * 0.20 / 200 
elif nhom == 2:
    ho_tro_ca_nhan = tong_goi_ho_tro * 0.30 / 120  
elif nhom == 3:
    print("\n>> Bạn thuộc nhóm 3 - Nhập thêm điểm để xác định mức hỗ trợ:")
    diem_tb = float(input("Nhập điểm trung bình: "))
    diem_rl = float(input("Nhập điểm rèn luyện: "))
    if diem_tb >= 8.0 and diem_rl >= 80:
        ho_tro_ca_nhan = tong_goi_ho_tro * 0.10 / 1000
    elif 7.0 <= diem_tb < 8.0 and 70 <= diem_rl < 80:
        ho_tro_ca_nhan = tong_goi_ho_tro * 0.08 / 950
    else:
        ho_tro_ca_nhan = tong_goi_ho_tro * 0.05 / (5000 - 200 - 120 - 1000 - 950)
elif nhom == 4:
    ho_tro_ca_nhan = tong_goi_ho_tro * 0.05 / (5000 - 200 - 120 - 1000 - 950)
else:
    print("Nhóm không hợp lệ!")

print(f"\n>> Số tiền bạn được nhận: {int(ho_tro_ca_nhan)} đồng")

sv_nhom1 = 200
sv_nhom2 = 120
sv_nhom3_loai1 = 1000  # >= 8.0 và RL >= 80
sv_nhom3_loai2 = 950   # 7.0–8.0 và RL 70–80
sv_con_lai = 5000 - sv_nhom1 - sv_nhom2 - sv_nhom3_loai1 - sv_nhom3_loai2

tong_nhom1 = tong_goi_ho_tro * 0.20
tong_nhom2 = tong_goi_ho_tro * 0.30
tong_nhom3_loai1 = tong_goi_ho_tro * 0.10
tong_nhom3_loai2 = tong_goi_ho_tro * 0.08
tong_nhom4 = tong_goi_ho_tro * 0.05

tong_da_ho_tro = tong_nhom1 + tong_nhom2 + tong_nhom3_loai1 + tong_nhom3_loai2 + tong_nhom4

print("\n===== THỐNG KÊ HỖ TRỢ CỦA TRƯỜNG =====")
print(f"Tổng hỗ trợ nhóm 1 (chính sách): {int(tong_nhom1)} đồng")
print(f"Tổng hỗ trợ nhóm 2 (có công CM): {int(tong_nhom2)} đồng")
print(f"Tổng hỗ trợ nhóm 3 - loại 1 (>=8.0): {int(tong_nhom3_loai1)} đồng")
print(f"Tổng hỗ trợ nhóm 3 - loại 2 (7.0-8.0): {int(tong_nhom3_loai2)} đồng")
print(f"Tổng hỗ trợ nhóm 4 (bình thường): {int(tong_nhom4)} đồng")
print(f"=> Tổng số tiền đã hỗ trợ: {int(tong_da_ho_tro)} đồng")

if tong_da_ho_tro > tong_goi_ho_tro:
    print(">> CẢNH BÁO: Tổng hỗ trợ vượt quá 3 tỷ đồng!")
elif tong_da_ho_tro < tong_goi_ho_tro:
    print(">> Gói hỗ trợ chưa được sử dụng hết.")
else:
    print(">> Trường đã sử dụng đúng và đủ 3 tỷ đồng để hỗ trợ.")
