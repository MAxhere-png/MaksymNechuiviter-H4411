class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False 

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} увімкнено")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} вимкнено")

class Smartphone(Device):
    def make_call(self, number):
        if self.is_on:
            print(f"Телефоную на номер {number} з {self.name}...")
        else:
            print(f"Помилка: {self.name} вимкнено. Неможливо зателефонувати.")

class Lamp(Device):
    def add_brightness(self, procent):
        if self.is_on:
            print(f"Яскравість лампи {self.name} встановлено на {procent}%.")
        else:
            print(f"Помилка: Світло вимкнено. Спочатку увімкніть лампу.")


phone = Smartphone("Iphone 15 pro")
desk_lamp = Lamp("lampa")

phone.turn_on()
phone.make_call("+380 00 000 00 00")
phone.turn_off()

print("-" * 30)

desk_lamp.add_brightness(80) 
desk_lamp.turn_on()
desk_lamp.add_brightness(80)
