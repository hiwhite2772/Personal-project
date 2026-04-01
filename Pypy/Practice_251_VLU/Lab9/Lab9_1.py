sv_info = {
    'ma_sv': '2574802010111',
    'ten': 'Nguyễn Quang Huy',
    'nganh': 'Công nghệ thông tin',
    'diem_tb': 8.5
}
#1
print("Mã sinh viên:", sv_info['ma_sv'])
print("Họ và tên:", sv_info['ten'])
print("Ngành:", sv_info['nganh'])
print("Điểm trung bình:", sv_info['diem_tb'])

#2
sv_info['email'] = 'goldblue123455@gmail.com' 
sv_info['diem_tb'] += 0.5
sv_info.pop('ma_sv')

print("Dictionary cuối cùng:", sv_info)