# 🏦 Advanced BankAccount System in Python

This project is an enhanced version of a simple bank system, rewritten to demonstrate **Object-Oriented Programming (OOP)** concepts and the use of **decorators**, **class methods**, and **properties** in Python.
## Features
- Manage customer accounts with balance tracking
- Deposit and withdraw operations with validation
- Automatic transaction logging using a custom @logdecorate decorator
- Encapsulated attributes with @property, @setter, and @deleter
- Create new accounts using @classmethod (factory method style)
- Display the bank name shared across all accounts via @classmethod 

# 🧠 Concepts Covered
- @property — for controlled attribute access
- @classmethod — for class-level logic and factory methods
- Custom decorators for logging function calls
- File handling (log.txt) for transaction history

## Example Usage
```python
from Bank_account_system import BankAccount
# Create an account
account = BankAccount("Zahra Betvan", 1000)

# Deposit and withdraw money
account.deposit(500)
account.withdraw(200)

# Show balance
print(account.balance)

# Update balance safely
account.balance = 200

# Create a new account using classmethod
account_str = "Fati-2000"
new_acc = BankAccount.new_account(account_str)
print(new_acc.owner)

# Display shared bank name
BankAccount.show_bank_name()

```
# 🧾 Log File Example
```text
time --> 2025-10-22 11:45:33
name of the function --> deposit
owner --> Zahra Betvan
Args --> (500,)
kwargs --> {}
value --> 1500
# --------------------------------------------------
```
# 🧩 Future Improvements
- Add JSON storage for saving and loading accounts
- Implement a command-line interface
- Add error handling for invalid data inputs

# 🧑‍💻 Author

Zahra Betvan
Learning Python step by step with focus on OOP and clean code.