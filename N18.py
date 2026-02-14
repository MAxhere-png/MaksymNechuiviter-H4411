user_list = [
    ("Tom", "Kid"),
    ("Bob", "Teenager"),
    ("Alice", "Adult")
]


try:
    while True:
        user_input = int(input("Оберіть ім'я зі списку числом(0, 1, 2): "))
        if user_input == 0:
            print(user_list[0])
            break
        elif user_input == 1:
            print(user_list[1])
            break
        elif user_input == 2:
            print(user_list[2])
            break
        else:
            print("Оберіть правильне число(0, 1, 2)")

except ValueError:
        print("Введіт ім'я числом(0, 1, 2)!!!")
finally:
    print("Робота завершена")