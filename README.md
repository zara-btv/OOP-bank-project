# 🏦 Advanced BankAccount System in Python
This project is an enhanced Object-Oriented Programming (OOP) system simulating a bank, now with transaction logging, context-managed transactions, and safe attribute handling.
## Features
- Manage customer accounts with balance tracking 
- Deposit and withdraw operations with validation
- Automatic transaction logging using a custom **@LogDecorator** 
- Context-managed transactions (with statement) with automatic rollback on errors
- Encapsulated attributes using **@property**, **@setter**, and **@deleter**
- Create new accounts with **@classmethod** factory method
- Display bank name shared across all accounts via **@classmethod**
- Custom exceptions for invalid operations (NegativeAmountError, InsufficientBalanceError)

# 🧠 Concepts Covered
- @property for controlled attribute access
- @classmethod for class-level logic and factory methods
- @staticmethod for utility methods
- Custom decorators for logging function calls
- Context Manager (__enter__ and __exit__) for safe transactions
- File handling (log.txt) for transaction history

## Example Usage
```python
from Bank_account_system import BankAccount
account = BankAccount("Zahra Betvan", 1000)
# Context-managed transactions
with account as acc:
    acc.deposit(500)
    acc.withdraw(200)

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
[2025-10-22 11:45:33] owner: Zahra Betvan
  function: deposit
  status: SUCCESS
  result: deposit amount:500 and new balance:1500
------------------------------------------------------------

[2025-10-22 11:46:12] owner: Zahra Betvan
  function: withdraw
  status: EXCEPTION (InsufficientBalanceError)
  error: amount must be greater than balance
  rollback balance: 1500
------------------------------------------------------------

```
# 🧩 Future Improvements
- Command-line interface (CLI) for interactive banking
- Additional validation for input data
- Reporting and transaction summaries
- Multi-account management per user

# 🧑‍💻 Author
**Zahra Betvan**
Learning Python step by step with focus on OOP, clean code, and real-world design patterns.