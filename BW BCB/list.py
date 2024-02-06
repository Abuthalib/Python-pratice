#D
arr.pop(0)
print(arr)
print()
#slicing
print("slicing \n")
x = list(range(0,30,2))
print(x)

print(x[0:10:2])
print(x[10:20:])
print(x[::-1])
print()
#searching
print("searching\n")
x = list(range(0,1000,2))
print(x[0:10])

s = 777
for i in range(len(x)):
    if x[i] == s:
        print("element found at index : ",i)
   
#sorting
print()
print("Sort \n")
x = list(range(0,10))
print(x)
print(sorted(x))
x.sort(reverse = True)
print(x)
