secret_password = "python"
attempts = 0

print("Welcome to the password guessing game!")
print()
print("you have 5 attempts to guess the secret password.")
while True:
    guess = input("Enter your guess: ")
    attempts = attempts + 1
    if guess == secret_password:
        print("you win, access granted")
        print(f"You guessed it in {attempts} attempts.")
        break
    elif len(guess) < len(secret_password):
        print("Your guess is too short.")
    elif len(guess) > len(secret_password):
        print("Your guess is too long.")
    if guess[0] == secret_password[0]:
        print("first letter is correct")
    if attempts >= 5:
        print("game over!")
        break

if attempts == 1:
    print("you are genius!")
elif attempts <= 3:
    print("well done!")
else:
    print("good effort!")

print("Thanks for playing!")