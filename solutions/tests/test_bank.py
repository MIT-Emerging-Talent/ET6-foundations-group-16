#!/usr/bin/env python3
"""
Unit tests for the BankAccount class.
"""

import unittest

from bank import BankAccount

"""
    Test cases for the BankAccount class.
    """


def test_initial_balance(self):
    """
    Test if the initial balance is set correctly.
    """
    initial_balance = 100
    account = BankAccount(initial_balance)
    assert account.balance == 100, "Initial balance should be 100"


def test_deposit(self):
    """
    Test deposit functionality.
    """
    initial_balance = 100
    account = BankAccount(initial_balance)
    account.deposit(50)
    assert account.balance == 150, "Balance after deposit should be 150"


def test_withdraw(self):
    """
    Test withdraw functionality.
    """
    initial_balance = 100
    account = BankAccount(initial_balance)
    account.withdraw(30)
    assert account.balance == 70, "Balance after withdrawal should be 70"


def test_deposit_transaction(self):
    """
    Test if deposit transaction is recorded correctly.
    """
    initial_balance = 100
    account = BankAccount(initial_balance)
    account.deposit(50)
    assert (
        account.transactions[-1] == "Deposited 50"
    ), "Last transaction should be 'Deposited 50'"


def test_withdraw_transaction(self):
    """
    Test if withdrawal transaction is recorded correctly.
    """
    initial_balance = 100
    account = BankAccount(initial_balance)
    account.withdraw(30)
    assert (
        account.transactions[-1] == "Withdrew 30"
    ), "Last transaction should be 'Withdrew 30'"


if __name__ == "__main__":
    unittest.main()
