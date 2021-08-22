#Docstring provides a way to associate documentation with functions, class, modules, and methods.

#Docstring conventions:
#Docstrings must be the first statement in the function, class, modules or methods - otherwise it's not considered a docstring.
#Cannot use a hashtag, as it is used for comments.  Begin and end with ''' or """ for docstrings. Comments can't be accessed with __doc__.
#Docstring line should begin with a capital letter and end with a period.
#First line is a short description (summary line) and can be the same line as the opening quotes, or on the next line.
#If single line, put opening and closing quotes on same line of docstring.
#If multi line, second line should be a blank, visually seperating the summary from the rest of the description.
#The following lines should describe calling conventions, side effects, returns, etc.
#The entire docstring is indented the same as the quotes at its first line.
#Relative indentation (to the first line) of later lines are allowed.

#Example of docstring on class, note the line break after the summary:
class Greeting:
    '''
    Class for different types of greetings.

    Attribute:
        name (string): The name of the person being greeted.
    '''

    def __init__(self, name):
        '''
        Constructor for Greeting class.

        Parameters:
            name (string): Name of the person being greeted.
        '''

        self.name = name

    def returnGreeting(self):
        '''
        Method to return a greeting string, rather than printing the string.

        Returns:
            string: Greeting string.
        '''

        return f"{self.name}, you've return instead of printing!"

    def printHello(self):
        '''Prints hello to inputted name.'''

        print(f"Hello there {self.name}.")

    def printGoodMorning(self):
        """Prints Good morning to inputted name."""

        print(f"Good morning {self.name}!")



aObj = Greeting("Tony")

#Print docstrings for printGoodMorining().  Note no paranthesis are used.
print(aObj.printGoodMorning.__doc__)
