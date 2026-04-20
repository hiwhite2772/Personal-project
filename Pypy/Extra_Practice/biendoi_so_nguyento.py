def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    return True

def test_prime(lst):
    tong = 0
    for i in lst:
        dao_so = int(str(i)[::-1])
        if la_so_nguyen_to(dao_so):
            tong += 1
    return tong
n = int(input("Nhap n: "))
lst = list(input("Nhap danh sach so: ").strip().split())
print(test_prime(lst))