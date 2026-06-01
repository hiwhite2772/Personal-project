def main():
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    
    if n != len(ls):
        print("Error!")
        exit()
    ds = {}
    for i, x in enumerate(ls):
        need = k - x
        
        if need in ds:
            a, b = ds[need], i
            if a > b:
                a, b = b, a
            print(a, b)
            return
        ds[x] = i
main()