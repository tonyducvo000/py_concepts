# Drive code to demonstrate usage of user defined package
import my_regular_package.greeting as greet
import my_regular_package.bye

print(my_regular_package)

greetObj = greet.greetings("Tony")
greetObj.printHello();

byeObj = my_regular_package.bye.Bye("Tony")
byeObj.printBye()