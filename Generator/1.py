def Fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in Fib():
    if f > 50:
        break
    print(f, end=" ")


def table(n):
    for i in range(1, 11):
        yield n * i
        i = i + 1


for i in table(10):
    print(i)
