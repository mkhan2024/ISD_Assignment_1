# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
Apurba Khan

## Assignment
### Assignment 01: `Classes`, `Encapsulation` and `Unit Test Planning` 
- Through this assignment, I incorporate encapsulation and get used to unit test planning.

## Encapsulation
- Encapsulation was implemented in the `BankAccount` and `Client` classes through private attributes, methods, and `@property` decorators to controlled access.
### Private Attribute (Client)
- `__client_number`, `__first_name`, `__last_name`, `__email_address`.
### Private Attribute (BankAccount)
- `__account_number`, `__client_number`, `__balance`.
### Methods (BankAccount, Transaction)
- `update_balance`, `deposit`, `withdraw`.
### Sum Up
- `@property` for `__client_number`, `__first_name`, `__last_name`, `__email_address`: Provide access for reading to private attributes in the Client class.
- Reasons: `Client` information is not changed frequently.
- `@property` for `__account_number`, `__client_number`, `__balance`: Provide access for reading to private attributes but also provide controlled access to the private attributes through methods.
- Reasons: `BankAccount` transaction information is changed frequently.