#tuples - immutable lists (cannot be changed after creation)

# creating a tuple
coordinates = (10, 20)
person = ("nick", 30, "developer")

#accessing (same as lists)
print("x:", coordinates[0])
print("y:", coordinates[1])
print("Name:", person[0])

# unpacking a tuple
name, age, profession = person
print(f"{name} is a {age}-year-old {profession}.")

#multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = get_min_max([3, 1, 4, 1, 5, 9, 2, 6, 5])
print(f"Smallest: {smallest}, Largest: {largest}")
