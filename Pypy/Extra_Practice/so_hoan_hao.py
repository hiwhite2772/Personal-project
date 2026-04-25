#KIỂM TRA SỐ HOÀN HẢO

n = int(input())

def kiem_tra_so_hoan_hao_1(n):
    if n < 1:
        return False
    
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    
    return tong == n

def kiem_tra_so_hoan_hao_2(n):
    if n < 2:
        return False
    tong = 1
    for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                tong += i
                if i != n//i:
                    tong += n//i
    return tong == n

if kiem_tra_so_hoan_hao_1(n) and kiem_tra_so_hoan_hao_2:
    print("YES")
else:
    print("NO")
