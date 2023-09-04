import json
import os

# Define the filename for storing transactions
data_file = "transactions.json"

# Initialize the transaction list
transactions = []

# Check if the data file exists and load transactions
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        transactions = json.load(file)

def save_transactions():
    # Save transactions to the data file
    with open(data_file, "w") as file:
        json.dump(transactions, file)

def add_transaction():
    transaction = {}
    transaction["type"] = input("Enter transaction type (Income/Expense): ").capitalize()
    transaction["category"] = input("Enter transaction category: ")
    try:
        transaction["amount"] = float(input("Enter transaction amount: "))
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return

    transactions.append(transaction)
    save_transactions()
    print("Transaction added successfully!")

def calculate_budget():
    income = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "Income")
    expenses = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "Expense")
    return income - expenses

def expense_analysis():
    expense_categories = set(transaction["category"] for transaction in transactions if transaction["type"] == "Expense")
    
    print("\nExpense Analysis:")
    for category in expense_categories:
        category_total = sum(transaction["amount"] for transaction in transactions if transaction["type"] == "Expense" and transaction["category"] == category)
        print(f"{category}: ${category_total:.2f}")

while True:
    print("\nOptions:")
    print("1. Add Transaction")
    print("2. Calculate Budget")
    print("3. Expense Analysis")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_transaction()
    elif choice == "2":
        budget = calculate_budget()
        print(f"Remaining Budget: ${budget:.2f}")
    elif choice == "3":
        expense_analysis()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option.")

print("Goodbye!")