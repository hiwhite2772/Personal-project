n = int(input())
ds = list(map(int, input().strip().split()))

total = sum(ds)
even = 0
max_ds = 0

for i in ds:
    if i % 2 == 0:
        even += 1
    
    #Chỉ số nguyên dương lớn nhất mà ko phải giá trị lớn nhất
    if i > 0:
        max_ds = i

print(total)
print(even)
print(max_ds)