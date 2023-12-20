# s = "welcome"
# s = str("welcome")
#name = str()
#name =""

""""
mutable  - can change the value of the variables

immutable0 cannot change the value of the variables

strings are immutable
"""

# str1="welcome"
# print(id(str1))
# str1= str1+"python"
# print(id(str1))

# if values change after updation then it is immutable

##############################
# + and * with string
# str="welcome"
# print(str+"ABU")
#
# print(str*2)

##############################
# string slicing

# str = "Hello World"
# print(str[0:5])
# print(str[6:])
# print(str[0:-1])
# print(str[0:-2])
# print(str[-3:])
###########################
# ord() and chr()
#
# print(ord('A'))
# print((chr(65)))

###########################
# max() min () len()

# print(max("abc"))
# print(min("abc"))
# print(len("welcome"))


##########################
# s="welcome"
# print("come" in s)
# print(("lome" not in s))
#
# print("tim"=="tip")
# print("tin"!="tip")
#
# print(s.isalnum())
# print(s.isalpha())
# print("2021".isdigit())

####################################
# searching for substring
# s="welcome to python"
# print(s.endswith("thon"))
#
# print(s.startswith("good"))
#
# print(s.find("come"))
# print(s.find("abu"))
#
# print(s.count("o"))

#########################
# reversing a string
# method 1
# s = "welcome"
# rev_str =""
# for i in s:
#     rev_str=i+rev_str
# print("reversed string is :",rev_str)

# method 2
s="welcome"
rev=s[::-1]
print(rev)