# Map function

li = [1,2,3,4,5,6,7,8,9,10]

def funct(x):
    return x**x

# print([funct(x) for x in li])                            works same as below.

print(list(map(funct,li)))


