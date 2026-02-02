import random

secrect_number = random.randint(1, 15)
attempts = 0

print("Welcome to the Number Guessing Game!")

while True:
    number = int(input("Guess a number between 1 and 15: "))
    attempts = attempts + 1
    difference = abs(secrect_number - number)
    if number == secrect_number:
        print(f"you won!")
        print(f"you guessed the number in {attempts} attempts.")
        break
    elif number < secrect_number:
        print("to low!")
    else:
        print("to high!")
    if difference <= 2: 
        print("very close!")
    elif difference <=5:
        print("warm!")
    else:
        print("cold!")
    if attempts >= 5:
        print(f"you lost! The correct number was {secrect_number}.")
        break

if number == secrect_number:
    if attempts == 1:
        print("genius!")
    elif attempts <=3:
        print("excellent!")
    else:
        print("good guess")
print("Thanks for playing!")
print("exiting...")