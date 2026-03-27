#Thực hành
#Câu 1
so = set(map(int, input("Nhập số: ").split(",")))
t = 0
for i in so:
    t += i
print("Tổng các số là:", t)
#câu 2
so1 = set()
input1 = input("số 1 = ").split(",")
for i in input1:
    try:
        val = float(i)
        if val.is_integer():
            val = int(val)
        so1.add(val)
    except ValueError:
        so1.add(i.strip())

so2 = set()
input2 = input("số 2 = ").split(",")
for i in input2:
    try:
        val = float(i)
        if val.is_integer():
            val = int(val)
        so2.add(val)
    except ValueError:
        so2.add(i.strip())

s = so1.intersection(so2)

rs = set()
for i in s:
    if isinstance(i, (int, float)):
        rs.add(i)
print("Kết quả là:", rs)
#câu 3
s = input("Nhập chuỗi: ")
d = dict()
for i in s:
    k = s.count(i)
    d[i] = k
print(d)
#câu 4
so = {'a':10, 'b':20, 'c':30, 'd':'hello'}
t = 0
for i in so.values():
    if isinstance(i, (int, float)):
        t += i
print("Tổng các giá trị là:", t)
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