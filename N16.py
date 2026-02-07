class TransportVehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} рухається зі швидкістю {self.speed} км.")

class Car(TransportVehicle):
    def move(self):
        print(f"Автомобіль {self.brand} рухається зі швидкістю {self.speed} км.")

class Airplane(TransportVehicle):
    def move(self):
        print(f"Літак {self.brand} рухається зі швидкістю {self.speed} км.")

class Bicycle(TransportVehicle):
    def move(self):
        print(f"Велосипедист на {self.brand} рухається зі швидкістю {self.speed} км.")

my_car = Car("Tesla", 120)
my_plane = Airplane("Boeing 747", 900)
my_bike = Bicycle("bicycle", 25)

my_car.move()
my_plane.move()
my_bike.move()