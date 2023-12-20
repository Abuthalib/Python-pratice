def Fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in Fib():
    if f > 50:
        break
    print(f, end=" ")

