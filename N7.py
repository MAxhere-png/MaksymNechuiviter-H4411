while True:
    number1 = float(input("Введіть перше число:"))
    number2 = float(input("Введіть друге число:"))

    Action1 = "1.Ділення"
    Action2 = "2.Множення"
    Action3 = "3.Віднімання"
    Action4 = "4.Додавання"
    print(Action1, Action2, Action3, Action4)

    userAction = int(input("Обиріть дію зі списку вище(вкажіть цифрою):"))
    if userAction == 1:
        if number2 == 0:
            print("Ділення на нуль неможливе")
        else:
            result = number1 / number2
            print("Результат:", result)
            break
    elif userAction == 2:
        result = number1 * number2
        print("Результат:", result)
        break
    elif userAction == 3:
        result = number1 - number2
        print("Результат:", result)
        break
    elif userAction == 4:
        result = number1 + number2
        print("Результат:",result)
        break
    else:
        print("Невідома дія")