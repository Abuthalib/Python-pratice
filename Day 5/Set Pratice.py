"""
set is a collection of non-repetitive elements:
sets are unordered
set are un indexed
there is no way to change the elements in set
cannot contain duplicate value

"""
mySet = {1,3,4}
mySet.add(45)
mySet.add(1)
print(len(mySet))

mySet = {1,3,4}
mySet.add(45)
mySet.add(1)
mySet.add("1")
print(mySet)
mySet.remove(45)
print(mySet)

print(mySet.pop())
print(mySet)

s ={1,2,3}
t ={1,2,3,4,5,6,}
print(s.union(t))

print(s.intersection(t))