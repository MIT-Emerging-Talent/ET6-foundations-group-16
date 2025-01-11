"""
This module contains the BankAccount class, which provides basic banking operations such as deposits and withdrawals.
"""


class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        balance (int): The current balance of the bank account.
        transactions (list): A list of transaction records.
    """

    def __init__(self, initial_balance: int = 0):
        """
        Initialize the bank account with an initial balance.

        Args:
            initial_balance (int): The starting balance of the account. Defaults to 0.
        """
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount: int) -> int:
        """
        Deposit a specified amount into the bank account.

        Args:
            amount (int): The amount to deposit. Must be greater than 0.

        Returns:
            int: The new balance after the deposit.

        Raises:
            ValueError: If the deposit amount is not greater than 0.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        return self.balance

    def withdraw(self, amount: int) -> int:
        """
        Withdraw a specified amount from the bank account.

        Args:
            amount (int): The amount to withdraw. Must be greater than 0 and less than or equal to the current balance.

        Returns:
            int: The new balance after the withdrawal.

        Raises:
            ValueError: If the withdrawal amount is not greater than 0 or exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Withdrawal amount exceeds the current balance.")

        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        return self.balance


# Example doctests
# >>> account = BankAccount(100)
# >>> account.deposit(50)
# 150
# >>> account.withdraw(30)
# 120
# >>> account.balance
# 120
