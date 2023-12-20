num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
#############################################
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


n = int(input("enter the number:"))
count = 0
num = 2

while count < n:
    if is_prime(num):
        print(num, end=" ")
        count += 1
    num += 1
