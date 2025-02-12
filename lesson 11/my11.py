from abc import abstractmethod

class Country:
    educatin = True

    def __init__(self, name, age):
        self.name = name
        self.hdsk = age

class Person(Country):
    min_age = 20
    max_age = 60

    def __init__(self, name, age, sername):
        super().__init__(self, name, age)
        self.sername = sername

bim = Person('bim', 20)
bim.org = 'new'
tom = Person('Tom', 22)
print(bim.hdsk)
tom.hdsk = tom.hdsk + 20
print(tom.hdsk)


class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        result = self.width * self.length
        return f'Площадь прямоугольника шириной {self.width} и длиной {self.length} равна {result}'

    def perimeter(self):
        result = (self.width + self.length) * 2
        return f'Периметр прямоугольника шириной {self.width} и длиной {self.length} равна {result}'

object1 = Rectangle(56, 40)

print(object1.perimeter())
print(object1.area())


