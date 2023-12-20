import sys
sys.path.append("C:/Users/ABUTHALIB/Desktop/Python_praticals/Day 9/PackA")
sys.path.append("C:/Users/ABUTHALIB/Desktop/Python_praticals/Day 9/PackB")

#apprch1
# import emp
# eobj = emp.Employee(101,"Abu",80000)
# eobj.displayemp()
#
#
# import stu
# sobj= stu.Student(103,"jebi","A+")
# sobj.displaystu()


#aproch2
from emp import *
from stu import *

objE=Employee(102,"Thalib",60000)
objE.displayemp()

objs= Student(104,"Meh","A")
objs.displaystu()

