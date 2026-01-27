import random  

secretNumber = random.randint(1,10)
attempts = 3
print("Вгадайте число від 1 до 10. У вас 3 спроби.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Спроба {attempt}: "))

    if guess == secretNumber:
        print("Вітаю! Ви вгадали!")
        break
    elif guess > secretNumber:
        print("Число менше")
    else:
        print("Число більше")
    
    if attempt == attempts:
        print(f"Спроби закінчилися. Це було число {secretNumber}.")
