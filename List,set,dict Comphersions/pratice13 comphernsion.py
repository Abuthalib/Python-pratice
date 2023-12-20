numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = [i for i in numbers if i % 2 == 0]
print("even", even)

odd = [i for i in numbers if i % 2 != 0]
print("odd", odd)


sq = [i**2 for i in numbers]
print("square",sq)



mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

hight = [m for m in mountains if m[1]>8600]
print(hight)