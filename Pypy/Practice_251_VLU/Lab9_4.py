tu_dien_anh_viet = {
    'hi''hello': 'xin chào',
    'goodbye': 'tạm biệt',
    'thank you': 'cảm ơn',
    'excuse me': 'xin lỗi',
    'information technology': 'Công nghệ thông tin'
}
tu_tieng_anh = input("Nhập từ tiếng Anh cần dịch: ")
if tu_tieng_anh in tu_dien_anh_viet:
    print("Tiếng việt:", tu_dien_anh_viet[tu_tieng_anh])
else:
    print("Từ này không có trong từ điển.")