#same result different result

print("===while loop===")
count = 1

while count <= 5:
    print(f"count: {count}")
    count = count + 1

print()

print("===for loop===")
for count in range(1,6):
    print(f"count: {count}")