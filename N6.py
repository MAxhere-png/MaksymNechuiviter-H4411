
while True:
    userRating = int(input("Введіть кількість отриманих балів (0-100):"))
    if userRating < 50:
        print("Незадовільно")
        break
        
    elif userRating >= 50 and userRating < 70:
        print("Задовільно")
        break

    elif userRating >=70 and userRating < 90:
        print("Добре")
        break

    elif userRating >=90 and userRating <=100:
        print("Відмінно")
        break

    else:
        print("Введіть правильну кількість балів!!!")
