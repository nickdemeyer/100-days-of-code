print("=== simple library manager ===")

books = []

while True:
    print("1. view books")
    print("2. add book")
    print("3. borrow book")
    print("4. return book")
    print("5. exit")
    choice = input("choose your option: ")

    if choice == "1":
        if books == []:
            print("empty")
        else:
            for i, book in enumerate(books):
                print(f"{i + 1}. {book[0]} - {book[1]}")

    elif choice == "2":
        user_input = input("what title would you like to add? ")
        status = "available"
        books.append([user_input, status])
        print("added successfully")
    
    elif choice == "3":
        for i, book in enumerate(books):
            print(f"{i + 1}. {book[0]} - {book[1]}")
        user_input = int(input("choose number of book you want to borrow: "))
        index = user_input - 1
        
        
        if books[index][1] == "available":
            books[index][1] = "borrowed"         
        else:
            print("book is borrowed")

    elif choice == "4":
        for i, book in enumerate(books):
            print(f"{i + 1}. {book[0]} - {book[1]}")
        user_input = int(input("choose number of book that u want to return: "))
        index = user_input - 1 
        
        if books[index][1] == "borrowed":
            books[index][1] = "available"
        else:
            print("book is available already")

    elif choice == "5":
        print("exiting...")
        break