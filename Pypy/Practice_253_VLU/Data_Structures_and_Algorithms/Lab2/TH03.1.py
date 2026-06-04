def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if lst[j] < lst[min_i]:
                min_i = j
        lst[i], lst[min_i] = lst[min_i], lst[i]
    return lst

arr = [140, 25, 15, 52, 10, 250, 55]

print(selection_sort(arr))