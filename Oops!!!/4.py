# static method
class Myclass:
    def m1(self):
        print("this is instence method")

    @staticmethod
    def m2(self, num):
        print(self, num)


mc = Myclass()
mc.m1()
mc.m2(100, 200)
Myclass.m2(10, 20)


# constructor
# req: Eployee
# constructor : eid,ename,sal
# display():print eid,ename & sal
#
class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display(self):
        print(self.eid, self.ename, self.sal)

    def __str__(self):
        return self.ename


e1 = Emp(101, "Abuthalib", 60000)
e1.display()

e2 = Emp(102, "jebi", 8000)
e2.display()

print(e2)
