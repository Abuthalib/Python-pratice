my_list = [1, 11, 34, 55, 33, 56, 77, 86, 5, 5, 42, 65, 75, 1, 4, 3, 6]
dic = dict.fromkeys(my_list)
un = list(dic.keys())
print(un)

nested = [[1, 2], [3, 4, 5], [6, 7]]
new = [item for sublist in nested for item in sublist]
print(new)

keys = ["a", "b", "c"]
values = [["apple", "apricot"], ["bat", "ball"], ["cat", "cow"]]

di = {}
for key, value in zip(keys, values):
    if key in di:
        di[key].append(value)
    else:
        di[key] = value

print(di)

d = {"a": 10, "b": 2, "c": 3}
maxkey = None
maxvalue = float('-inf')
for key, value in d.items():
    if value > maxvalue:
        maxvalue = value
        maxkey = key
print(maxkey)


def uppercase(func):
    def wrapper(text):
        return func(text.upper())

    return wrapper
@uppercase
def hello(name):
    return "hello ",name

print(hello("abu"))


def fib():
    a,b =0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib():
    if  f>50:
        break
    print(f,end=" ")
print()

class Remote:
    def __init__(self):
        self.channels =["HBO","CNN","BBC"]
        self.index =-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r = Remote()
itr = iter(r)

print(next(itr))
print(next(itr))

min = lambda x,y: x if (x<y) else y
print(min(12,4))

numbers =[1,2,3,4,5,6,7,8,9]
even =[i for i in numbers if i %2==0]
print(even)