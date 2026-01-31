#lists inside lists

#tic-tac-toe board
board = [["X", "O", "X"],
         ["O", "X", "O"],
         ["O", "X", "X"]]

#acces items
print("top-left:", board[0][0])  # Output: X
print("center:", board[1][1])    # Output: X
print("bottom-right:", board[2][2])  # Output: X

#print the board
for row in board:
    print(row)

print()

#print formatted
for row in board:
    for cell in row:
        print(cell, end=" ")
    print()  # Newline after each row