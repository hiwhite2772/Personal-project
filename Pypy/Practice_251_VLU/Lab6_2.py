def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

while True:
    try:
        n = int(input("Nhập số nguyên n = "))
        if 0 < n < 100: break
    except: pass
    print("Vui lòng nhập lại!")

print(f"{n} là số nguyên tố." if is_prime(n) else f"{n} không phải là số nguyên tố.")

primes = [i for i in range(1, n+1) if is_prime(i)]
print("Số nguyên tố từ 1 đến", n, "là:", primes)
print("Số lượng:", len(primes))
print("Tổng:", sum(primes))
