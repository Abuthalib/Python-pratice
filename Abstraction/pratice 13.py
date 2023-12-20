class Employee:
    __count = 0

    def __init__(self):
        Employee.__count = Employee.__count + 1

    def display(self):
        print("the numbers of employee :", Employee.__count)


emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp1.display()
