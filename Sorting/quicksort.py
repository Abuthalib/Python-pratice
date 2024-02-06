def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot = arr[len(arr)//2]
    left =[x for x in  arr if x < pivot]
    middle =[x for x in arr if x == pivot]
    right =[x for x in arr if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)

arr = [2,3,5,1,7,1,8,1,9,10]
print(quick_sort(arr))
