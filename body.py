import os
from datetime import datetime

# In-memory database to store expenses
expenses = []

# Function to display all expenses
def display_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\nExpenses List:")
    print("{:<20} {:<10} {:<15} {:<10}".format("Category", "Amount", "Date", "Delete"))
    for idx, expense in enumerate(expenses):
        print(f"{expense['category']:<20} {expense['amount']:<10} {expense['date']:<15} {idx:<10}")

# Function to add a new expense
def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    # Convert date to a standard format
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    
    expense = {
        'category': category,
        'amount': amount,
        'date': date_obj
    }
    expenses.append(expense)
    print("Expense added successfully!")

# Function to delete an expense by index
def delete_expense():
    try:
        display_expenses()
        idx = int(input("Enter the index of the expense to delete: "))
        if 0 <= idx < len(expenses):
            expenses.pop(idx)
            print("Expense deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to display total amount of expenses
def display_total():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: {total:.2f}")

# Main function to run the app
def main():
    while True:
        print("\n--- Money Tracker ---")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Delete Expense")
        print("4. View Total Expenses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_expenses()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            display_total()
        elif choice == '5':
            print("Exiting Money Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == '__main__':
    main()
