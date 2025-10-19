class BankAccount():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"
    def deposit(self,count):
        new_balance=count+self.balance
        self.balance=new_balance
        return new_balance
    def withdraw(self,count):
        if count<self.balance:
            new_balance=self.balance-count
            self.balance=new_balance
        else:
            print("there is not enough money!!")
    def show_balance(self):
        print(f"{self.owner} has {self.balance}$.")


class Bank():
    def __init__(self,bank_name):
        self.name=bank_name
        self.accounts=[]
    def add_account(self,account):
        self.accounts.append(account)
        print(f"Account '{account.owner}' added.")
    def remove_account(self,account):
        if self.accounts.__contains__(account):
            self.accounts.remove(account)
        else:
            print("account not exist")
    def show_balance(self):
        print(f"Accounts in bank '{self.name}':")
        if not self.accounts:
            print("No accounts in bank")
        else:
            for account in self.accounts:
                print(f"Account '{account.owner} has {account.balance}$.")

bank_1=Bank("MELI")
p1=BankAccount("Zahra",1000)
p2=BankAccount("Ali",2000)
p3=BankAccount("Rozita",3000)
bank_1.add_account(p1)
bank_1.add_account(p2)
bank_1.add_account(p3)
bank_1.remove_account(p3)
bank_1.show_balance()
bank_1=Bank("AYANDE")
print("*"*70)
p1=BankAccount("Ziba",1000)
p2=BankAccount("Ramin",2000)
p3=BankAccount("Aram",3000)
bank_1.add_account(p1)
bank_1.add_account(p2)
bank_1.add_account(p3)
bank_1.remove_account(p3)
bank_1.show_balance()
