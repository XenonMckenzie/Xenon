from datetime import datetime

def write_entry():

    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    print("\n--- New Diary Entry ---")
    entry = input("Write your diary entry:\n")

    with open("diaries.txt","a") as file:
        file.write(f"\nDate: {date_time}\n")
        file.write(entry + "\n")
        file.write("-" * 40 + "\n")

    print("Entry saved suuccessfully!\n")


def view_entries():
    try:
        with open("diaries.txt","r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No diary entries found yet.\n")


def main():
    while True:
        print("Personal Diary App")
        print("1. Write new entry")
        print("2. View entries")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            write_entry()
        elif choice =="2":
            view_entries()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()