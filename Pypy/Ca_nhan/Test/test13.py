#1 - Xoá khoảng trắng ở đầu và cuối chuỗi
word1 = input("Nhập chuỗi: ")
w = word1.strip()
print("Xoá khoảng trắng ở đầu và cuối:", w)
#2 - In ra ký tự xuất hiện nhiều nhất trong chuỗi
word2 = input("Nhập chuỗi: ")
max_char = word2[0]
max_count = word2.count(word2[0])
for ch1 in word2:
    if word2.count(ch1) > max_count:
        max_count = word2.count(ch1)
        max_char = ch1
print("Ký tự xuất hiện nhiều nhất:", max_char)
#3 - Xoá tất cả các chữ số khỏi chuỗi
word3 = input("Nhập chuỗi: ")
kq = ""
for ch2 in word3:
    if not ch2.isdigit():
        kq += ch2
print("Chuỗi sau khi xoá số:", kq)
#4 - Thay toàn bộ khoảng trắng bằng dấu gạch ngang
word4 = input("Nhập chuỗi: ")
print("Sau khi thay toàn bộ:", word4.replace(' ', '-'))
#5 - Kiểm tra chuỗi chỉ gồm chữ cái
word5 = input("Nhập chuỗi: ")
if word5.isalpha():
    print("Hợp lệ")
else:
    print("Không hợp lệ")
#6 - Đếm số ký tự không phải chữ cái
word6 = input("Nhập chuỗi: ")
kq2 = 0
for ch2 in word6:
    if not ch2.isalpha():
        kq2 += 1
print("Đếm số ký tự không phải chữ cái:", kq2)
#7 - Đếm số chữ cái in hoa
word7 = input("Nhập chuỗi: ")
kq3 = 0
for i3 in word7:
    if i3.isupper():
        kq3 += 1
print("Đếm số chữ cái in hoa:", kq3)
#8 - Xoá tất cả các nguyên âm khỏi chuỗi
word8 = input("Nhập chuỗi: ")
kq4 = ''
for i4 in word8:
    if i4.lower() not in 'ueoai':
        kq4 += i4
print("Sau khi xoá tất cả các nguyên âm:", kq4)
#9 - Từ nào dài nhất trong chuỗi
word9 = input("Nhập chuỗi: ")
kq5 = word9.split()
max_word = kq5[0]
for w in kq5:
    if len(w) > len(max_word):
        max_word = w
print("Từ dài nhất:", max_word)
#10 - chuỗi có thường, hoa, số (phân loại giỏi)
word10 = input("Nhập chuỗi: ")
hoa = False
Thuong = False
So = False
for ch in word10:
    if ch.isupper():
        hoa = True
    elif ch.islower():
        thuong = True
    elif ch.isdigit():
        so = True
if hoa and thuong and so:
    print("Chuỗi mạnh!")
else:
    print("Chuỗi yếu!")
#11 - Đếm số ký tự đặc biệt
word11 = input("Nhập chuỗi: ")
kq7 = 0
for i5 in word11:
    if not i5.isalpha() and not i5.isdigit():
        kq7 += 1
print("Ký tự đặc biệt:", kq7)
#12 - In chuỗi mới chỉ gồm các chữ cái mà giữ nguyên thứ tự
word12 = input("Nhập chuỗi: ")
kq8 = ''
for i6 in word12:
    if i6.isalpha():
        kq8 += i6
print("Chuỗi mới chỉ gồm chữ cái:", kq8)
#13 - Kiểm tra chuỗi có bắt đầu chữ cái và kết thúc bằng chữ số?
word13 = input("Nhập chuỗi: ")
if word13[0].isalpha() and word13[-1].isdigit():
    print("Đúng")
else:
    print("Sai")
#14 - Từ nào ngắn nhất trong chuỗi
word14 = input("Nhập chuỗi: ")
kq9 = word14.split()
min_word = kq9[0]
for i9 in kq9:
    if len(i9) < len(min_word):
        min_word = i9
print("Từ ngắn nhất:", min_word)
#15 - Đếm xem có bao nhiêu chữ cái khác nhau
word15 = input("Nhập chuỗi: ")
chucai = ""
for i10 in word15:
    if i10.isalpha() and i10 not in chucai:
        chucai += i10
print("Số chữ cái khác nhau:", len(chucai))
#16 - Ds mới chỉ gồm các số dương
word16 = list(map(int, input("Nhập số nguyên: ").split(",")))
ds_a = []
for x in word16:
    if x > 0:
        ds_a.append(x)
print("Danh sách chỉ gồm số dương", ds_a)
#17 - Ktra xem ds có tăng dần hay ko?
word17 = list(map(int, input("Nhập số n theo thứ tự tăng dần: ").split(",")))
increase = True
for i in range(len(word17)-1):
    if word17[i] > word17[i+1]:
        increase = False
        break
if increase:
    print("Thứ tự tăng dần:", word17)
else:
    print("Không hợp lệ")
#18 - tách các từ thành danh sách và in ra các từ độ dài lớn hơn 3
word18 = input("Nhập chuỗi: ")
ds = word18.split()
for w in ds:
    if len(w) > 3:
        print(w)
#19 - Đếm tần suất xuất hiện của từng kí tự và lưu vào dict
word19 = input("Nhập chuỗi: ")
td = {}
for i in word19:
    if i in td:
        td[i] += 1
    else:
        td[i] = 1
#20 - Dic (Phân loại giỏi)
ds = {
    "Hà" : 7.6,
    "Trung" : 8.8,
    "Huy": 8.0,
    "Minh": 7.5
}
#Những bạn từ điểm 8 trở lên
for ten in ds:
    if ds[ten] >= 8:
        print(ten ,"- Học sinh Giỏi")
#Điểm cao nhất
max_ten = list(ds.keys())[0]
for ten in ds:
    if ds[ten] > ds[max_ten]:
        max_ten = ten
print("Điểm cao nhất đó là:", max_ten,"-",ds[max_ten])