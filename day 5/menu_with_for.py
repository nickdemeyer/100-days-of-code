#using for loops for menus

print("=== shopping list ===")

items = ["Apples", "Bread", "Milk", "Eggs", "Cheese"]

for i in range(len(items)):
    print(f"{i + 1}. {items[i]}")

print()

choice = int(input("which item number?"))

if 1 <= choice <= len(items):
    selected = items[choice - 1]
    print(f"you selected: {selected}")
else:
    print("invalid choice!")

    