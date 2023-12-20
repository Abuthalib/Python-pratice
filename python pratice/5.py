def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper


@my_decorator
def say_hello():
    print("hello!!!!!")


say_hello()


def uppercase(func):
    def wrapper(text):
        return func(text.upper())

    return wrapper

@uppercase
def greet(name):
    return " hello ",name

print(greet("Abuthalib"))

