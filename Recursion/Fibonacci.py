def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1) + fib(num - 2)


num_terms = 1
if num_terms <= 0:
    print("please enter valid positive number")
else:

    print("The fibonaci series  ara :")

for i in range(num_terms):
    print(fib(i))
