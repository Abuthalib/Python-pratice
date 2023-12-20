# Eg:1 create set
# myset = { "apple","banana","cherry"}
# print(myset)

# Eg:2 Accessing items from set
# myset = { "apple","banana","cherry"}
# for i in myset:
#     print(i)

# eg:3 if the value exist
# myset = { "apple","banana","cherry"}
#
# print("apple" in myset)
#
# print("apple1" in myset)

# eg :4 adding item to set
# add ()  update()
#add()
# myset = { "apple","banana","cherry"}
# myset.add("orange")
# print(myset)

#update
# myset = { "apple","banana","cherry"}
# myset.update(["mango","orange"])
# print(myset)

# # eg:5 length of set
# myset = { "apple","banana","cherry"}
# print(len(myset))

#eg:6 remove item or discard from set
# remove() and discard()
#remove
# myset = { "apple","banana","cherry"}
# myset.remove("banana")
# print(myset)


#discrad()
# myset = { "apple","banana","cherry"}
# myset.discard("banana")
# print(myset)

#myset = { "apple","banana","cherry"}
#myset.discard("abcd")
# it doesnt throw any error but remove will throuw error

#eg :7 clear all item from set

# myset = { "apple","banana","cherry"}
# myset.clear()
# print(myset)

# del
# myset = { "apple","banana","cherry"}
# del myset
# print(myset)

#eg:8  joining 2 set  - union()
# set1 = { "apple","banana","cherry"}
# set2 ={"A","B","C"}
# set3=set1.union(set2)
# print(set3)

#update()

set1 = { "apple","banana","cherry"}
set2 ={"A","B","C"}
set1.update(set2)
print(set1)






























