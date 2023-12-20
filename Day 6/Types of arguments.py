# eg:1
# def func(i,j):
#     print(i,j)
# func(10,20) # positional arguments
# func(j=20,i=30) #keyword argument

# eg:2  default value asigned to positional argument

# def func(i, j=10):
#     print(i, j)
#
#
# func(100, 200)
# func(100)

# # eg:3 key word arguments
# def greetings(name,greetmsg):
#     print(greetmsg+" "+name)
#
# greetings(name="Abu",greetmsg="Hello")

# eg:4
# def func(a,b,c):
#     print(a,b,c)
#
# func(10,20,30)
# func(a=10,b=20,c=30)
# func(b=20,a=10,c=30)
# func(10,20,c=30)
# func(10,b=20,c=30)
# func(10,b=20,30) this is wrong because positional argument must come before any key word argument
# func(10,30,b=20)  this haves logical error

# eg:5
def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


res = largest(10,20)
print(res) # it is in tuple collection

# eg:6


# eg:7
