#Tạo dictionary:
dichtu = {'Vietnam':'Việt Nam', 'korea':'Hàn Quốc', 'japan':'Nhật Bản'}
print(dichtu)

#Truy cập vào các phần tử trong dictionary:
dssv = {
    '101':"Anna",
    '102':"Bob",
    '103':"Charlie",
    '104':"David",
    '105':"Eva"
}
print(dssv['102'])

#Duyệt qua các phần tử trong dictionary:
hoaqua = {'grape':'nho', 'banana':'chuối','pineapple':'dứa','cherry':'anh đào'}
for vegetable in hoaqua.keys():
    print(vegetable, end="\t") #Hàm keys() lấy ra các khóa trong dictionary

for vegetable in hoaqua.values():
    print(vegetable , end="\t") #Hàm values() lấy ra các giá trị trong dictionary

for key, value in hoaqua.items():
    print(key ,"---",value) #Hàm items() lấy ra cả khóa và giá trị trong dictionary