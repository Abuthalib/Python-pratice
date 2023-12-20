def multiple_yield():
    str1="First string"
    yield  str1

    str2 = "second string"
    yield  str2

    str3 = "third string"
    yield  str3

obj = multiple_yield()

print(next(obj))
print(next(obj))
print(next(obj))