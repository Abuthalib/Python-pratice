def is_palindrome(string):
    return string == string[::-1]


string = input("enter the string :")

if is_palindrome(string):
    print("the string is palindrome")
else:
    print("its not palindrome")
