# Python program to check if a string is palindrome or not
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("yes")
else:
    print("No")

x = "malayalam"
w = ""
for i in x:
    w = i + w
if (x == w):
    print("yes")
else:
    print("No")
