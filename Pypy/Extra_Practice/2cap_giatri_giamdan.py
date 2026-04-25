a, b = map(int, input().split())
ds = []

#Duyệt ds theo giảm dần
for i in range(b - 1, a, -1):
    if i % 3 == 0:
        ds.append(i)
        #Tìm 2 số lớn nhất
        if len(ds) == 2:
            break
if ds:
    print(*ds)
else:
    print("NOT FOUND")