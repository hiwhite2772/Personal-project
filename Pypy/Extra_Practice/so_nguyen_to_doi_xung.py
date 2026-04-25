#KIỂM TRA SỐ NGUYÊN TỐ ĐỐI XỨNG

def la_so_nguyen_to(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_doi_xung(i):
    s = str(i)
    return s == s[::-1]

T = int(input())
for _ in range(T):
    l, r = map(int, input().strip().split())
    lst = [i for i in range(l, r+1)]
    
    tong = 0
    for i in lst:
        if kiem_tra_so_doi_xung(i) and la_so_nguyen_to(i):
            tong += i
    print(tong)
