#break - stop the loop early

print("looking for number 7:")
for num in range(1,20):
    print(f"checking {num}...")
    if num == 7:
        print("founded!")
        break
print()

#continue - skip some iterations

print("only even number:")
for num in range(1,11):
    if num % 2 == 1:
        continue
    print(num)