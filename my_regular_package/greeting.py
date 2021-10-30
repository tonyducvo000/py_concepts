#  simple module to demonstrate usage of user defined package
class greetings():
    def __init__(self, name):
        self.name = name

    def printHello(self):
        print(f"Hello {self.name}, from the user defined package!")

