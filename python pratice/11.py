dict1 = {'apple': 50, 'banana': 20, 'orange': 80, 'grapes': 30}
dict2 = {'apple': 30, 'banana': 60, 'orange': 40, 'kiwi': 70}

intersection = {}

for key in dict1.keys():
    if key in dict2:
        intersection[key] = dict1[key] + dict2[key]

print("Intersection of the two dictionaries:", intersection)

# prime

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

    # n primes


def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


n = 10  # number of primes to find
count = 0  # count of primes found
num = 2  # start with the first prime number

print("The first", n, "prime numbers are:")
while count < n:
    if is_prime(num):
        print(num, end=" ")
        count += 1
    num += 1
