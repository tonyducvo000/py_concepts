# What are abstract classes?
# Abstract class can be considered as a blueprint for other classes.
# Abstract classes must contain one or more abstract methods.
# Abstract methods is a method that is declared but contains no implementation.
# Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.

# Abstract base classes provide an interface and make sure that the derived classes are implemented properly.

# Class to demonstrate problem of instantiating base class, and
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
# but did not fully implement all the methods of Base class.
conObj = Concrete()
print(isinstance(conObj, Concrete))  # Prints True

# Now the error is thrown ONLY when the bar() method is used.
# The error should be early as possible (i.e., Error should be thrown at line 29, when conObj is instantiated)
# If user did not call the bar() method, program would run with no issues.
# This becomes a problem ONLY when user calls the bar() method.
conObj.bar()
