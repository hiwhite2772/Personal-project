# #Số nguyên tố gần nhất
#cách 1
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_gan_nhat(n):
    #Số nguyên tố lớn hơn
    down = n - 1
    while n >= 2:
        if la_nguyen_to(down):
            break
        down -= 1
    
    #Số nguyên tố nhỏ hơn
    up = n + 1
    while True:
        if la_nguyen_to(up):
            break
        up += 1

    #So sánh khoảng cách
    if (n - down) <= (up - n):
        return down
    else:
        return up

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if la_nguyen_to(n):
            print("YES", tim_gan_nhat(n))
        else:
            print("NO")

main()

#Cách 2 - Tối ưu nhanh
t = int(input())
arr = [int(input()) for _ in range(t)]

sntgn = max(arr) + 5

is_prime = [True] * sntgn
is_prime[0] = is_prime[1] = False

for i in range(2, int(sntgn ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, sntgn, i):
            is_prime[j] = False

def tim_gan_nhat(n):
    down = n - 1
    while down >= 2 and not is_prime[down]:
        down -= 1
    
    up = n + 1
    while up < sntgn and not is_prime[up]:
        up += 1

    if (n - down) <= (up - n):
        return down
    else:
        return up
    
for i in arr:
    if is_prime[i]:
        print("YES", tim_gan_nhat(i))
    else:
        print("NO")

#Cách 3
from math import sqrt
def la_nguyen_to(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def tim_gan_nhat(n):
    d = n - 1
    while not la_nguyen_to(d):
        d -= 1

    u = n + 1
    while not la_nguyen_to(u):
        u += 1
    
    if (n - d) <= (u - n):
        return d
    else:
        return u

t = int(input())
for _ in range(t):
    n = int(input())
    if la_nguyen_to(n):
        print("YES", tim_gan_nhat(n))
    else:
        print("NO")