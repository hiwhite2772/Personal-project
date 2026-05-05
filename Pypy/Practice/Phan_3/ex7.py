def tong_chan(a, n):
    #Điều kiện dừng: duyệt hết mảng
    if n < 0:
        return 0
    # Nếu phần tử hiện tại là số chẵn thì cộng vào tổng
    if a[n] % 2 == 0:
        return a[n] + tong_chan(a, n-1)
    # Nếu không thì bỏ qua
    else:
        return tong_chan(a, n-1)
    
with open("input.txt", "r") as f:
    a = list(map(int, f.readline().strip().split()))

res = tong_chan(a, len(a)-1)

with open("output.txt", "w") as f:
    f.write(str(res))