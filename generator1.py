import random

alphabet = ["a","b","c","d","e","f","g","h","i","j","k",
           "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def random_letters():
    while True:
        yield random.choice(alphabet)

gen = random_letters()

for _ in range(10):
    print(next(gen))