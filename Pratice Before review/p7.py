add = lambda a,b:a+b
print(add(10,3))

min = lambda x,y:x if (x>y) else y
print(min(5,8))

list1=[1,2,3,476,87,34,23,21,23]
odd = list(filter(lambda num:(num %2 !=0),list1))
print(odd)