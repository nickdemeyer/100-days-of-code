#while loops = repeat while condition is true

print("=== number guessing game ===")
print("i'm thinking of a number between 1 and 20")
print("you have 5 lives")
print()

import random
secret = random.randint(1,20)
lives = 5

while lives > 0:
    guess = int(input(f"lives:{lives} - your guess:"))
    if guess == secret:
        print(f"you won! with {lives} remaining")
        break
    elif guess < secret:
        lives = lives - 1
        print("too low")
    else:
        lives = lives - 1
        print("too high")
        if lives == 0:
            print("game over, the number was {secret}")
print("thanks for playing!")
