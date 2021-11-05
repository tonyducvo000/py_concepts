# Drive code to demonstrate usage of user defined package
import my_regular_package.greeting as greet
import my_regular_package.bye

# Demonstrate namespace package
from my_pack_module import module1, module2

print(my_regular_package)

greetObj = greet.greetings("Tony")
greetObj.printHello();

byeObj = my_regular_package.bye.Bye("Tony")
byeObj.printBye()

# Namespace package modules
module1.myModFunc1()
mod1Obj = module1.MyModClass1()
mod1Obj.myModMethod()

module1.myModFunc1()
mod2Obj = module1.MyModClass1()
mod1Obj.myModMethod()

