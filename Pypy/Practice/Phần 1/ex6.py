#1
def tinh_dtb(a, b):
    return (a + b) / 2

def main():
    while True:
        ten = input("Nhập họ tên: ").strip()
        if len(ten) != 0:
            break
        print("Không được rỗng!")
    while True:
        try:
            a, b = map(float, input("Nhập 2 điểm môn Toán và Văn: ").strip().split())
            if 0 <= a <= 10 and 0 <= b <= 10:
                break
            print("Vui lòng nhập từ 0 đến 10!")
        except ValueError:
            print("Vui lòng nhập đầy đủ 2 môn Toán và Văn!")

    print(f"Họ và tên: {ten}")
    print(f"Điểm trung bình: {tinh_dtb(a, b)}")

# main()

#2
def tinh_tong(x, n):
    total = 0
    for i in range(0, n+1):
        total += x**i
    return total
def main():
    x = int(input("Nhập x: ").strip())
    n = int(input("Nhập n: ").strip())
    print("S =", tinh_tong(x, n))

# main()

#3
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to(lst):
    kq = []
    for i in lst:
        if la_so_nguyen_to(i):
            kq.append(i)
    if kq:
        return kq
    else:
        return "Không thể tìm thấy số nguyên tố trong dãy"
        
def main():
    while True:
        try:
            n = list(map(int, input("Nhập các số: ").strip().split()))
            if len(n) > 5:
                break
            print("Vui lòng nhập hơn 5 số!")
        except ValueError:
            print("Vui lòng nhập số nguyên!")

    print(f"Kết quả: {tim_so_nguyen_to(n)}")

# main()

#4
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to(lst):
    kq = []
    count = 0
    for i in lst:
        if la_so_nguyen_to(i):
            kq.append(i)
            count += 1
    kq.sort()

    return count, kq

def main():
    while True:
        try:
            n = list(map(int, input("Nhập các số: ").strip().split()))
            if len(n) > 5:
                break
            print("vui lòng nhập hơn 5 số")
        except ValueError:
            print("vui lòng nhập số nguyên!")
    
    count, kq = tim_so_nguyen_to(n)

    if kq:
        print("Đếm số nguyên tố:", count)
        print("Sắp xếp:", kq)
    else:
        print("Không có số nguyên tố")

main()