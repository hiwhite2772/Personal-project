#Truy cập vào các phần tử trong set
number = {3, 22, 45, 78, 92}
for element in number:
    print(element, end='\t')
print(92 in number)

#Thêm một phần tử vào set
ds = set()
ds.add(1)
ds.add(2)
ds.add(3)
print(ds)
ds.update([5,6,7,8])
print(ds)