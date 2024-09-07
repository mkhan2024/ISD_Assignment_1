"""
Description: A class to manage BankAccount objects.
Author: Sion Kim
Date: 2024.09.07
"""

class BankAccount:
    """
    A class for bank account.

    Attributes:
        account_number (int): The account_number of the bank account.
        client_number (int): The client_number of the bank account.
        balance (float): The balance of the bank account.
    """
    def __init__(self, account_number: int, client_number: int, balance: float):
        """
        A method for client's attributes.

        Args:
            account_number (int): numeric
            client_number (int): numeric.
            balance (float): float.

        Returns:
            data type: The return value. Describe what each return value may indicate.

        Raises:
            ValueError (account_number: non-numeric
                        client_number: non-numeric
                        balance: non-numeric -> 0).
        """
        if not isinstance(account_number, int):
            raise ValueError("account_number must be numeric.")
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("client_number must be numeric.")
        self.__client_number = client_number

        if isinstance(balance, (int, float)):
            self.__balance = float(balance)
        else:
            self.__balance = 0
            print("Balance: $0")
        
    @property
    def account_number(self) -> int:
        """
        Returns:
            int: The account_number.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Returns:
            int: The client_number.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Returns:
            float: The balance.
        """
        return self.__balance

    def update_balance(self, amount: float) -> None:
        """ 
        Update the balance by adding.

        Args:
            amount (float): Add to balance

        Raises:
            ValueError (amount: non-numeric).
            TypeError (amount: invalid type).
        """
        try:
            amount = float(amount)
            self.__balance += amount
        except (ValueError, TypeError):
            pass 

    def deposit(self, amount: float) -> None:
        """ 
        Deposit.

        Args:
            amount (float): amount for deposit

        Raises:
            ValueError (amount: non-numeric
                        amount: negative).
        """
        if not isinstance(amount, (float, int)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount} must be positive.")

        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """ 
        withdraw.

        Args:
            amount (float): amount for withdraw

        Raises:
            ValueError (amount: non-numeric
                        amount: negative
                        amount: exceed).
        """
        if not isinstance(amount, (float, int)):
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")

        if amount <= 0:
            raise ValueError(f"Withdrawal amount: {amount:,.2f} must be positive.")

        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: {amount:,.2f} must not exceed the account balance: {self.__balance:,.2f}")

        self.update_balance(-amount)


    def __str__(self) -> str:
        """
        A method for return a string.

        Returns:
            str: account_number, balance.
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"

