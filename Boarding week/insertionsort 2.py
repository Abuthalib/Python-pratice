def insertion_sort(arr):
    n = len(arr)
    i =1
    
    while i < n :
        key = arr[i]
        j = i-1

        while j >=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        i+=1
    return arr

arr=[3,2,4,15,1,56,2]
sort = insertion_sort(arr)
print(sort)