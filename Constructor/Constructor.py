class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def info(self):
        print(self.name, "is a", self.role)


a = Person("Abuthalib", "developer")
b = Person("jebi", "psychologist")
a.info()
b.info()
