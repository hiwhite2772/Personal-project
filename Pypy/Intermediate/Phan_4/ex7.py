class SanPham:
    def __init__(self, ten, gia):
        self._ten = ten
        self._gia = gia
    
    def get_gia(self):
        return self._gia
    
    def get_ten(self):
        return self._ten
    
def tong_gia_lon_hon(ds, n):
    if n < 0:
        return 0
    if ds[n].get_gia() > 100:
        return ds[n].get_gia() + tong_gia_lon_hon(ds, n-1)
    else:
        return tong_gia_lon_hon(ds, n-1)

n = int(input())
ds = []

for i in range(n):
    ten = input()
    gia = float(input())
    ds.append(SanPham(ten, gia))

result = tong_gia_lon_hon(ds, len(ds) - 1)

print(result)