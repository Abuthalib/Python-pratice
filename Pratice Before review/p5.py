def fib():
    a,b =0,1
    while True:
        yield a
        a,b=b,a+b

for i in fib():
    if i >50:
        break
    print(i, end=" ")


def table(n):
    for i in range(1,11):
        yield  n*i
        i=i+1

n=10
for i in table(n):
    print(i)
