def is_palindrome(x):

    return x ==x[::-1]

x=str(input("enter the value : "))
print(is_palindrome(x))
