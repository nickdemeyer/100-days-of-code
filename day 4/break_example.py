#break exits the loop directly

count = 1

while count <= 10:
    print("count:", count)

    if count == 5:
        print("breaking out")
        break #exit the loop when count is 5

    count = count + 1

print("loop finished at:", count)