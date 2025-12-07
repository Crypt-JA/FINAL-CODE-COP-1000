# Personal Expense Tracker - Final Project

# List to store expenses
expenses = []


# Function to add a new expense
def add_expense():
    try:
        person = input("Enter your name: ").strip()
        name = input("Purchase: ").strip()
        amount = float(input("Amount: $").strip())

        expenses.append({
            "person": person,
            "name": name,
            "amount": amount
        })

        print(f"Added ${amount} for {name} under {person}")
    except ValueError:
        print("Error: amount must be a number.")
    input("\nPress Enter to return to the menu...")


# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\n--- Expenses ---")
        for i, e in enumerate(expenses, 1):
            print(f"{i}. {e['name']} (${e['amount']}) — {e['person']}")
        print("----------------")
    input("\nPress Enter to return to the menu...")


# Function to view unique users (people who entered expenses)
def view_payees():
    if not expenses:
        print("No users recorded yet.")
    else:
        people = sorted({e['person'] for e in expenses})
        print("\n--- Users ---")
        for p in people:
            print("-", p)
        print("-------------")
    input("\nPress Enter to return to the menu...")


# Function to calculate total spending
def total_spent():
    total = sum(e['amount'] for e in expenses)
    print(f"\nTotal spent: ${total}")
    input("\nPress Enter to return to the menu...")


# Main menu loop
while True:
    print("\n*** Expense Tracker Menu ***")
    print("1) Add a new expense")
    print("2) View current expenses")
    print("3) View users")
    print("4) View total of all expenses")
    print("5) Quit program")

    choice = input("Enter choice: ").strip()

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        view_payees()
    elif choice == '4':
        total_spent()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number 1-5.")
        input("\nPress Enter to return to the menu...")