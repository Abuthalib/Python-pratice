def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [10, 23, 1, 44, 5, 26, 90, 3]
bubble_sort(arr)

print("Sorted array:", arr)
