userNumber = int(input("Введіть число:"))
def factorial_loop(userNumber):
    count = 1
    for i in range(2, userNumber + 1):
        count *= i
    return count
print(factorial_loop(userNumber)) 
