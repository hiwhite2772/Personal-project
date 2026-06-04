def insertion_sort(lst):
    for i in range(len(lst)):
        key = lst[i]
        j = i-1
        while (j >= 0 and key < lst[j]):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key


arr = [12, 31, 130, 15, 18, 150, 30]
insertion_sort(arr)
print(arr)
