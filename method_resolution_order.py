# Method resolution order defines the order in which the base classes are searched when executing a method.
# First, the method or attribute is searched within a class and then it follows the order we specified while inheriting.
# This order is also called Linearization of a class and set of rules are called MRO (Method Resolution Order).

# Program to demonstrate multiple layers of inheritance.
# The MRO is then printed, showing the order of inheritance in a list,
# with the most recent inheritance appearing  near the beginning of the list.
# Note that <class 'object'> is the last element in the list.  This is the superclass that all classes inherit from.
from abc import ABCMeta, abstractmethod

# Abstract Base Class
# Animal kingdom
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

# Species
# Horse
class Caballus(Equus):
    def shape(self):
        print("I'm pretty big!")

    def say(self):
        print("Neigh!")

    # Redefining temperament() inherited from Abstract Base Class.
    def temperament(self):
        print("I'm gentle!")

# Donkey
class Africanus(Equus):
    def __init__(self):
        self.hasBigEars = True

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

# Throws an error since it cannot create a consistent method resolution.
# class MuleClone(Animalia, Mammalia, Perissodactyla, Equidae, Equus, Caballus, Africanus):
#     pass


# This won't throw an error, since the listed parent classes are written in order, from most recent to least recent
# inheritance.
class MuleClone(Caballus, Africanus, Equus, Equidae,
                Perissodactyla, Mammalia, Animalia):
    def talk(self):
        print("I'm the mule clone!")

# All abstract method has been overridden.
# No errors when instantiated.
MuleObj = Mule()

# Calling method inherited from Donkey.
print(MuleObj.hasBigEars)

# Calling method from Mammalia.
MuleObj.giveBirth()
MuleObj.feedChild()

# Mule clone instantiation and calling its methods.
print("Mule clone is giving birth!")
MCloneObj = MuleClone()
MCloneObj.giveBirth()
MCloneObj.feedChild()

# Calling the MRO.
# Both MRO are similar.
print(Mule.mro())
print(MuleClone.mro())