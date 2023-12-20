#Write a program to print the table of the given number using the generator.

def table(n):
    for i in range(1,11):
        yield  n*i
        i=i+1

for i in table(15):
    print(i)