# Using a recursive function to calculate the sum of a sequence

def sum(n):
    if n>0:
        return n+sum(n-1)
    return 0


result = sum(10)
print(result)
