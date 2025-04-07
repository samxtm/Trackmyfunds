class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, date):
        # Basic validation to ensure all fields are filled
        if not category or not amount or not date:
            print("Please fill in all fields!")
            return
        
        # Add expense to the list
        expense = {
            'category': category,
            'amount': float(amount),
            'date': date
        }
        self.expenses.append(expense)
        
        # Update the total amount
        self.update_total()

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print(f"Expense at index {index} deleted.")
            self.update_total()
        else:
            print("Invalid index. Could not delete expense.")

    def update_total(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total amount: ${total:.2f}")
    
    def display_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for i, expense in enumerate(self.expenses):
                print(f"{i+1}. Category: {expense['category']}, Amount: ${expense['amount']}, Date: {expense['date']}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense")
        print("2. Delete Expense")
        print("3. Display Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category: ").strip()
            amount = input("Enter amount: ").strip()
            date = input("Enter date (YYYY-MM-DD): ").strip()

            tracker.add_expense(category, amount, date)
        elif choice == '2':
            tracker.display_expenses()
            try:
                index = int(input("Enter the index of the expense to delete: ")) - 1
                tracker.delete_expense(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            tracker.display_expenses()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
