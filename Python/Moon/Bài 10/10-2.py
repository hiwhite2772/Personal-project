#Thực hành
#1
def giai_thua(n):
    if n < 0:
        return -1
    t = 1
    for i in range(1, n+1):
        t *= i
    return t
i = int(input("i = "))
print(giai_thua(i))


#2
def dao_chuoi(s):
    return s[::-1]
i = input()
print(dao_chuoi(i))

#3
def ham_mu(a, b):
    t = 1
    if (b == 0):  # b = 0
        return t
    elif (b > 0):  # b > 0
        for i in range(0, b):
            t *= a
    else:  # b < 0
        for i in range(0, abs(b)):
            t *= a
        t = 1/t
    return round(t, 3)  #Làm tròn đến chữ số thập phân thứ 3

m = float(input("a = "))
n = int(input("b = "))
print(ham_mu(m, n))

#4
# Cách 1:
def transform_list(lst):
    ds = list()
    for x in lst:
        y = 2*x**3 + 3*x + 1
        ds.append(y)
    return ds
#Nhập danh sách các số
ds = list(map(int, input("Ds: "). split()))
print(transform_list(ds))
# Cách 2
andanh = list(map(lambda x: 2*x**3+3*x+1, ds))
print(andanh)

#5 - caesar cipher 
def ma_hoa(s, m):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rs = ''
    for c in s:
        if (c.isupper()):
            i = ALPHABET.find(c)
            if i != -1:
                c = ALPHABET[(i + m) % 26]
        else:
            i = alphabet.find(c)
            if i != -1:
                c = alphabet[(i + m) % 26]
        rs += c
    return rs

i = input("Chuỗi cần mã hoá: ")
n = int(input("Số bước dịch: "))
print(ma_hoa(i, n))