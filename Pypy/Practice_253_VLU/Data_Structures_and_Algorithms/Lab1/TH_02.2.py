def binary_search(arr, key):
    mid = 0
    left = 0
    right = len(arr)
    step = 0
    while left <= right:
        step += 1
        mid = (left + right) // 2
        if (key == arr[mid]):
            return mid
        if key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
key = 29
result = binary_search(arr, key)
print(f"Vi tri tim kiem thu i la: {result}")
