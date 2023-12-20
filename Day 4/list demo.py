#example 1

# mylist =[10,20,30,4,5.5]
# mylist2 =["apple","banana","cherry"]
# mylist3 =["apple",10,7.5]
# mylist4=list()
#
#
# print(mylist)
# print(mylist2)
# print(mylist3)
# print(mylist4)

# eg:2 accesing item from list

# mylist =["apple","banana","cherry"]
# print(mylist[-1])
# print(mylist[0])

# eg:3 range of list
# mylist =["apple","banana","cherry","orange","kiwi"]
# print((mylist[2:5]))
# print(mylist[-3:-1])

# eg:4 change item value
# mylist =["apple","banana","cherry"]
# print(mylist)
#
# mylist[0]="orange"
# print(mylist)

# eg:5  read items using loop statement

# eg:6 check the item is present
# mylist =["apple","banana","cherry"]
# if "apple" in mylist:
#     print("Yes")
# else:
#     print("No")

#eg:7 count of items or length of list
# mylist =["apple","banana","cherry"]
# print(len(mylist))

#eg:8 add items
#adppend() insert()

#append()

# mylist =["apple","banana","cherry"]
# mylist.append("orange")
# print(mylist)

# insert()
# mylist =["apple","banana","cherry"]
# mylist.insert(1,"orange")
# print(mylist)

# eg:9 remove item from list

# pop()
# mylist =["apple","banana","cherry"]
# mylist.pop(0)
# print(mylist)

#del
# mylist =["apple","banana","cherry"]
# del mylist[1]
# print(mylist)

#clear()

# mylist =["apple","banana","cherry"]
# mylist.clear()
# print(mylist)

#eg:10 copy list
# list()
# mylist =["apple","banana","cherry"]
# mylist2 = list(mylist)
#
# print(mylist)
# print(mylist2)

#copy()

# mylist =["apple","banana","cherry"]
# mylist2=mylist.copy()
# print(mylist)
# print(mylist2)

#eg:11 combine/join list

# using + operator
# mylist =["apple","banana","cherry"]
# mylist2 =["orange","grapes"]
# mylist3 = mylist + mylist2
# print(mylist3)

# using loop
# mylist =["apple","banana","cherry"]
# mylist2 =["orange","grape"]
# for i in mylist2:
#     mylist.append(i)
#
# print(mylist)

# extend ()
# list1 =["apple","banana","cherry"]
# list2 =["A","B"]
# list1.extend(list2)
# print(list1)