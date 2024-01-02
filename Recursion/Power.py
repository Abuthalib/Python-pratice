def power(num, pow):
    if pow == 0:
        return 1
    else:
        return num * power(num, pow - 1)


res = power(2, 6)
print(res)
