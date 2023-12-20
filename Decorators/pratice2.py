def uppercase(func):
    def wrapper(text):
        return func(text.upper())

    return wrapper


@uppercase
def greet(name):
    return "hello", name


print(greet("abu"))
print(greet("jebi"))
