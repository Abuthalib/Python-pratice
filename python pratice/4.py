# monkey poaching
class Hey:

    def hey():
        print("hey")

class Mocked:
    def hey():
        print("you are mocked")

Hey.hey()
Hey = Mocked
Hey.hey()


def power(a,b):
  print(a**b)

def mock_power(a,b):
    print("mocked!!!!!!")


power(2,3)
power = mock_power
power(2,3)