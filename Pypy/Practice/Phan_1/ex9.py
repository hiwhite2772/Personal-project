#1
def main():
    while True:
        n = int(input())
        arr = list(map(int, input().split()))

        if len(arr) == n:
            break
        else:
            print(f"Khong khop voi {n} phan tu!")

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(*arr)


if __name__ == "__main__":
    main()

#2
def main():
    while True:
        n = int(input())
        arr = list(map(int, input().split()))

        if len(arr) == n:
            break
        else:
            print(f"Khong khop voi {n} phan tu!")
    arr.sort(key=lambda x: (abs(x), x))
    
    print(*arr)


if __name__ == "__main__":
    main()

#3
def main():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    matrix.sort(key=lambda row: sum(row))
    
    col_info = []
    
    for col in range(m):
        col_sum = 0
        for row in range(n):
            col_sum += matrix[row][col]
        col_info.append((col_sum, col))
    
    col_info.sort()
    new_order = []
    
    for _, col_index in col_info:
        new_order.append(col_index)
    
    new_matrix = []
    for row in matrix:
        new_row = []
        
        for col_index in new_order:
            new_row.append(row[col_index])
        new_matrix.append(new_row)
    
    for row in new_matrix:
        print(*row)


if __name__ == "__main__":
    main()
