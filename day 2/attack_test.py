#test the attack timing
for tick in range(44, 60):
    if tick % 4 == 0:
        print(f"tick {tick}: Attack!")
    else:
        remainder = tick % 4
        print(f"tick {tick}: wait... (remainder: {remainder})")

