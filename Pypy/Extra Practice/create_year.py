def can_make(cnt):
    target = [2, 0, 2, 6]
    def dfs(pos):
        if pos == 4:
            return True
        
        need = target[pos]

        #Cách 1: Dùng trực tiếp
        if cnt[need] > 0:
            cnt[need] -= 1
            if dfs(pos + 1):
                return True
            cnt[need] += 1
        #Cách 2: ghép 2 chữ số
        for a in range(10):
            for b in range(a, 10):
                if a == b and cnt[a] < 2:
                    continue
                if a != b and (cnt[a] == 0 or cnt[b] == 0):
                    continue
                
                #Thử cộng
                if a + b == need:
                    cnt[a] -= 1
                    cnt[b] -= 1
                    if dfs(pos + 1):
                        return True
                    cnt[a] += 1
                    cnt[b] += 1
                #Thử trừ
                if abs(a - b) == need:
                    cnt[a] -= 1
                    cnt[b] -= 1
                    if dfs(pos + 1):
                        return True
                    cnt[a] += 1
                    cnt[b] += 1
        return False
    return dfs(0)
i = int(input("Nhap so lan: "))
for _ in range(i):
    cnt = list(map(int, input("Nhap so nguyen (10 so nguyen): ").split()))
    print("ket qua: YES" if can_make(cnt) else "ket qua: NO")