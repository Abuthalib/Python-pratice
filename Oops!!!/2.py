# overrriding
class A:
    def m1(self):
        print("this is m1 method from A class")


class B(A):
    def m1(self):
        print("this is m1 method from class B")
        super().m1()

obj =B()
obj.m1()


class Parent:
    name = "Abu"


class child(Parent):
    name = "Thalib"

    def test(self):
        print(super().name)

o= child()
o.test()
print(o.name)
##################################
class Bank:
    def intrest(self):
        return 0


class XBank(Bank):
    def intrest(self):
        return 10


class YBank(Bank):
    def intrest(self):
        return 15


ob1 = XBank()
print(ob1.intrest())

ob2 = YBank()
print(ob2.intrest())
