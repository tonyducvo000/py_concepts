# To remedy the problems presented in abstract_base_class, Python's abc module is used.

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

# Problem #1 solution - @abstractmethod prevents Base class from being instantiated.
# TypeError: Can't instantiate abstract class Base with abstract methods bar, foo
baseObj = Base()

# Problem #2 solution - @abstract method prevents Concrete from being instantiated
# Concrete class did not implement all of the methods in Base class.
# TypeError: Can't instantiate abstract class Concrete with abstract methods bar
conObj = Concrete()