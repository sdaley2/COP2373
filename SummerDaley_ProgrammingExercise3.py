from functools import reduce

def analyze_expenses(expenses):
    """Calculate the total, highest, and lowest monthly expenses."""

    # Add all the monthly expense amounts together.
    total_expense = reduce(
        lambda total, expense: total + expense["amount"],
        expenses,
        0.0
    )

    # Find the expense with the highest amount.
    highest_expense = reduce(
        lambda highest, expense: expense
        if expense["amount"] > highest["amount"] else highest,
        expenses
    )

    # Find the expense with the lowest amount.
    lowest_expense = reduce(
        lambda lowest, expense: expense
        if expense["amount"] < lowest["amount"] else lowest,
        expenses
    )

    return total_expense, highest_expense, lowest_expense

def main():
    """Run the monthly expense calculator."""

    expenses = []

    # Continue asking the user to enter monthly expenses.
    while True:
        expense_type = input(
            "Enter the expense type (or 'done' to finish): "
        )

        # Stop collecting expenses when the user enters done.
        if expense_type.lower() == "done":
            break

        # Prevent the user from entering an empty expense name.
        if not expense_type.strip():
            print("Please enter an expense type.")
            continue

        # Get the amount for the current expense.
        try:
            amount = float(input("Enter the expense amount: $"))

            if amount < 0:
                print("Please enter an amount of zero or more.")
                continue

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        # Store the expense name and amount in the list.
        expenses.append({
            "type": expense_type,
            "amount": amount
        })

        print("Expense added successfully.\n")

    # Calculate and display the results if expenses were entered.
    if expenses:
        total_expense, highest_expense, lowest_expense = analyze_expenses(
            expenses
        )

        print("\nMONTHLY EXPENSE SUMMARY")
        print("----------------------------")

        print(f"Total Expenses: ${total_expense:.2f}")

        print(
            f"Highest Expense: {highest_expense["type"]} - "
            f"${highest_expense['amount']:.2f}"
        )

        print(
            f"Lowest Expense: {lowest_expense["type"]} - "
            f"${lowest_expense['amount']:.2f}"
        )

    else:
        print("No expenses were entered to analyze.")

if __name__ == "__main__":
    main()
