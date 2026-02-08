def add_expense():
    date = input("Enter date (DD/MM/YYYY): ")
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    amount = input("Enter amount: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{date},{category},{amount}\n")

    print("Expense added successfully!")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses found.")
        else:
            print("\n--- Expense List ---")
            for exp in expenses:
                date, category, amount = exp.strip().split(",")
                print(f"Date: {date}, Category: {category}, Amount: ₹{amount}")

    except FileNotFoundError:
        print("No expenses file found.")


def total_expense():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                date, category, amount = line.strip().split(",")
                total += float(amount)

        print(f"Total Expense: ₹{total}")

    except FileNotFoundError:
        print("No expenses file found.")


while True:
    print("\n--- Expense Tracker developed by Monty ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.")
