def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 2) + fib(n - 1)


n = 5
print(fact(n))
print(sum(n))
print(fib(n))
