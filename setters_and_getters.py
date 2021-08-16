#setters and getters can be used to add validation logic around setting and getting a value
#avoid direct access/modification of a private variable.

class Nerds:
    def __init__(self):
        self._age = 0  #age is declared as private

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

    # function to set value of _age
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        print("del method called")
        del self._age


    #property() is a buildt-in function that creates and returns a property object.
    #
    age = property(get_age, set_age, del_age)

#################################################################
#Implementation of property() as a Function Decorator (@property)

class NerdsWProperty:
    def __init__(self):
        self._age = 0

    #Getter method.
    #@property is used to define a property.
    #here we define @property as age().
    #Property name will now be age and setter will be called by @age.setter
    @property
    def age(self):
        print("getter method called")
        return self._age

    #Setting @age.setter property
    #Notice we are not using @property.setter
    @age.setter
    def age(self, a):
        if(a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a

    #Setting @age.deleter property
    #Again, notice we are not using @property.deleter
    @age.deleter
    def del_age(self):
        print("del method called")
        del self._age


markWithProperty = NerdsWProperty()
markWithProperty.age = 12 #this line sets the age using set_age() method.  This will fail the program.
print(markWithProperty.age) #this line gets the age using the get_age() method


mark = Nerds()
mark.age = 10 #this line sets the age using set_age() method
print(mark.age) #this line gets the age using the get_age() method