#keep asking until valid age

print("=== age verifier ===")

while True:
    age = int(input("enter your age (1 - 120): "))

    if age < 1:
        print("age must be possitive")
    elif age > 120:
        print("age must be 120 or below")
    else:
        print(f"valid age: {age}")
        break
print("age verifier complete")