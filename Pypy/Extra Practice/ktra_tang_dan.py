t = int(input())

for _ in range(t):

    s = input().strip()
    current_len = 1
    max_len = 1

    for i in range(1, len(s)):

        if s[i] > s[i-1]:
            current_len += 1
        else:
            current_len = 1

        max_len = max(max_len, current_len)

    print(max_len)