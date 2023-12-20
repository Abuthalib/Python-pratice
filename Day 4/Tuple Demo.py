# Eg:1 creation of tuple
# mytuple =("A","B","C")
# print(mytuple)
# mytuple=()

# eg:2 access tuple items
# mytuple =("apple","banana","cherry")
# print(mytuple[1])

# eg:3 range of indexes
# tuple =("apple","banana","cherry","orange","grapes")
# print(tuple[2:5])
# print(tuple[-4:-1])

# Eg:4 chnage tuple values
"""
directly not possible to modify so we can achive it through indirect way
tuple -->list(modify) ---> tuple
"""
# tuple1 = ("apple", "banana", "cherry")
# list1 = list(tuple1)
# list1[0] = "orange"
#
# tuple1 = tuple(list1)
# print(tuple1)

#eg :5 reading tuple items loop

# tuple1 = ("apple", "banana", "cherry")
# for i in tuple1:
#     print(i)

#eg:6 check tuple item

# tuple1 = ("apple", "banana", "cherry")
# if "apple" in tuple1:
#     print("yes")
# else:
#     print("Np")

# eg:7 count or length
# tuple1 = ("apple", "banana", "cherry")
# print(len(tuple1))

#eg :8  add item into tuple
"""
its not possible but  we can use indirect way
tuple ---> list(modify) ---> tuple
"""
#eg:9 copying tuple
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = tuple1
# print(tuple2)

#eg :10 removing items from tuple
"""
its not possible but  we can use indirect way
tuple ---> list(modify) ---> tuple
using del tuple we can delete tuple
del tuple1
"""

# eg:11 join/combin

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = ("A","B")
# tuple3= tuple1+tuple2
# print(tuple3)

#eg:12 comparsion

tuple1 = ("apple", "banana", "cherry")
tuple2 = ("A","B")

if tuple1 ==tuple2:
    print("its equal")
else:
    print("its not equal")