# overloading (polymorphism)
class Human:
    def say(self,name=None):
        if name is not None:
            print("hello ",name)
        else:
            print("hello")

h =Human()
h.say()
h.say("Abuthalib")


class Calculation():
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


cal = Calculation()
cal.add()
cal.add(10)
cal.add(10, 20)
cal.add(10, 20, 30)
