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
        print("Balance: " + str(self.balance) + " Interest Rate: " + str(self.int_rate))


    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) < 0:
            return False
        else:
            return True

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()
################################################

bob = BankAccount(0.05, 200)
frank = BankAccount(0.1, 420)

bob.deposit(200).deposit(200).deposit(600).withdraw(150).yield_interest().display_account_info()

frank.deposit(6000).deposit(500).withdraw(150).withdraw(250).withdraw(1250).withdraw(110).yield_interest().display_account_info()

BankAccount.all_balances()