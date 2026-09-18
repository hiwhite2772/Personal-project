n, m = map(int, input().split())

for i in range(1, (n // 2)+1):
    pattern = ".|." * (2 * i - 1)
    print(pattern.center(m, "-"))

print("WELCOME".center(m, "-"))

for i in range(n // 2, 0, -1):
    pattern = ".|." * (2 * i - 1)
    print(pattern.center(m, "-"))