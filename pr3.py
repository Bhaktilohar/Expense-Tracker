# import csv
# from datetime import datetime

# def add_expense(category, amount, description, date):
#     with open('expenses.csv', mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([category, amount, description, date])

# def display_expenses():
#     try:
#         with open('expenses.csv', mode='r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 print(f"Category: {row[0]}, Amount: {row[1]}, Description: {row[2]}, Date: {row[3]}")
#     except FileNotFoundError:
#         print("No expenses recorded yet.")

# def main():
#     categories = ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Others']
    
#     while True:
#         print("\nExpense Tracker")
#         print("1. Add an Expense")
#         print("2. View Expenses")
#         print("3. Exit")
        
#         choice = input("Choose an option: ")
        
#         if choice == '1':
#             print("\nCategories:")
#             for i, category in enumerate(categories, 1):
#                 print(f"{i}. {category}")
                
#             cat_choice = int(input("Choose a category: "))
#             category = categories[cat_choice - 1]
            
#             amount = float(input("Enter the amount: "))
#             description = input("Enter a description: ")
#             date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
#             add_expense(category, amount, description, date)
#             print("Expense added successfully.")
            
#         elif choice == '2':
#             print("\nExpenses:")
#             display_expenses()
            
#         elif choice == '3':
#             print("Goodbye!")
#             break
            
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()



import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, data_file='expenses.json'):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            print("Error: Could not decode JSON data.")
            self.data = []

    def save_data(self):
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error: Could not save data. {e}")

    def add_expense(self, amount, category, description):
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
        except ValueError as e:
            print(f"Invalid amount: {e}")
            return

        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().isoformat()
        }

        self.data.append(expense)
        self.save_data()
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.data:
            print("No expenses recorded.")
            return

        for expense in self.data:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

    def main(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                amount = input("Enter the amount: ")
                category = input("Enter the category: ")
                description = input("Enter the description: ")
                self.add_expense(amount, category, description)
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.main()
