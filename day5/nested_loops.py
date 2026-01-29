#loop inside a loop

print("=== pattern ===")

for row in range(5):
    for col in range(5):
        print("*", end=" ")
    print()

print()

#number pattern

print("=== number pattern ===")

for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

