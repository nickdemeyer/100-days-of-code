print("===simple username check===")

usernames = ["gym", "beast", "pinda"]

user_input = input("which username do you want to use? ")

if user_input in usernames:
    print("welcome")
else:
    print("username not found")