##################################################################################################################################################################

# What are abstract classes?
# Abstract class can be considered as a blueprint for other classes.
# Abstract classes must contain one or more abstract methods.
# Abstract methods is a method that is declared but contains no implementation.
# Abstract classes may not be instantiated, and all of its abstract methods must be implemented by its subclasses.
# Abstract base classes separate the interface from the implementation.

# When and how to use abstract classes:
# Abstract base classes provide an interface and make sure that the derived classes are implemented properly.

# Abstract base classes provide a way to define interfaces when other techniques
# like hasattr() would be clumsy or subtly wrong (for example with magic methods).

# When there is a large number of classes and keeping track is impossible,
# abstract base classes can help in this regards.

# When multiple classes have methods that function similarly (e.g., Lion.feed_lion(), Cat.feed_cat(), Dog.feed_dog()).
# Lion, Cat, and Dog class can be subclassed from an abstract class (e.g., Class Animal).
# Each subclass then simply implement the abstract feed() method.

# Subclass of abstract classes must implement ALL of the abstract methods.

##################################################################################################################################################################

# Class to demonstrate problem of:
# 1. Instantiating base class, and
# 2. Error when calling an abstract method (i.e., Concrete subclass did NOT override abstract base method).
class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'

# Problem #1: Base class is able to be instantiate.
# Base classes imply that children classes should subclass the base class.
# In this example, the base class directly being used.


baseObj = Base()
print(isinstance(baseObj, Base))  # Prints True

# Problem #2: Concrete class (subclass of Base), is able to instantiate,
# but did not fully implement all of the methods in Base class.
conObj = Concrete()
print(isinstance(conObj, Concrete))  # Prints True

# Now the error is thrown ONLY when the bar() method is called.
# The error should be early as possible (i.e., Error should be thrown at line 49, when conObj is instantiated).
# If user did not call the bar() method, the program would run normally.
# This becomes a problem when the user calls the method.
conObj.bar()

# In abstract_base_class_decorator.py, solution to problem 1 and 2 will be provided.
