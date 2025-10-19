# 🏦 Simple Bank System in Python

This is a beginner-friendly **Object-Oriented Programming (OOP)** project that simulates a simple banking system.

## Features
- Add and remove bank accounts  
- Deposit and withdraw money  
- Display all accounts in a bank  

## Example
```python
bank_1 = Bank("MELI")
p1 = BankAccount("Zahra", 1000)
p2 = BankAccount("Ali", 2000)

bank_1.add_account(p1)
bank_1.add_account(p2)
bank_1.show_balance()
