#looping through a list

names = ["Nick", "Emma", "Lucas", "Sophie"]

print("people in the list:")
for name in names:
    print(f"hello, {name}")

print()

#you can loop through any list
numbers = [10, 20, 30, 40, 50]

print("number doubled:")
for num in numbers:
    doubled = num * 2
    print(f"{num} x 2 = {doubled}")