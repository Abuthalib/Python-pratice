class Hey:
    def hey():
        print("hey")


class Mocked:
    def hey():
        print("you are mocked")


Hey.hey()
Hey = Mocked
Hey.hey()


# monkey patching with function


def power(a, b):
    return a ** b


def mock_power(a, b):
    return "mocked power"


power = mock_power
print(power(2, 4))
