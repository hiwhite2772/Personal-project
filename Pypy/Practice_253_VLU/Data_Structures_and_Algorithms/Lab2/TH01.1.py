def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
arr = [120, 35, 60, 42, 280, 7, 15, 19]
print(bubble_sort(arr))