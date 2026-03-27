#Cập nhật hoặc thêm phần tử dictionary:
sanpham = {
    'iphone': 15000000,
    'samsung': 12000000,
    'xiaomi': 8000000,
    'oppo': 7000000,
    'nokia': 5000000
}
print("Giá trị ban đầu của dictionary:", sanpham)
sanpham['iphone'] = 25000000
print("Giá trị sau khi cập nhật năm 2017 của dictionary:", sanpham)
sanpham.update({'xiaomi': 10000000})
print("Giá trị sau khi cập nhật mới 2022 của dictionary:", sanpham)
sanpham['sony']=4000000
sanpham.update({'realme':6000000})
print("Giá trị sau khi thêm sản phẩm mới 2025 của dictionary:", sanpham)

#Xóa phần tử trong dictionary:
toys = {
    'lego': 100000,
    'barbie': 200000,
    'action figure': 150000,
    'puzzle': 80000,
    'nito': 8000000
}
toys.pop('barbie')
print("Giá trị sau khi xóa bộ đồ chơi:", toys) #Hàm pop() xóa phần tử theo khóa
toys.popitem()
print(toys) #Hàm popitem() xóa phần tử cuối cùng trong dictionary
del toys['puzzle']
print(toys) #Câu lệnh del xóa phần tử theo khóa
toys.clear()
print("Giá trị cuối cùng:", toys)  #Hàm clear() xóa tất cả các phần tử trong dictionary