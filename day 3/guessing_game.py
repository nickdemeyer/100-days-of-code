#number guesser game

print("=== number guessing game ===")
print("i am thinking of a number between 1 and 10")
print()

#secret number
secret_number = 7

#ask user to guess
guess = int(input("what is your guess? "))

#check guess
if guess == secret_number:
    print("come get your prize!")
elif guess < secret_number:
    print("too low!")
else: 
    print("too high!")

print()
print("the secret number was:", secret_number)
print("thanks for playing!")