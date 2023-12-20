class Recur:
    def fact(self, n):
        if n == 0:
            return 1
        else:
            return n * self.fact(n - 1)

    def sum(self, n):
        if n == 1:
            return 1
        else:
            return n + self.sum(n - 1)

    def fib(self, n):
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


r = Recur()
n =5

print("factorial of ",n," :", r.fact(n))
print("fibinocci of",n," :", r.fib(n))
print("sum of",n," :", r.sum(n))
