class RemoteControl:
    def __init__(self):
        self.channels = ["HBO", "CNN", "ABC", "POGO", "ESPN"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]


r = RemoteControl()
itr = iter(r)
# for a in RemoteControl():
#     print(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

