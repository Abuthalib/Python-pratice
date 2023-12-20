class first:
    def print(self):
        print("befor monkey patcing")


import monkey


def monkey_function(self):
    print("after monkey patching")


monkey.A.print = monkey_function
obj = monkey.A()
obj.print()
