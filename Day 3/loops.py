# while loop

""""
while condition:
    #body of loop

The block repeats executing until the condition is true

In  while loop  the condition is checked first .If it evaluates to true the body of loop is executed otherwise not!
if the  loop is entered the process of [condition check and execution] is continued until the condition becomes False
"""
a = 0
while (a < 100):
    print(a, end=" ")
    a += 1

a = [1, 2, 3, 4, 5, "Apple"]
i = 0
while (i < len(a)):
    print(a[i])
    i += 1

# for Loop
"""
for loop is used  to iterate through a sequence  like list,tuple or string [iterables]
The range function in python is used to generate a sequence  of number
We can also specify the start,stop and step-size  as follow : (start,stop,step_size)


"""
for i in range(10, 34):
    print(i, end=" ")
print()

for i in range(len(a)):
    print(a[i], end=",")

print()

for item in a:
    print(item, end=" ")

# for  loop with else
l = [1, 2, 3, 4]
for i in l:
    print(i)
else:
    print("done")

# The Break Statement and continue
"""
"Break is used to come out the loop when encountered
It instruct the program to Exit the loop now

"continue" is used to come out from particular iteration/step
is instruct the program to Stop the current iteration and execute the next iteration
"""

for i in l:
    print(i)
    if i == 3:
        break
print("Loop exited")


# Continue State ment

for i in l:
    print(i)
    if i == 3:
        continue
    print("done this iteration for",i)
print("executed")