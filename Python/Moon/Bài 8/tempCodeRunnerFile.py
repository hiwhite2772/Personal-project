#câu 5
ds1 = {'a':10, 'b':20, 'c':30}
ds2 = {'d':15,'e':25,'a':35}
ds = ds1.copy()
for k, v in ds2.items():
    if k in ds.keys():
        ds[k] += v
    else:
        ds[k] = v
print("Kết quả là:", ds)