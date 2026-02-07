class Person:
    def __init__(self, name, age = 27):
        self.name = name
        self.age = age

    def person_age(self):
        return f"{self.name} має вік: {self.age}"
    
class Driver(Person):
    def __init__(self, name, id_number):
        super().__init__(name)
        self.id_number = id_number

    def result(self):
        return f"Водій {self.name}, має номер посвідчення: {self.id_number}" 

human = Person("Alex")
print(human.person_age())

driver = Driver("Ivan", "6623712345")
print(driver.result())
