l1=[1,4,6,7,8]
l2 = [3,5,7,8,9]
list3 = l1+l2


def merge_sort(list3):
    if len(list3) > 1:
        mid = len(list3)//2
        left = list3[:mid]
        right =list3[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i=j=k=0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list3[k] = left[i]
                i+=1
            else:
                list3[k] = right[j]
                j+=1
            
            k+=1
        
        while i  < len(left):
            list3[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            list3[k] = right[j]
            j+=1
            k+=1
            
    else:
        return list3
    
    return list3
    
a = merge_sort(list3)
print(a)