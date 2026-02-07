class Animal:
    weight = 0.0
    def __init__(self, age = 14, name = "Tom"):
        self.age = age
        self.name = name

class Leopard(Animal):
    pass

class Dog(Animal):
    weight = 14.0
    def __init__(self, age= 9.0, name = "Charlie"):
        super().__init__(age)
        super().__init__(name)


class Owl(Animal):
    weight = 2.4
    def __init__(self, age= 5.0, name = "Arthur"):
        super().__init__(age)
        super().__init__(name)

leo = Leopard()
sobaka = Dog()
sova = Owl()
print("Age:", leo.age, "Name:" , leo.name, "Weight:", leo.weight)
print("Age:", sobaka.age, "Name:" , sobaka.name, "Weight:", sobaka.weight)
print("Age:", sova.age, "Name:", sova.name, "Weight:", sova.weight)