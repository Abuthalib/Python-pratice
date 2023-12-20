# list comphersion
numbers =[1,2,3,4,5,6,7,8,9]

even =[i for i in numbers if i%2==0]
print(even)

sq =[i*i for i in numbers]
print(sq)

# lambda

add = lambda a, b: a + b
print(add(10, 3))

add = lambda x: x + 2
print(add(11))

prodcut = lambda a, b, c: a * b * c
print(prodcut(1, 2, 3))

# lambda to filter odd numbers

list1 = [32, 44, 33, 56, 77, 89, 12, 90]
even = list(filter(lambda num: (num % 2 == 0), list1))
print(even)

minimum = lambda x,y: x if (x<y) else y
print(minimum(100,20))