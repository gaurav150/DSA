class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Add funds to the account."""
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtract funds from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError("Insufficient funds for withdrawal.")
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def transfer(self, other_account, amount):
        """Transfer funds from this account to another account."""
        if amount > 0:
            if amount <= self.balance:
                self.withdraw(amount)  # Withdraw from this account
                other_account.deposit(amount)  # Deposit to the other account
            else:
                raise ValueError("Insufficient funds for transfer.")
        else:
            raise ValueError("Transfer amount must be positive.")

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    acc1 = BankAccount("John Doe", 1000)
    acc2 = BankAccount("Jane Smith", 2000)
    assert acc1.balance == 1000
    assert acc2.balance == 2000
    acc1.deposit(500)
    acc2.withdraw(100)
    acc1.transfer(acc2, 200)
    assert acc1.balance == 1300
    assert acc2.balance == 2300

    # Test Case 2
    acc3 = BankAccount("Alice Johnson", 500)
    acc4 = BankAccount("Bob Brown", 1500)
    assert acc3.balance == 500
    assert acc4.balance == 1500
    acc3.deposit(100)
    acc4.withdraw(200)
    acc3.transfer(acc4, 300)
    assert acc3.balance == 400
    assert acc4.balance == 1800

    print("All test cases passed!")