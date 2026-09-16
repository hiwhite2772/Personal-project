from functools import reduce
lst = list(map(int, input().split()))
ds_pos = list(filter(lambda x: x > 0, lst))

if ds_pos:
    res = reduce(lambda x, y: x + y, ds_pos)
    print(res)
else:
    print("0")