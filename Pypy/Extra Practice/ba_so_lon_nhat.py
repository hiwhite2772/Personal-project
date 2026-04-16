# Cách 1
n = int(input())
ds = list(map(int, input().split()))
print(max(ds))
ds.remove(max(ds))
print(max(ds))
ds.remove(max(ds))
print(max(ds))

# Cách 2
n = int(input())
ds = list(map(int, input().split()))
ds.sort(reverse=True)
print(ds[0])
print(ds[1])
print(ds[2])
