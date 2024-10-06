""""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: Apurba Khan
Date: 2024.09.23
"""
from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Transaction classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.

    print("-" * 100)

    try:
        client = Client(None, "Apurba", "Khan", "mkhan14@rrc.ca")
    except ValueError as e:
        print(e)
    
    try:
        client = Client(1999, " ", "Khan", "mkhan14@rrc.ca")
    except ValueError as e:
        print(e)

    try:
        client = Client(1999, "Apurba", " ", "mkhan14@rrc.ca")
    except ValueError as e:
        print(e)

    try:
        client = Client(1999, "Apurba", "Khan", "mkhan14@rrc.ca")
    except ValueError as e:
        print(e)

    print("-"*100)

    # 2. Declare a BankAccount object with an initial value of None.

    bank_account = None

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    """ Main Balance: $100 """
    try:
        bank_account = BankAccount(9836, client._Client__client_number, 100)
    except ValueError as e:
        print(e)
    print("Balance: $100")
    
    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    """ Invalid Demo Balance: $0 """
    try:
        invalid_bank_account = BankAccount(9836, client._Client__client_number, " ")
    except ValueError as e:
        print(e)

    print("-"*100)

    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.

    print(client)
    print(bank_account)

    print("-"*100)

    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 

    try:
        bank_account.deposit("text")
    except ValueError as e:
        print(e)

    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 

    try:
        bank_account.deposit(-30)
    except ValueError as e:
        print(e)

    print("-"*100)

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
    """ Main Balance: $10 = 100 - 90 """
    try:
        bank_account.withdraw(90)
    except ValueError as e:
        print(e)

    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 

    try:
        bank_account.withdraw("text")
    except ValueError as e:
        print(e)

    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 

    try:
        bank_account.withdraw(-30.0)
    except ValueError as e:
        print(e)

    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
 
    try:
        bank_account.withdraw(900)
    except ValueError as e:
        print(e)

    print("-"*100)

    # 12. Code a statement which prints the BankAccount instance created in step 3. 

    print(bank_account)

if __name__ == "__main__":
    main()