from abc import abstractmethod

class Country:
    educatin = True
    def __init__(self, name, age):
        self.name = name
        self.hdsk = age

class Person(Country):
    min_age = 20
    max_age = 60

bim = Person('bim', 20)
bim.org = 'new'
tom = Person('Tom', 22)
print(bim.hdsk)
tom.hdsk = tom.hdsk + 20
print(tom.hdsk)