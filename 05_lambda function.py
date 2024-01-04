# lambda function 

def func(x):
    func2 = lambda x:x+5
    return func2(x) + 10

funct = lambda x,y:x+y
print(funct(5,5))
print(func(2))

# lambda on map and filter 

a = [1,2,3,4,5,6,7,8,9,10]
List = list(map(lambda x: x+5,a))
newlist = list(filter(lambda x: x%2==0,a))
print(List)
print(newlist)

