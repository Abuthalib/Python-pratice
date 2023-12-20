class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return "hi,its me" ,self.name


class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        print(super().greet(), "i am a", self.job_title)


emp = Employee("Abu", 23, "pythondeveloper")
emp.greet()
P1 = Person("Abuthalib", 23)
P1.greet()
P2 = Person("jebi", 22)
P2.greet()
print(Person.counter)
