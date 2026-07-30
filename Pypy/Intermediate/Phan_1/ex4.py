#1
def tong_chan(ds):
    #Day la tong cac so chan trong ds
    return sum(x for x in ds if x % 2 == 0)

def so_lon_nhat(ds):
    #Day tim so lon nhat trong ds
    return max(ds)

def main():
    try:
        n = int(input("Nhap so luot: "))
      
        while True:
            try:
                ds = [int(input(f"Nhap so nguyen thu {i+1}: ")) for i in range(n)]
                if len(ds) > 0:
                    break
                print("Vui long nhap so nguyen duong!")

                print(f"Tong cac so chan: {tong_chan(ds)}")
                print(f"So lon nhat: {so_lon_nhat(ds)}")
            
            except ValueError:
                print("Vui long nhap so nguyen!")

    except ValueError:
        #Neu nhap sai so nguyen thi coi nhu ket qua
        print("Vui long nhap so nguyen!")  
main()

#2
def tong_dq(n):
    if n == 0:
        return 0
    return n + tong_dq(n-1)

def tong_khu_dq(n):
    if n == 0:
        return 0
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def main():
    try:
        i = int(input("Nhap so nguyen: "))
        print(f"Tong: {tong_dq(i)}")
        print(f"Tong: {tong_khu_dq(i)}")
    except ValueError:
        print("Vui long nhap so nguyen!")
main()