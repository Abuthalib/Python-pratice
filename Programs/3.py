# Python Program for factorial of a number

def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


num = 5
print("factprial of", num, "is : ", fact(num))
