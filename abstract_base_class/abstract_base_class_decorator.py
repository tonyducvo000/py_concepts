# To remedy the problems presented in abstract_base_class,py, Python's abc module is used.

# How to use abc:
# Base class subclasses ABCMeta and abstract methods are decorated with @abstractmethod function decorators.
# Subclass of Base class MUST implement all abstract methods.

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
# TypeError: Can't instantiate abstract class Base with abstract methods bar, foo will be thrown.
baseObj = Base()


# Problem #2 solution - @abstract method prevents Concrete from being instantiated
# Concrete class did not implement all of the methods in Base class.
# TypeError: Can't instantiate abstract class Concrete with abstract methods bar will be thrown.
conObj = Concrete()
