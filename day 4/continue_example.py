#continu skips the rest of this iteration

count = 0

while count < 10:
    count = count + 1

    #skip odd numbers
    if count % 2 == 1:
        continue

    print("even number:", count)

print("done")
