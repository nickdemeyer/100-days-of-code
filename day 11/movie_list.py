print("=== movie list ===")

list = []

while True:
    print("1. list movies")
    print("2. add movie")
    print("3. delete movie")
    print("4. exit")

    choice = input("choose an option: ")
    if choice == "1":
        if list == []:
            print("no movies in the list")
        else:
            for i, movie in enumerate(list):
                print(f"{i + 1}. {movie}")
    elif choice == "2":
        movie = input("enter movie name: ")
        list.append(movie)
        print(f"{movie} added to the list")
    elif choice == "3":
        movie = int(input("enter movie number to delete: "))
        if 1 <= movie <= len(list):
            removed_movie = list.pop(movie - 1)
            print(f"{removed_movie} removed from the list")
        else:
            print("invalid movie number")
    elif choice == "4":
        print("exiting...")
        break