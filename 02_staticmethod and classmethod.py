# staticmethod and classmethod

class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def Getpopulation(cls):
        return cls.population
    
    @staticmethod
    def isAdult(age):
        return age >= 18
    
    def display(self):
        print(f"{self.name} is {self.age} years old" )
    
newperson = person("tim", 10)
print(person.Getpopulation())
print(person.isAdult(50))



