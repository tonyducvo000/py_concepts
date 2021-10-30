#  simple module to demonstrate usage of user defined package
class Bye():
    def __init__(self, name):
        self.name = name

    def printBye(self):
        print(f"Good bye {self.name}, from the user defined package!")

