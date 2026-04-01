lop_hoc = { 
"ten_lop": "K31_IT02", 
"giang_vien": "ThS. Huỳnh Hữu Nghĩa", 
"danh_sach_sv": [ 
{"ma_sv": "10111", "ten": "Nguyễn Quang Huy"}, 
{"ma_sv": "10555", "ten": "Phạm Hoàng Hà"}
] 
}
svm1 = {"ma_sv": "10999", "ten": "Lê Thị Thu Hà"}
svm2 = {"ma_sv": "10777", "ten": "Trần Văn Bảo"}
lop_hoc["danh_sach_sv"].append(svm1)
lop_hoc["danh_sach_sv"].append(svm2)
print(lop_hoc["danh_sach_sv"][1]["ten"])
tongsv = len(lop_hoc['danh_sach_sv'])
print("Tổng số sinh viên:", tongsv)