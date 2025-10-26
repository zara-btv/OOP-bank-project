# custom Exception

class NegativeAmountError(Exception):
    pass
class InsufficientBalanceError(Exception):
    pass

from datetime import datetime
def LogDecorator(func):
    def wrapper(*args, **kwargs):
        time = datetime.now()
        owner =args[0].owner if args else "Unknown"
        try:
            result = func(*args, **kwargs)
            log_status="SUCCESS"
        except Exception as e:
            result=str(e)
            # type of Error
            log_status=f"Exception({type(e).__name__})"
            backup=getattr(args[0],"_backup_balance",None)
            with open("log.txt","a",encoding="utf-8") as file:
                file.write(f"time -->{time}\n")
                file.write(f"owner-->{owner}\n")
                file.write(f"function name-->{func.__name__}\n")
                file.write(f"Status:{log_status}\n")
                file.write(f"Exception -->{e}\n")
                if backup is not None:
                    file.write(f"rollback balance:{backup}\n")
                file.write("-"*100)
            raise
        else:
            with open("log.txt","a") as file:
                file.write(f"time -->{time}\n")
                file.write(f"function name-->{func.__name__}\n")
                file.write(f"Status:{log_status}\n")
                file.write(f"new balance -->{result}\n")
                file.write("-"*100)
            return result


    return wrapper



class BankAccount:

    def __init__(self,owner ,balance):
        self._owner = owner
        self._balance = balance
        self._backup_Balance = balance
    def __enter__(self):
        print(f"Starting transaction for {self.owner}")
        self._balance_backup = self._balance
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Error occured: {exc_type}. Rolling back ...")
            self._balance = self._backup_Balance
            return False
        else:
            print(f"Transaction completed successfully")
            return False

    @classmethod
    def new_account(cls,new):
        owner,balance=new.strip().split("-")
        return cls(owner,int(balance))

    @property
    def owner(self):
        return self._owner
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,value):
        if value<0:
            raise NegativeAmountError("Balance cannot be negative")
        self._balance = value
    @LogDecorator
    def withdraw(self,amount):
        if amount<=0:
            raise NegativeAmountError("amount must be positive")
        if amount>self._balance:
            raise InsufficientBalanceError("amount must be greater than balance")
        self._balance -= amount
        return f"withdraw amount:{amount} and new balance:{self._balance}"
    @LogDecorator
    def deposit(self,amount):
        if amount<=0:
            raise NegativeAmountError("amount must be positive")
        self._balance += amount
        return f"deposit amount:{amount} and new balance:{self._balance}"
    def __str__(self):
        return f"owner:{self.owner}, balance:{self.balance}"

    @staticmethod
    def show_history():
        with open("log.txt","r",encoding="utf-8") as file:
            print(file.read())

    @staticmethod
    def format_currency(amount):
        return f"{amount}$"







account_1=BankAccount("zahra",100)
account_2=BankAccount.new_account("ali - 2000 ")
try:
    with account_1 as a:
        a.withdraw(100)
        a.deposit(10)
except Exception as e:
    print(f"Transaction failed :{e}")

try:
    with account_2 as b:
        b.withdraw(-100)
        b.deposit(3000)
except Exception as e:
    print(f"Transaction failed :{e}")

print(f"Final balance for {account_1.owner}:{account_1.balance}")
account_1.show_history()


