def my_decorator(func):
    def wrapper():
        print("before the function is called")
        func()
        print("after the function is called")

    return wrapper


@my_decorator
def say_hello():
    print("hello!!")

@my_decorator
def Hey():
    print("Hey!!!")


say_hello()
Hey()


##########################

def uppercase(func):
    def wrapper(text):
        return func(text.upper())

    return wrapper


@uppercase
def greet(name):
    return "Hello", name


print(greet("abuthalib"))
print(greet("mehjabeen"))
