try:
    number_float = float(input("Введіть число:"))
    number_int = int(number_float)
    print("int number:", number_int)
except(ValueError):
    print("Ці дані неможливо конвертувати в ціле число")
finally:
    ("Робота завершена")   