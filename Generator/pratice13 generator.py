def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in fib():
    if f > 50:
        break
    print(f, end=" ")


#########multiplication table##############

def table(n):
    for i in range(1, 11):
        yield n * i
        i = i + 1


n = 10
for i in table(n):
    print(i)
