def la_so_hoan_hao(a, b, c, k):
    # Tìm số nhỏ nhất và lớn nhất
    min_val = min(a, b, c)
    max_val = max(a, b, c)
    
    #Khoảng cách giữa số lớn nhất và số nhỏ nhất
    # Nếu n <= k thì mọi cặp phần tử <= k
    return (max_val - min_val) <= k


def ba_so_hoan_hao(a, b, c, k):
    # Kiểm tra 3 số hoàn hảo?
    if la_so_hoan_hao(a, b, c, k):
        print("Yes")
    else:
        print("No")


a, b, c, k = map(int, input().split())
ba_so_hoan_hao(a, b, c, k)
