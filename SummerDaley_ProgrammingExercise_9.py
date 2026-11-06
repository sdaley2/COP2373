class BankAcct:
    """Represent a bank account."""

    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        """Change the interest rate."""
        self.interest_rate = new_rate

    def deposit(self, amount):
        """Add money to the account."""
        self.amount += amount

    def withdraw(self, amount):
        """Remove money from the account if enough funds are available."""
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        """Return the current balance of the account."""
        return self.amount

    def calculate_interest(self, days):
        """Calculate interest rate based on the number of days."""
        interest = self.amount * self.interest_rate* (days / 365)
        return interest

    def __str__(self):
        """Display the account balance and interest rate."""
        return(
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.amount: .2f}\n"
            f"Interest Rate: {self.interest_rate: .2%}"
        )

def test_bank_account():
    """Test the methods in the BankAcct class."""

    account = BankAcct("Summer Daley", "123456789", 1000.00, 0.05)

    print("Original Account Information")
    print(account)

    account.deposit(500.00)
    print("\nAfter Deposit")
    print(f"Balance: ${account.get_balance(): .2f}")

    account.withdraw(200.00)
    print("\nAfter Withdrawal")
    print(f"Balance: ${account.get_balance(): .2f}")

    account.adjust_interest_rate(0.06)
    print("\nAfter Interest Rate Adjustment")
    print(account)

    interest = account.calculate_interest(30)
    print("\nInterest for 30 Days")
    print(f"Interest Amount: ${interest: .2f}")

if __name__ == "__main__":
    test_bank_account()