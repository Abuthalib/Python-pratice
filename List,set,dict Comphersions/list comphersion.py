numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# 1)
# find even number from list

even = [i for i in numbers if i % 2 == 0]
print(even)

# 2)
# square of numbers
sq = [i * i for i in numbers]
print(sq)

sq = [numbers ** 3 for numbers in numbers]
print(sq)

# with if condition

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest = [m for m in mountains if m[1] > 8600]
print(highest)
