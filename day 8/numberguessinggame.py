print("=== welcome ===")

import random
secret_number = random.randint(1, 10)
attempts = 0

while True:
    user_number = int(input("Guess a number between 1 and 10: "))
    attempts = attempts + 1
    if user_number == secret_number:
        print("you win!")
        print(f"you took {attempts} attempts")
        break
    elif user_number < secret_number:
        print("to low")
    elif user_number > secret_number:
        print("to high")
    else:
        print("error")
        continue


print("=== game over ===")