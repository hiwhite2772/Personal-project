t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    for ch in s:
        if ch == "+":
            k += 1
        else:
            k -= 1
    print(k)