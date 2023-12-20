# eg:1 parent and child class
class A:
    def m1(self):
        print("this is M1 method from class A")


class B(A):
    def m2(self):
        print("this is m2 method from class B")


obj = B()
obj.m2() #method m2 from class B
# obj.m1() #method m1 from class A

# eg:2 # single inheritance in another way

# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# obj = B()
# obj.m1()
# obj.m2()

# eg:3  multi level inheritance

# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)


# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()


# eg:4  Hierarchy Inheritance

# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)


# obj1 = B()
# obj2 = C()
#
# obj1.m1()
# obj1.m2()
#
# obj2.m1()
# obj2.m3()

# eg:5  Multiple inheritance

# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B:
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A, B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
#
# obj = C()
# obj.m1()
# obj.m2()
# obj.m3()


# eg:6 calling parent class method using child class using super()
# method override
# class A:
#     def m1(self):
#         print("this is m1 method from A class")
#
#
# class B(A):
#     def m1(self):
#         print("this is m1 method from class B")
#         super().m1()
#
#
# obj = B()
# obj.m1()
# #


# eg:7
# class A:
#     a, b = 10, 20
#
#
# class B(A):
#     i, j = 100, 200
#
#     def m1(self, x, y):
#         print(x + y)  # local variables
#         print(self.i + self.j)  # class variables
#         print(self.a + self.b)
#
#
# o = B()
# o.m1(10,3)

# eg:8  overriding variables
# class Parent:
#     name = "Abu"
#
#
# class Child(Parent):
#     name = "Thalib"  # overridding the variable  value
#
#     def test(self):
#         print(super().name)
#
#
# o = Child()
# o.test()
# print(o.name)


# eg:9  overriding  method
# class Bank:
#     def rateOfIntrest(self):
#         return 0
#
#
# class XBank(Bank):
#     def rateOfIntrest(self):
#         return 10
#
#
# class YBank(Bank):
#     def rateOfIntrest(self):
#         return 15
#
#
# obj1 = XBank()
# print(obj1.rateOfIntrest())
#
# obj2 = YBank()
# print(obj2.rateOfIntrest())

# eg:10  Method Overloading (ploymorphism)
# class Human:
#     def sayhello(self, name=None):
#         if name is not None:
#             print("hello " + name)
#         else:
#             print("Hello")
#
# h=Human()
# h.sayhello()
# h.sayhello("Abuthalib")


# eg:11 overloading (polymorphism)

# class Calculation:
#     def add(self, a=0, b=0, c=0):
#         print(a + b + c)
#
#
# cal = Calculation()
# cal.add()
# cal.add(10)
# cal.add(10, 20)
# cal.add(10, 20, 30)

# eg:12

# eg:13


# eg:14

# eg:15
