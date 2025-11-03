
import json, pickle
from models.Account import Accounts
from core.decorators import logdecorator


class Bank:
    def __init__(self, name):
        self._name = name
        self._bank_accounts=[]
    @logdecorator
    def add_account(self, account):
        if not any(acc.owner==account.owner for acc in self._bank_accounts):
            self._bank_accounts.append(account)
        else:
            raise Exception("this account already exists")

    @classmethod
    def new_account(cls,account_owner):
        owner,balance=account_owner.strip().split("-")
        new_acc=Accounts(owner, int(balance))
        return new_acc

    def show(self):
        print(f"Bank Name: {self._name}")
        if self._bank_accounts:
            for acc in self._bank_accounts:
                print(acc.owner, acc.balance,"\n")
        else:
            raise Exception(f"There are no bank accounts yet")
    # account.json for saving accounts
    def save_to_json(self,filename="account.json"):
        data=[acc.to_dict()for acc in self._bank_accounts]
        with open(filename,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)

    @classmethod
    def load_from_json(cls, filename="account.json"):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        bank = cls("Meli")
        for acc_data in data:
            acc = Accounts(acc_data["owner"], acc_data["balance"])
            bank.add_account(acc)
        return bank
    def save_pickle(self,filename="bank.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
    @staticmethod
    def load_pickle(filename="bank.pkl"):
        with open(filename, "rb") as f:
            return pickle.load(f)