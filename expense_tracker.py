import json
import os

FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

expenses = load_expenses()

while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter Category (Food/Travel/Shopping/etc): ")
        amount = float(input("Enter Amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense Added Successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\n--- Expense List ---")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['category']} - ₹{exp['amount']}")

    elif choice == "3":
        total = sum(exp["amount"] for exp in expenses)
        print(f"\nTotal Expense = ₹{total}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice. Please try again.")
