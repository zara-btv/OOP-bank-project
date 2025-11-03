import csv
from datetime import datetime
from core.decorators import logdecorator
from core.errors import NegativeAmountError,InsufficientAmountError
# ---------------------------------------------------------------------------
class Accounts:
    def __init__(self, owner, balance):
        self._owner=owner
        self._balance=balance
        self._backup_balance=balance
    # context manager
    def __enter__(self):
        print(f"Start transition for {self._owner}")
        self._backup_balance=self._balance
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
                print(f"⚠️ Error occurred: {exc_val}. Rolling back ...")
                self._balance = self._backup_balance
        else:
            print("✅ Transaction completed successfully.")
            return False
    @property
    def owner(self):
        return self._owner
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        self._balance=value
    @logdecorator
    def withdraw(self, amount):
        if amount<0:
            raise NegativeAmountError
        if amount > self._balance:
            raise InsufficientAmountError
        self._balance-=amount
        result=self._balance
        with open("../data/transaction.csv", "a", newline="", encoding="utf-8") as f:
            fieldnames=["owner","action","amount","date","balance"]
            writer=csv.DictWriter(f,fieldnames=fieldnames)
            if f.tell()==0:
                writer.writeheader()

            writer.writerow({"owner":self._owner,"action":"Withdraw","amount":amount,"date":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"balance":result})
        return self._balance

    @logdecorator
    def deposit(self,amount):
        if amount<0:
            raise NegativeAmountError
        self._balance+=amount
        result=self._balance
        with open("../data/transaction.csv", "a", newline="", encoding="utf-8") as f:
            fieldnames = ["owner", "action", "amount", "date", "balance"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if f.tell() == 0:
                writer.writeheader()

            writer.writerow({"owner": self._owner, "action": "Deposit", "amount": amount,
                             "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "balance": result})
        return self._balance
    def show(self):
        print(f"owner: {self._owner}, balance: {self._balance}")
    def __str__(self):
        return f"Account(owner={self._owner},balance={self._balance})"
    def __repr__(self):
        return self.__str__()
    def to_dict(self):
        return {
            "owner":self._owner,
            "balance":self._balance
        }