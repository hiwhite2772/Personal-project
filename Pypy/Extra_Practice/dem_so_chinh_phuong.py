from math import isqrt, sqrt, ceil
a, b = map(int, input().split())

left = ceil(sqrt(a))
right = isqrt(b)

if left > right:
    print(0)
else:
    print(right - left + 1)