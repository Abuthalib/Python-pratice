class Employee:
    __count = 0

    def __init__(self):
        Employee.__count = Employee.__count + 1

    def display(self):
        print("thr numbers of employee", Employee.__count)


emp = Employee()
emp2 = Employee()

emp.display()
