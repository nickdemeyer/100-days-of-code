import random #random number generator

#setup and initialize
all_guesses = [] #list to store all guesses
total_wins = 0 #total wins all rounds
total_rounds = 0 #total rounds played

#main game loop
print("Welcome to the Number Guessing Game!")
while True:
    print("\n" + "="*40)
    
    #start a new round
    play = input("Do you want to play a round? (yes/no): ").lower() #.lower() to standardize input
    if play == "no":
        break   #player dont want to play so program ends
    elif play != "yes":
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue #restart loop for valid input
    
    #generate random number
    secret = random.randint(1, 20) #randint(1,20) generates random number between 1 and 20
    round_guesses = [] #list to store guesses for this round
    attempts = 0 #number of attempts in this round
    won = False
    total_rounds = total_rounds + 1 #increase round counter

    print(f"\n Round {total_rounds}")
    print("I'm thinking of a number between 1 and 20.")
    print("you have 5 attempts to guess it.")

    #guessing loop
    while attempts < 5:
        try: #error handling for non-integer input
            guess = int(input(f"attempt {attempts + 1}/5: Enter your guess: "))
        except: #if input is not an integer
            print("Invalid input. Please enter valid number between 1 and 20.")
            continue #restart loop for valid input

        attempts = attempts + 1 #increase attempt counter
        round_guesses.append(guess) #store guess in round guesses
        
        #check guess
        if guess == secret:
            print(f"Correct! You've guessed the number {secret} in {attempts} attempts.")

            won = True #player has won this round
            total_wins = total_wins + 1 #increase total wins counter
            break #exit guessing loop after they won

        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

    #end of round
    if not won: #out of guesses and didnt win
        print(f"Sorry, you've used all attempts. The number was {secret}.")

    #round statistics
    print("\n" + "-"*40)
    print("round statistics:")
    print("-"*40)

    print("your guesses:", round_guesses) #display all guesses for this round
    num_guesses = len(round_guesses)
    print(f"total guesses: {num_guesses}") #display total number of guesses

    #analyze guesses
    highest_guess = max(round_guesses)
    print(f"highest guess: {highest_guess}") #display highest guess
    lowest_guess = min(round_guesses)
    print(f"lowest guess: {lowest_guess}") #display lowest guess
    average_guess = sum(round_guesses) // len(round_guesses)
    print(f"average guess: {average_guess}") #display average guess

    #count close guesses 
    close_guesses = 0
    for g in round_guesses:
        difference = abs(g - secret) #gives absolute difference between guess and secret number
        if difference <= 3:
            close_guesses = close_guesses + 1
            print(f"close guesses within 3: {close_guesses}") #display number of close guesses
            all_guesses.extend(round_guesses) #.extend() adds all items from lists

#final statistics after all rounds
print("\n" + "="*40)
print("final statistics:")
print("="*40)
print(f"total rounds played: {total_rounds}") #display total rounds played
print(f"total rounds won: {total_wins}") #display total rounds won

#calculate winrate
if total_rounds > 0:
    win_rate = (total_wins / total_rounds) * 100
    print(f"win rate: {win_rate}%") #display win rate with 2 decimal places
else:
    print("no rounds played")

#all-time guess analysis
if len(all_guesses) > 0: #list is not empty
    print("\n all time guess analysis:")
    print(f"Total guesses ever: {len(all_guesses)}") #display total guesses ever
    print(f"Highest guess ever: {max(all_guesses)}") #display highest guess ever
    print(f"Lowest guess ever: {min(all_guesses)}") #display lowest guess ever

    avg_all_time = round(sum(all_guesses) / len(all_guesses), 1) #calculate average guess all time
    print(f"Average guess ever: {avg_all_time}") #display average guess all time

    print("\n most common guesses:")
    counted = []

    for num in range(1, 21): #check numbers between 1 and 20
        count = all_guesses.count(num) #count occurrences of num in all_guesses
        if count > 0:
            print(f"{num} was guessed {count} times")

#end of program
print("\n" + "="*40)
print("thanks for playing")
print("="*40)