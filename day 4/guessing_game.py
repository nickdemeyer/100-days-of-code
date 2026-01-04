#number guessing game

print("=== number guessing game ===")
print("i'm thinking of a number between 1 and 10")
print()

secret_number = 7
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("enter your guess: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("congratz you won")
        break
    elif guess < secret_number:
        remaining = max_attempts - attempts
        print(f"too low! you have {remaining} attempts left")

    else:
        remaining = max_attempts - attempts
        print(f"too high! you have {remaining} attempts left")

     #check if user has used all attempts
    if attempts == max_attempts:
        print("sorry you lost the number was", secret_number)

print()
print("thanks for playing!")


    