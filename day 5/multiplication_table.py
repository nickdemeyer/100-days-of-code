#multiplication table

print("===multiplication table for 5===")

for i in range(1,11):
    result = 5 * i
    print(f"5 x {i} = {result}")
print()

#ask user what table they want

number = int(input("which multiplication table?"))

print(f"===multiplication table for {number}")

for i in range(1,11):
    result = number * i
    print(f"{number} * {i} = {result}")