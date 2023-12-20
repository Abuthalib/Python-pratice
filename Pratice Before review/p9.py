class Hey:
    def hey():
        print("hey")
class Mocked:
    def hey():
        print("mocked!!!")

Hey.hey()

Hey = Mocked

Hey.hey()


def power(a,b):
    return a**b
def mock(a,b):
    return "mock power"
power = mock
print(power(2,4))
