while True:
    print("\n===PERSONAL DIARY===")
    print("1. Write Entry")
    print("2. Read Entries")
    print("3. Exit")

    choice = input("Choose an option:")


    if choice == "1":
        entry = input("Write your diary entry: ")

        with open("diary.txt","a") as file:
            file.write(entry + "\n")

        print("Entry  saved succesfully!")


    elif choice == "2":
        try:
            with open("diary.txt","r")as file:
                content = file.read()
                print("\n--- Your Diary Entries---")
                print(content)
            
        except FileNotFoundError:
            print("No diary entires found yet.")


    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
            
