# 1
my_str = "Hello"
x = 0
for i in my_str:
    x += 1
    print(my_str[0:x])
for i in my_str:
    x -= 1
    print(my_str[0:x])

# 2
s = "ABCDE"
x = 0
for i in range(1, len(s) + 1):
    print(s[0:i])
print()

# 3
s = "ABCDE"
for i in range(len(s), 0, -1):
    print(s[0:i])
print()

# 4
x = "12345"
for i in range(1, len(x) + 1):
    print(x[0:i])
print()

# 5
a = "ABC"
kq = ""
for i in range(len(a)):
    kq += a[i] + str(i + 1)
    print(kq)
print()

# 6
s = "ABCDE"
kq = len(s)
for i in range(kq):
    left = s[: (i + 1)]
    right = s[:i][::-1]
    print(" " * (kq - i - 1) + left + right)
print()

# 7
n = 5
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()
