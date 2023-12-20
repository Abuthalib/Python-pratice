class Hey:
    def hey():
        print("hey")


class Mocked:
    def hey():
        print("you are mocked")

Hey.hey()

Hey = Mocked

Hey.hey()
