def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


res = is_palindrome("Abuthalib")
res1 = is_palindrome("Malayalam")
print(res)
print(res1)


# recursion
def is_recpalindrome(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_recpalindrome(word[1:-1])


res = is_recpalindrome("ababba")
print(res)
