# conditional statement
# if , if..else,elif
#############################
# person eligible for vote

age =15
if age >=18:
    print("eligible for vote")
else:
    print("not eligible for vote")
##############################
if True:
    print("its True")
else:
    print("false condition")

#####################
if 0:
    print("one")
else:
    print("Not one")

##############33333
# num =11
#
if num%2 == 0:
    print(" number is even")
else:
    print("odd number ")


############
# if, else in single line (ternary operator)
num = 10
print("Even Number") if num % 2 == 0 else print("odd number")

##############
# multiple statements in single line
a = 5
{print("hello"), print("Python")} if a >= 10 else {print("hello"), print("Abu")}


########################
# multiple condtion using : elif

weekno=5

if weekno ==1:
    print("sunday")
elif weekno ==2:
    print("monday")
elif weekno ==3:
    print("tuesday")
elif weekno ==4:
    print("wednesday")
elif weekno ==5:
    print("thursday")
elif weekno ==6:
    print("friday")
elif weekno ==7:
    print("saturday")
else:
    print("invalid choice")


