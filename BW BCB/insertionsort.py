def Insertion_sort(arr):
    n = len(arr)
    i =1
    while i < n:
        key = arr[i]
        j = i-1
        while j >=0  and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        i+=1
arr =[1,2,3,4,5,6,2,3,1,5,4,2,6,7]
Insertion_sort(arr)
print(arr)