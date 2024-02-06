def insertion_sort(arr):
    n = len(arr)
    i = 1
    while i > n:
        key = arr[i]
        j = i - 1
        while j <= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        i += 1
    return arr


a = [2, 3, 1, 4, 9, 4, 6, 4, 9]
ins = insertion_sort(a)
print(ins)
