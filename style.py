import os
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# In-memory database to store expenses
expenses = []

# Function to display all expenses
def display_expenses():
    if not expenses:
        print(Fore.RED + "No expenses recorded yet.")
        return
    
    print("\n" + Fore.CYAN + "Expenses List:")
    print(Fore.YELLOW + "{:<20} {:<10} {:<15} {:<10}".format("Category", "Amount", "Date", "Delete"))
    for idx, expense in enumerate(expenses):
        print(f"{expense['category']:<20} {expense['amount']:<10} {expense['date']:<15} {idx:<10}")

# Function to add a new expense
def add_expense():
    category = input(Fore.GREEN + "Enter expense category: ")
    amount = float(input(Fore.GREEN + "Enter amount: "))
    date = input(Fore.GREEN + "Enter date (YYYY-MM-DD): ")

    # Convert date to a standard format
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
    except ValueError:
        print(Fore.RED + "Invalid date format. Please use YYYY-MM-DD.")
        return
    
    expense = {
        'category': category,
        'amount': amount,
        'date': date_obj
    }
    expenses.append(expense)
    print(Fore.GREEN + "Expense added successfully!")

# Function to delete an expense by index
def delete_expense():
    try:
        display_expenses()
        idx = int(input(Fore.GREEN + "Enter the index of the expense to delete: "))
        if 0 <= idx < len(expenses):
            expenses.pop(idx)
            print(Fore.GREEN + "Expense deleted successfully!")
        else:
            print(Fore.RED + "Invalid index.")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid number.")

# Function to display total amount of expenses
def display_total():
    total = sum(expense['amount'] for expense in expenses)
    print(Fore.CYAN + f"\nTotal Expenses: {total:.2f}")

# Main function to run the app
def main():
    while True:
        print(Fore.MAGENTA + "\n--- Money Tracker ---")
        print(Fore.YELLOW + "1. View Expenses")
        print(Fore.YELLOW + "2. Add Expense")
        print(Fore.YELLOW + "3. Delete Expense")
        print(Fore.YELLOW + "4. View Total Expenses")
        print(Fore.YELLOW + "5. Exit")

        choice = input(Fore.GREEN + "Choose an option: ")

        if choice == '1':
            display_expenses()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            display_total()
        elif choice == '5':
            print(Fore.RED + "Exiting Money Tracker. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option. Please choose a valid option.")

if __name__ == '__main__':
    main()
