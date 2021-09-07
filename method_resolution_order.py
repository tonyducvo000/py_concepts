# Method resolution order defines the order in which the base classes are searched when executing a method.
# First, the method or attribute is searched within a class and then it follows the order we specified while inheriting.
# This order is also called Linearization of a class and set of rules are called MRO (Method Resolution Order).

from abc import ABCMeta, abstractmethod

# Abstract Base Class
class Animalia(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def consumes(self):
        pass
    @abstractmethod
    def dwelling(self):
        pass
    @abstractmethod
    def temperament(self):
        pass

# Class
class Mammalia(Animalia):
    def __init__(self):
        self.hasHair = True
        self.warmBlooded = True
        self.liveBirth = True
        self.produceMilk = True
        self.bigBrain = True

    def giveBirth(self):
        print("*Gives birth*")

    def feedChild(self):
        print("*Nurses children*")

# Order
class Perissodactyla(Mammalia):
    def __init__(self):
        self.isOddToed = True
        self.isRuminant = False
        self.walksOnFourLegs = True

    def form(self):
        print("I'm an odd-toed ungulate!")

    def consumes(self):
        print("*Consumes vegetation*")

    def dwelling(self):
        print("I live on land!")


# Family
class Equidae(Perissodactyla):
    def shape(self):
        print("*Is horse-like form*")

# Genus
class Equus(Equidae):
    pass

# Genus species
# Horse
class Caballus(Equus):
    def shape(self):
        print("I'm pretty big!")

    def say(self):
        print("Neigh!")

    def temperament(self):  # redefining down temperament here, after multiple layers of inheritance
        print("I'm gentle if domesticated!")

# Donkey
class Africanus(Equus):
    def shape(self):
        print("I'm pretty small!")

    def say(self):
        print("Hee-haw!")

    def temperament(self):
        print("I'm impatient!")

# Mule - multiple inheritance
class Mule(Caballus, Africanus):
    def shape(self):
        print("I have a head of a donkey, and body of a horse!")

    def say(self):
        print("Neigh hee-haw!")

    def temperament(self):
        print("I'm intelligent, sociable, and gentle!")

print(Mule.mro())
