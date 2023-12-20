def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper


@my_decorator
def Hey():
    print("Hey!!!")


Hey()


def uppercase(func):
    def wrapper(text):
        return  func(text.upper())
    return wrapper
@uppercase
def display(name):
    return name

print(display("Abuthalib"))
