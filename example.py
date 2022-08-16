from datetime import date
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @classmethod
    def frombirthyear(cls,name,year):
        return cls(name,date.today().year-year)

    @staticmethod
    def isadult(age):
        return age>18

person1 = person('moni',21)
person2 = person.frombirthyear('moni',1996)
print(person1.age)
print(person2.age)
print(person.isadult(22))
    
output:

21
26
True