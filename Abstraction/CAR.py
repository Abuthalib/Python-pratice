#from abc import ABC, abstractmethod


class Car():
    def milage(self):
        pass


class Tesla(Car):
    def milage(self):
        print(" tesla = 20 kmph")


class Suzuki(Car):
    def milage(self):
        print("Suzuki = 30 kmph")


class Duster(Car):
    def milage(self):
        print("duster = 25 kmph")


t = Tesla()
t.milage()

s = Suzuki()
s.milage()

d = Duster()
d.milage()
