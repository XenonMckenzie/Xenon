from datetime import datetime

def write_report():
    now = datetime.now()
    date_time = now. strftime("%Y-%m-%d %H:%M:%S")

    print("\n --- DAILY SITE REPORT ---")
    weather = input("Weather condition: ")
    workers = input("Number of workers on site: ")
    activities = input("Work done today: ")
    issues = input("Issues encountered: ")

    with open("site_report.txt","a") as file:
        file.write(f"\nDate: {date_time}\n")
        file.write(f"Weather: {weather}\n")
        file.write(f"Workers: {workers}\n")
        file.write(f"Activities: {activities}\n")
        file.write(f"Issues: {issues}\n")
        file.write("-" * 50 + "\n")

    print("Report saved successfully!\n")

def view_report():
    try:
        with open("site_report.txt","r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No report entries found yet.\n")

def main():
    while True:
        print("Site Daily Report Logger")
        print("1. Write new report")
        print("2. View Report")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            write_report()
        elif choice == "2":
            view_report()
        elif choice == "3":
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()