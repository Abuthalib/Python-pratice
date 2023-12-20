class Abu:
    def __init__(self):
        print("this is constructor method")

    def my(self):
        print("this is normal method")

    def __del__(self):
        print("destructor method called")
        print("object deleted")


ob = Abu()
ob.my()
del ob
