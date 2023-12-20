add = lambda a, b: a + b
print(add(4, 9))

sum = lambda x: x + 10
print(sum(90))

product = lambda x, y, z: x * y * z
print(product(10, 20, 0))

list1 = [1, 2, 3, 476, 87, 34, 23, 21, 23]
odd = list(filter(lambda num: (num % 2 != 0), list1))
print(odd)

Min = lambda x, y: x if (x < y) else y
print(Min(50, 88))
