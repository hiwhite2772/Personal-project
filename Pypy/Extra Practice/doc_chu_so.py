t = int(input("Nhập số lần lượt: "))

for _ in range(t):
    s = input("Nhập số nguyên: ")
    if len(s) < 3:
        s = s.zfill(3) # zfill() dùng để thêm số 0 vào bên trái chuỗi cho đủ độ dài.

    a = int(s[0]) #Hàng trăm
    b = int(s[1]) #Hàng chục
    c = int(s[2]) #Hàng đơn vị

    def doc(x):
        if x == 0: return "khong"
        if x == 1: return "mot"
        if x == 2: return "hai"
        if x == 3: return "ba"
        if x == 4: return "bon"
        if x == 5: return "nam"
        if x == 6: return "sau"
        if x == 7: return "bay"
        if x == 8: return "tam"
        return "chin"

    # ⭐ TRƯỜNG HỢP ĐẶC BIỆT
    if a == 0 and b == 0 and c == 0:
        print("khong")
        continue

    kq = ""

    if a != 0: #Hàng trăm
        kq += doc(a) + " tram"

    if b == 0: #Hàng chục
        if a != 0 and c != 0:
            kq += " le"
    elif b == 1:
        kq += " muoi"
    else:
        kq += " " + doc(b) + " muoi"

    if c != 0: #Hàng đơn vị
        if c == 5 and b != 0:
            kq += " lam"
        else:
            kq += " " + doc(c)

    print(kq.strip())
