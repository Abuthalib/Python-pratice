# eg1:
#
# print("this is starting point of program....")
# print("this is starting point of program....")
# print("this is starting point of program....")
# try:
#     print(x)
# except:
#     print("exception occured")
#
# print("this is end of program")
# print("this is end of program")
# print("this is end of program")

# eg :2

# print("start")
# print("pgm in progress")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("cant divded by zero")
# print("completed!")


# eg:3 multiple except block [try -- except--else --finally]
# try:
#     num1, num2 = 10, 5
#     result = num1 / num2
#     print("result is : ", result)
# except ZeroDivisionError:
#     print("zero division Errror occured..")
# except SyntaxError:
#     print("Syntax error exception..")
# except:
#     print("exception handled..")
# else:
#     print("No exception")
# finally:
#     print("always execute...")

# eg:4 raising our own exception

def enterage(num):
    if num < 0:
        raise ValueError("only integers are allowed")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


print("checking even or odd")
num = -1
try:
    enterage(num)
except ValueError:
    print("value error exception occured and handled")
print("completed!!")
