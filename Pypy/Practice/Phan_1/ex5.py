#cau1.py
def nhap_ds(n):
    ds = []
    for _ in range(n):
        while True:
            i = int(input("Nhap so phan tu: "))
            if i > 0:
                break
            print("Vui long nhap so lon hon 0!")
        ds.append(i)
    return ds
#Tong so chan
def tong_so_chan(lst):
    #Gia tri ban dau
    tong = 0

    for i in lst:
        #Tim so chan
        if i % 2 == 0:
            #Tim so chan thi co the cong len
            tong += i
    return tong

def tim_max(lst):
    #vi tri phan tu dau tien
    mx = lst[0]

    for i in lst:
        #Tung so lon hon vi tri phan tu dau tien
        if i > mx:
            mx = i
    return mx

def xuat(lst, tong, mx):
    print("-"*20)
    print(f"Danh sach: {lst}")
    print(f"Tong so chan: {tong}")
    print(f"So lon nhat: {mx}")

def main():
    try:
        n = int(input("Nhap n so nguyen: "))
        ds = nhap_ds(n)
        tsc = tong_so_chan(ds)
        mx = tim_max(ds)
        print(xuat(ds, tsc, mx))
    except ValueError:
        print("Vui long nhap so nguyen!")

main()


#cau2.py
def giai_thua(n):
    if n == 0:
        return 1
    #De quy
    return n * giai_thua(n - 1)

def tong_chu_so(n):
    if n == 0:
        return 0
    return n % 10 + tong_chu_so(n // 10)

def giai_thua_lap(n):
    kq = 1
    while n > 0:
        kq *= n
        n -= 1
    return kq

def main():
    while True:
        try:
            n = int(input("Nhap n: "))
            if n > 0:
                break
            print("Vui long nhap so lon hon 0")
        except ValueError:
            print("Vui long nhap du lieu!")

    while True:
        try:
            m = int(input("Nhap m: "))
            if m > 0:
                break
            print("Vui long nhap so lon hon 0")
        except ValueError:
            print("Vui long nhap du lieu!")

    gt = giai_thua(n)
    tcs = tong_chu_so(m)
    gtl = giai_thua_lap(n)
    print("Giai thua - de quy:", gt)
    print("Tong chu so:", tcs)
    print("Giai thua - khu de quy:", gtl)

main()
