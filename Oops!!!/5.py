# exception handling (try except else finally)
print("this is starting point of program....")
print("this is starting point of program....")
print("this is starting point of program....")

try:
    print(x)

except:

    print("exception occurred")

print("this is end of program")
print("this is end of program")
print("this is end of program")
x = 100


def cool():
    global x
    x = 500
    print(x)


cool()


# monkeypatching

def power(a, b):
    return a ** b


def mock_powe(a, b):
    return "mocked!!!!!!"


power = mock_powe

print(power(2, 4))
