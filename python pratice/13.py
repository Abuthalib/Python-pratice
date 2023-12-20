dict1 = {'apple': 50, 'banana': 20, 'orange': 80, 'grapes': 30}
dict2 = {'apple': 30, 'banana': 60, 'orange': 40, 'kiwi': 70}

inter = {}

for key in dict1.keys():
    if key in dict2:
        inter[key] = dict1[key] + dict2[key]
print(inter)

##########
num = 10
if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not prime")
            break
    else:
        print(n, "is prime")
else:
    print(num, "is not prime")


############
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % 2 == 0:
            return False
    return True

n=11
count =0
num =2

while count <n:
    if is_prime(num):
        print(num, end=" ")
        count +=1
    num +=1
