"""Bạn cần tạo một hệ thống tính lương đơn giản bằng kế thừa trong Python. 
Tạo lớp NhanVien với thuộc tính ten (tên) và luong_co_ban (lương cơ bản). 
Sau đó tạo lớp NhanVienBanHang kế thừa từ NhanVien, thêm thuộc tính doanh_so (doanh số bán hàng) và phương thức tinh_luong() 
để tính lương thực nhận theo công thức: luong_co_ban + doanh_so * 0.1 (10% doanh số).
Đầu vào: Một dòng chứa ba giá trị cách nhau bởi dấu cách: tên (chuỗi), lương cơ bản (số nguyên), doanh số (số nguyên).
Đầu ra: Một dòng chứa tên và lương thực nhận (làm tròn đến 2 chữ số thập phân), cách nhau bởi dấu cách.

Ví dụ:
Đầu vào: "Nguyen Van A 5000000 20000000"
Đầu ra: "Nguyen Van A 7000000.00" (vì 5,000,000 + 20,000,000 * 0.1 = 7,000,000)

Ràng buộc:
Tên có thể có khoảng trắng, không chứa số.
Lương cơ bản và doanh số là số nguyên dương từ 1 đến 10^9.
Đầu ra lương phải có đúng 2 chữ số thập phân (ví dụ: 7000000.00).
Lưu ý: Trong các test case, đầu ra sử dụng văn bản không dấu để tránh lỗi kỹ thuật (ví dụ: “Nguyen Van A” thay vì “Nguyễn Văn A”)."""

class NhanVien:
    def __init__(self, ten, luong_co_ban):
        self.ten = ten
        self.luong_co_ban = luong_co_ban

class NhanVienBanHang(NhanVien):
    def __init__(self, ten, luong_co_ban, doanh_so):
        super().__init__(ten, luong_co_ban)
        self.doanh_so = doanh_so
    def tinh_luong(self):
        return self.luong_co_ban + self.doanh_so * 0.1

ten, lcb, ds = input().strip().rsplit(maxsplit=2)
nvbh = NhanVienBanHang(ten, int(lcb), int(ds))
print(nvbh.ten, f"{nvbh.tinh_luong():.2f}")
    
