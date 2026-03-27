# #1
# def tinh_cuoc_taxi(so_km):
#     if so_km <= 1:
#         return (so_km * 15000)
#     elif 2 <= so_km <= 30:
#         #1 km đầu giá 15k, các km còn lại giá 13.5k
#         return (1 * 15000 + (so_km-1) * 13500)
#     else:
#         #1 km đầu 15k, 29km tiếp theo 13.5k, còn lại 11k
#         return (1 * 15000 + 29 * 13500 + (so_km-1) * 11000)

# def main():
#     n = float(input("Nhap so km: "))
#     print(round(tinh_cuoc_taxi(n), 1))
# main()

# #2
# def tinh_S_de_quy(n):
#     if n == 0:
#         return 0
#     return n / (n + 1) + tinh_S_de_quy(n-1)

# def tinh_S_khu_de_quy(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i / (i+1)
#     print(total)

# def main():
#     n = int(input("Nhap so n: "))
#     print(tinh_S_de_quy(n))
#     print(tinh_S_khu_de_quy(n))
# main()

# #3
# def S_de_quy(n):
#     if n == 1:
#         return 1
#     return n**2 + S_de_quy(n-1)

# def S_khu_de_quy(n):
#     tong = 0
#     for i in range(1, n+1):
#         tong += i**2
#     return tong

# def main():
#     n = int(input("Nhap so n: "))
#     print(S_de_quy(n))
#     print(S_khu_de_quy(n))
# main()

#4

ls = [1, 2, 3, 4, 5]
ls.append([7,8,9])
print(len(ls))