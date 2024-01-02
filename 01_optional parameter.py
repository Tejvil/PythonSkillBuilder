# optional parameter

# def funct(x=1):
#     return x**2

# call = funct()
# print(call)

def funct(word, freq=1):
    print(word*freq)

call = funct("tim")


class car (object):
    def __init__(self, make, model, year, condition="New", kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
    
    def display (self,showall):
        if showall:
            print(f"This is a {self.make} {self.model} from year {self.year}, it is {self.condition} and has {self.kms}.")
        else :
            print (f"This car is a {self.make} {self.model} from {self.year}.")

whip = car ("Ford","Fusion", 2012,"New",1000)

whip.display(True)



