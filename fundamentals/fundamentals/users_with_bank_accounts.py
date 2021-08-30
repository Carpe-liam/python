class BankAccount:
    bank_name = "Karma Kredit"
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
            return self

    def display_account_info(self):
        print("Balance: " + str(self.balance))

    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) < 0:
            return False
        else:
            return True

    @classmethod
    def all_balances(cls):
        sum =0
        for account in cls.all_accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "Checking": BankAccount(int_rate=0.1, balance=100),
            "Savings": BankAccount(int_rate=0.12, balance=2500)
        }

    def make_deposit(self, amount):
        self.account.balance += amount

    def make_withdrawal(self, amount):
        self.account.balance -= amount
    
    def display_user(self):
        print("User: " + self.name + ", Balance: $" + str(self.account.balance))
    
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        print("User: " + self.name + ", Balance: $" + str(self.account.balance))
        print("User: " + other_user.name + ", Balance: $" + str(other_user.account.balance))

bob = User("Bob Banana", "bBananas@fruits.rs")
bob.account["Savings"].yield_interest()
bob.account["Checking"].display_account_info()
bob.account["Savings"].display_account_info()
