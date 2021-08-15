#code to demonstrate passing a function
#as an argument into another function

def inc(x):
    return x+1

#operates takes in a function as part of the paramerter
def operate(func, x):
    #pass x as argument into func function
    result = func(x)
    return result

#pass in inc function as an argument into operate()
print(operate(inc, 3))