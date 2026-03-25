#Code
n = int(input("Nhap so n = "))
if n < 0:
    print("Khong hop le! Vui long nhap lai so nguyen duong.")
tongchuso = 0
sotam = n
if sotam < 0:
    sotam = abs(sotam)
while sotam > 0:
    chusocuoi = sotam % 10
    tongchuso += chusocuoi
    sotam //= 10
print(f"Tong cac chu so cua {n} la: {tongchuso}")

#Mã Giả:
#B1: Bắt đầu
#B2: Nhập số n 
#B3: Nếu n < 0 thì không hợp lệ
#B4: tongchuso = 0, sotam = n
#B5: Nếu sotam < 0 thì sotam = abs(sotam)
#B6:
# While sotam > 0 
#   tongchuso += chusocuoi
#   tongchuso += chusocuoi
#   sotam //= 10
#B7: In ra tong cac chu so cua n
#B8: Kết thúc