add=lambda a,b:a+b
print(add(10,20))

add = lambda x: x+100
print(add(50))

print((lambda a,b:a*b)(3,5))

product = lambda x,y,z:x*y*z
print(product(z=5,x=10,y=10))

#code to filter the odd numbers from list
list_ =[34,12,43,21,64,55,75,13,88,63]

odd_list=list(filter(lambda num:(num%2!=0),list_))

print(odd_list)

#minimum of a number

Minimum = lambda x, y: x if (x < y) else y
print(Minimum(35, 21))


import  calendar
s= calendar.prcal(2023)
