"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Sion Kim
Date: 2024.09.07
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_init_valid(self):
        """ Test for bank account with name mangling """
        bank_account = BankAccount(9836, 1999, 100)
        self.assertEqual(9836, bank_account._BankAccount__account_number)
        self.assertEqual(1999, bank_account._BankAccount__client_number)
        self.assertEqual(100, round(bank_account._BankAccount__balance, 2))

    def test_init_non_numeric_balance_sets_zero(self):
        """ Test for setting balance (" ") """
        bank_account = BankAccount(9836, 1999, " ")
        self.assertEqual(bank_account._BankAccount__balance, 0)

    def test_init_non_numeric_account_number_raises_exception(self):
        """ Test for none numeric account number (" ") """
        with self.assertRaises(ValueError):
            bank_account = BankAccount(" ", 1999, 100)

    def test_init_non_numeric_client_number_raises_exception(self):
        """ Test for none numeric client number (" ") """
        with self.assertRaises(ValueError):
            bank_account = BankAccount(9836, " ", 100)

    def test_account_number_getter_returns_account_number(self):
        """ Test for getter returns account number """
        bank_account = BankAccount(9836, 1999, 100)
        self.assertEqual(9836, bank_account._BankAccount__account_number)

    def test_client_number_getter_returns_client_number(self):
        """ Test for getter returns client number """
        bank_account = BankAccount(9836, 1999, 100)
        self.assertEqual(1999, bank_account._BankAccount__client_number)

    def test_balance_getter_returns_balance(self):
        """ Test for getter returns balance """
        bank_account = BankAccount(9836, 1999, 100)
        self.assertEqual(100, round(bank_account._BankAccount__balance, 2))

    def test_update_balance_received_positive_amount(self):
        """ Test for updating balance received positive amount """
        bank_account = BankAccount(9836, 1999, 100)
        bank_account.update_balance(40)
        self.assertEqual(140, round(bank_account._BankAccount__balance, 2))

    def test_update_balance_redceived_negative_amount(self):
        """ Test for updating balance received negative amount """
        bank_account = BankAccount(9836, 1999, 100)
        bank_account.update_balance(-40)
        self.assertEqual(60, round(bank_account._BankAccount__balance, 2))

    def test_update_balance_received_non_numeric_amount(self):
        """ Test for updating balance received none-numerice amount """
        bank_account = BankAccount(9836, 1999, 100)
        bank_account.update_balance(" ")
        self.assertEqual(100, round(bank_account._BankAccount__balance, 2))

    def test_deposit_updated_valid_amount(self):
        """ Test for deposit valid amount """
        bank_account = BankAccount(9836, 1999, 100)
        bank_account.deposit(30)
        self.assertEqual(130, round(bank_account._BankAccount__balance, 2))

    def test_deposit_provided_negative_amount_raises_exception(self):
        """ Test for deposit negative amount """
        bank_account = BankAccount(9836, 1999, 100)
        with self.assertRaises(ValueError):
            bank_account.deposit(-30)

    def test_withdraw_updated_valid_amount(self):
        """ Test for withdraw valid amount """
        bank_account = BankAccount(9836, 1999, 100)
        bank_account.withdraw(90)
        self.assertEqual(10, round(bank_account._BankAccount__balance, 2))

    def test_withdraw_provided_negative_amount_raises_exception(self):
        """ Test for withdraw negative amount """
        bank_account = BankAccount(9836, 1999, 100)
        with self.assertRaises(ValueError):
            bank_account.withdraw(-90)

    def test_withdraw_provided_exceeds_balance_raises_exception(self):
        """ Test for withdraw exceed amount """
        bank_account = BankAccount(9836, 1999, 100)
        with self.assertRaises(ValueError):
            bank_account.withdraw(900)

    def test_retunrs_str_bank_account(self):
        """ Test for return expected str format """
        bank_account = BankAccount(9836, 1999, 100)
        self.assertEqual("Account Number: 9836 Balance: $100.00", str(bank_account))