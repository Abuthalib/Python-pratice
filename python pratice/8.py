add = lambda a,b :a+b
print(add(10,3))

product = lambda x,y,z:x*y*z
print(product(10,1,2))

list1 =[1,2,3,4,5,6]
odd = list(filter(lambda num:(num %2 !=0),list1))
print(odd)

min = lambda x,y: x if(x < y) else y
print(min(11,2))