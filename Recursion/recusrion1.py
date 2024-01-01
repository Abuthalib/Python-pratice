def fun(count):
    if count > 5:
        return
    print(10)
    count += 1
    fun(count)


# un(1)


def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)


# countdown(5)


def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)


countdown(5)


def countdown(n):
    while n >= 0:
        print(n)
        n -= 1

countdown(5)
