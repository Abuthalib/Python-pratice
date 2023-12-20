def Arraysum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum


arr = [1, 2, 3, 4, 5]

ans = Arraysum(arr)

print("sum of array is ",ans)
print(max(arr))


