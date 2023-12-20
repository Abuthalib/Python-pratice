# eg :1
#
class MyClass:
    def func(self):
        pass

    def display(self,name):
        print(name)


mc1=MyClass()
mc1.func()
mc1.display("ABU")

# eg :2
class MyClass:
    def m1(self):
        print("this is instence method")

    @staticmethod
    def m2(self, num):
        print(self, num)


mc = MyClass()
mc.m1()
mc.m2(100, 200)
MyClass.m2(10, 20)
# eg:3
class MyClass:
    a,b=10,20 # class variables

    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a * self.b)

mc=MyClass()
mc.add()
mc.mul()

# eg:4
# i, j = 15, 25  # global variables
#
#
# class MyClass:
#     a, b = 10, 20  # class variables
#
#     def add(self, x, y):  # x and y here is local variables
#         print(x + y)  # x,y are local variable we can simply acces
#         print(self.a + self.b) # a,b are class variable we can acces using self keyword
#         print(i+j)  # i and j is global variable so we can acess evry where
# mc=MyClass()
# mc.add(100,200)


# eg:5
# a, b = 15, 25  # global variables
#
#
# class MyClass:
#     a, b = 10, 20  # class variables
#
#     def add(self, a, b):
#         print(a+b )  # local
#         print(self.a +self.b) # class variables
#         print(globals()['a']+globals()['b']) # global varaiables
#
#
# mc = MyClass()
# mc.add(100, 200)

# eg:6  one class can have multiple object

# class MyClass:
#     def display(self,name):
#         print("this is display method")
#         print(name)
#
# obj1 = MyClass()
# obj1.display("Abu")
#
# obj2 = MyClass()
# obj2.display("Thalib")


# eg:7   Constructor

# class MyClass:
#     def __init__(self):
#         print("this is constructor")
#
#     def m1(self):
#         print("hello...")
#
#     def m2(self, x, y):
#         return (x + y)
#
#
# mc = MyClass()  # this invoke/call constructor automatically
# mc.m1()  # method we have to call explicitly by using object
# print(mc.m2(10, 20))


# eg:8
# class MyClass:
#     name="abu"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
# mc=MyClass("Thalib") # passing parameter to the constructor

# eg:9
# req: Eployee
# constructor : eid,ename,sal
# display():print eid,ename & sal
# class Emp:
#     def __init__(self, eid, ename, sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#
#     def display(self):
#         print(self.eid, self.ename, self.sal)
#
#
# e1 = Emp(103, "Abuthalib", 60000)
# e1.display()
#
# e2 = Emp(113,"Mehjebeen",80000)
# e2.display()


# eg:10
# req: Eployee
# constructor : eid,ename,sal
# constructor:print eid,ename & sal

# class Emp:
#     def __init__(self, eid, ename, sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#
#     def __str__(self):
#         return (self.ename)
#
#
# e1 = Emp(103, "Abuthalib", 60000)
# print(e1)
# e2 = Emp(113, "Mehjebeen", 80000)
# print(e2)