def print_msg(message):
        greeting = "Hello"

        #define printer() function within print_msg function
        def printer():
                print(greeting, message)

        #call printer() function
        #printer()

        #instead of calling the printer() function
        #return the printer function - no parenthesis
        return printer

#print_msg("Python is awesome")

#bind identifier to print_msg(),
#that is store result of print_msg("Python is awesome") to func
func = print_msg("Python is awesome")

#################################################################################
#at this point, the function print_msg is done executing and
#all the local scope variables are destroyed since it is done executing

#although the scope of print_msg is destroyed,
#we still have access to greeting and message variables
#the print statement, print(greeting, message) in printer() function
#is accessing these variables - this demonstrates closure.

#closure is simply a value that remembers and variables in it's enclosing scope
#even if the outer function is done executing

#the line below is valid - it is calling the inner print() function
func()

