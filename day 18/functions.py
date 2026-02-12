#greet basic

def welcome_user(name):
    print(f"{name} goodluck with your workout today!")

welcome_user("nick")
print()

#btw calculator
amount = int(input("fill in number to calc: "))
def calc_btw(amount):
    result = amount * 1.21
    return result
total = calc_btw(amount)
print(total)

#change option 5 tracker into function
sets = 4
reps = 12
def progress_check(sets, reps):
    total = sets * reps
    if total > 40:
        status = "very strong"
    elif total >= 25:
        status = "strong"
    else:
        status = "can better"
    return status
output = progress_check(sets, reps)
print(f"your progress is {output}")

