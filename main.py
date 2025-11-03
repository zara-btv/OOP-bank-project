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
bank.save_to_json("accounts.json")    # stores accounts as list of dicts
loaded = Bank.load_from_json("data/accounts.json")
loaded.show()

# fast snapshot
bank.save_pickle("bank.pkl")
snapshot = Bank.load_pickle("data/bank.pkl")

# show CSV and log files created:
# - transactions.csv  (append-only ledger for deposits/withdrawals)
# - log.json          (structured log of all decorated calls)
