import json
from datetime import datetime
from collections import defaultdict

class Transaction:
    def __init__(self, amount, category, description, trans_type):
        self.amount = amount
        self.category = category
        self.description = description
        self.type = trans_type  # "income" or "expense"
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "type": self.type,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        t = Transaction(data["amount"], data["category"], data["description"], data["type"])
        t.date = data["date"]
        return t


class FinanceTracker:
    def __init__(self, data_file="finance_data.json"):
        self.transactions = []
        self.data_file = data_file
        self.load_data()

    def add_transaction(self, amount, category, description, trans_type):
        transaction = Transaction(amount, category, description, trans_type)
        self.transactions.append(transaction)
        print("Transaction added successfully!")

    def show_summary(self):
        total_income = sum(t.amount for t in self.transactions if t.type == "income")
        total_expense = sum(t.amount for t in self.transactions if t.type == "expense")
        balance = total_income - total_expense

        print(f"\n--- Summary ---")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Balance: ${balance:.2f}")

    def show_by_category(self):
        category_summary = defaultdict(float)
        for t in self.transactions:
            if t.type == "expense":
                category_summary[t.category] += t.amount

        print("\n--- Expenses by Category ---")
        for category, total in category_summary.items():
            print(f"{category}: ${total:.2f}")

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump([t.to_dict() for t in self.transactions], f, indent=4)
        print("Data saved successfully!")

    def load_data(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.transactions = [Transaction.from_dict(d) for d in data]
                print(f"Loaded {len(self.transactions)} transactions.")
        except FileNotFoundError:
            print("No previous data found. Starting fresh.")

    def run(self):
        print("Welcome to Personal Finance Tracker!")

        while True:
            print("\nOptions:")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. Show Summary")
            print("4. Show Expenses by Category")
            print("5. Save & Exit")

            choice = input("Select an option (1-5): ")

            if choice == "1":
                amount = float(input("Enter income amount: $"))
                category = input("Enter category (e.g. Salary, Bonus): ")
                desc = input("Enter description: ")
                self.add_transaction(amount, category, desc, "income")

            elif choice == "2":
                amount = float(input("Enter expense amount: $"))
                category = input("Enter category (e.g. Food, Rent, Bills): ")
                desc = input("Enter description: ")
                self.add_transaction(amount, category, desc, "expense")

            elif choice == "3":
                self.show_summary()

            elif choice == "4":
                self.show_by_category()

            elif choice == "5":
                self.save_data()
                break

            else:
                print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    tracker = FinanceTracker()
    tracker.run()
