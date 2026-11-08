# Python Expense Tracker

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open("expenses.txt", "a") as file:
        file.write(date + "," + name + "," + amount + "\n")

    print("Expense added successfully!")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            print("\n--- Your Expenses ---")

            for line in file:
                date, name, amount = line.strip().split(",")
                print(date, "|", name, "| Rs.", amount)

    except FileNotFoundError:
        print("No expenses found.")


def total_expenses():
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                total = total + float(data[2])

        print("Total Expenses: Rs.", total)

    except FileNotFoundError:
        print("No expenses found.")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")