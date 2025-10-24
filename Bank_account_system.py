from datetime import datetime

def logdecorate(func):
    def wrapper(*args, **kwargs):
        time=datetime.now()
        value=func(*args, **kwargs)
        owner =args[0]._owner if args else "Unknown"
        with open("log.txt","a")as file:
            name=func.__name__
            file.write(f"time-->{time}"+"\n")
            file.write(f"name of the function -->{name}\n")
            file.write(f"owner -->{owner}"+"\n")
            file.write(f"Args-->{args[1:]}"+"\n")
            file.write(f"kwargs-->{kwargs}"+"\n")
            file.write(f"value-->{value}"+"\n")
            file.write("-"*50+"\n")
        return value
    return wrapper


class BankAccount():
    bank_name="Mali Bank"
    def __init__(self,owner,balance):
        self._owner=owner
        self._balance=balance
    #     to show the balance
    @classmethod
    def new_account(cls,account_string):
        owner,balance=account_string.split("-")
        return cls(owner,int(balance))

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        print(f"{self._owner}'s balance is {self._balance}")
        return self._balance

    @balance.setter
    # here I use validation for set the balance
    def balance(self,amount):

        if amount<0:
            print("balance cannot be negative")
        elif amount==0:
            print("balance cannot be zero")
        else:
            self._balance=amount
    # @balance.deleter
    # def balance(self):
    #     del self._balance
    #     --------------------
    @logdecorate
    def deposit(self,amount):
        if amount<=0:
            print("It is not possible to deposit a negative amount.")
            return
        else:
            self._balance+=amount
            print("Deposited amount:",self._balance)
            return self._balance
    #         ------------------------
    @logdecorate
    def withdraw(self,amount):
        if amount>self._balance:
            print("It is not possible because the amount is greater than the balance.")
            return
        else:
            self._balance-=amount
            print("Withdrawed amount:",self._balance)
            return self._balance
    @classmethod
    def show_bank_name(cls):
        print(f"This account belongs to {cls.bank_name}")

    def __str__(self):
        return f"{self._owner}'s balance is {self._balance}"



account=BankAccount("Zahra Betvan",1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)
account.balance=200
print(account.balance)
BankAccount.show_bank_name()
Account="fati-2000"
account=BankAccount.new_account(Account)
print(account.owner)

