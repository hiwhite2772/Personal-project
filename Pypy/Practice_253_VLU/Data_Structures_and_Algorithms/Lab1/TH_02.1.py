def binary_search(array, element):
    mid = 0
    start = 0
    step = 0
    end = len(array)
    
    while start <= end:
        step += 1
        mid = (start + end) // 2
        
        if array[mid] == element:
            return mid
        
        if array[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    return -1

array = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
element = 28
result = binary_search(array, element)
print(f"Phan tu tim kiem duoc la: {result}")