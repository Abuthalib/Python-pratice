def bubble_sort(a):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j] ,arr[j+1] = arr[j+1],arr[j]
    return arr
arr = [64,25,12,22,11]
print("orginal array :",arr)

bubble_sort(arr)
print("Sorted array:",arr)