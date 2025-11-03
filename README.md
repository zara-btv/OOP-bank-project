# 🏦 Advanced Bank System (Python)

An object-oriented mini banking system demonstrating real-world patterns: context-managed transactions, structured logging, persistence (JSON / CSV / pickle), custom exceptions, and small utilities.

---

## ⚙️ Features
- Create and manage accounts (`Accounts`) inside a `Bank` container  
- Deposit / Withdraw with validation and custom exceptions (`NegativeAmountError`, `InsufficientAmountError`)  
- Context-managed transactions (`with account:`) — automatic rollback on error  
- Structured JSON logging (`log.json`) via a `@logdecorator` (records success and exceptions)  
- CSV transaction ledger (`transactions.csv`) — owner, action, amount, date, balance  
- Persist accounts: save / load accounts to/from JSON (`accounts.json`)  
- Fast snapshot persistence with `pickle` (`bank.pkl`) — quick save / load of full objects  
- Utilities: pretty `__str__/__repr__`, `to_dict()` for serialization, and formatting helpers

---

## 🧭 Quick concepts (covered)
- `@property`, `@setter` for controlled attributes  
- `@classmethod` (factory) for easy account creation (`new_account`)  
- `@staticmethod` helpers (e.g. currency format)  
- Custom decorators for structured logging  
- Context manager (`__enter__`, `__exit__`) for safe transactions  
- File IO: JSON / CSV / binary (pickle)

---

## 📦 Installation / Requirements
No external packages required — pure Python 3 (recommended 3.8+).

Clone your repo and run with Python:
```bash
git clone <your-repo-url>
cd <your-project-folder>
python main.py   # or run your script file (e.g. sheet.py / bank.py)
```
# Example Usage

```python

from models.Account import Accounts
from models.Bank import Bank

# create accounts
a1 = Accounts("Arya", 1000)
a2 = Accounts("Fati", 1200)

# bank and add accounts
bank = Bank("Meli Bank")
bank.add_account(a1)
bank.add_account(a2)

# deposit / withdraw with logging + CSV ledger
a1.deposit(500)
try:
    with a1 as t:
        t.withdraw(300)
        t.withdraw(2000)  # will raise InsufficientAmountError and rollback
except Exception as e:
    print("Transaction failed:", e)

# persistence
bank.save_to_json("accounts.json")  # stores accounts as list of dicts
loaded = Bank.load_from_json("data/accounts.json")
loaded.show()

# fast snapshot
bank.save_pickle("bank.pkl")
snapshot = Bank.load_pickle("data/bank.pkl")

# show CSV and log files created:
# - transactions.csv  (append-only ledger for deposits/withdrawals)
# - log.json          (structured log of all decorated calls)

```
# 🧾 Logging examples
```tetx
[
  {
    "time": "2025-11-02 17:48:55.861995",
    "owner": "Arya",
    "function_name": "withdraw",
    "args": [
      {"owner": "Arya", "balance": 900},
      100
    ],
    "result": 900,
    "status": "SUCCESS"
  },
  {
    "time": "2025-11-02 17:48:55.862993",
    "owner": "Arya",
    "function_name": "withdraw",
    "args": [
      {"owner": "Arya", "balance": 1000},
      1000
    ],
    "status": "EXCEPTION",
    "exception": "InsufficientAmountError: amount must be greater than balance",
    "rollback": 1000
  }
]
```
# 💾 Persistence details
## JSON (human-readable)
- Bank.save_to_json(filename="accounts.json")
- saves a list of simple dicts: [{ "owner": "...", "balance": ... }, ...].
- Bank.load_from_json(filename="accounts.json")
- returns a Bank instance populated with Accounts objects built from the file.
## CSV (transactions)
- transactions.csv is append-only. Each deposit/withdraw writes a row.
- Use csv.DictWriter, write header only when the file is empty (if f.tell() == 0).
## Pickle (fast snapshot)
- Bank.save_pickle("bank.pkl") — stores the entire Bank object (binary).
- Bank.load_pickle("bank.pkl") — returns the pickled Bank object.
- Security note: never pickle.load() files from untrusted sources.

# 🧰 Project structure 
bank_project/
│
├─ main.py                      
│
├─ core/
│   ├─ errors.py                
│   ├─ decorators.py            
│
├─ models/                      
│   ├─ Account.py               
│   └─ Bank.py                  
│
├─ data/                      
│   ├─ log.json
│   ├─ transactions.csv
│   ├─ account.json
│   └─ bank.pkl
│
└─ README.md

# ✅ Next steps / TODO
- Add CLI for account management (create, deposit, withdraw, save, load)
- Add unit tests for exceptions, persistence, serialization
- move project into a package (src/), add type hints and docstrings
# 👩‍💻 Author
Zahra Betvan — Learning Python step by step with focus on OOP, clean code, and real-world patterns.