# *args and **kwargs are ways to pass a variable number of arguments to functions.
# *args are non keyward arguments, while **kwargs are keyword arguments.

# Example:
def argFunc(*args):
    # *args takes in any number of variable, of any type, and stores it as a tuple.
    for index in args:
        print(index, end=" ")

    print(f"\nargs is of type: {type(args)}")


def kwargFunc(**kwargs):
    # **kwargs takes in any number of keyword variables, of any type, and stores it as a dictionary.
    for key, value in kwargs.items():
        print(f"The key is {key}, and the value is {value}")

    print(f"kwargs is of type: {type(kwargs)}")


argFunc("hello", 232, [1, 4, 56], {"myKey":"myValue", 1:"foo", 2:"bar", 3:"foobar"}, \
        ("myTuple", 1, 2, 3), {1, 1, 1, 2, 3})

print("\n")

kwargFunc(myString="bye", myNum=100, myList=[4, 5, 6, 2], \
          myDict={"myOtherKey":"myOtherValue", 1:"fizz", 2:"buzz", 3:"fizzbuzz"}, \
          myTuple=("myOtherTuple", 1, 2, 3), mySet={4,4,4,23} )