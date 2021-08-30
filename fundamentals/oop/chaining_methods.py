class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user(self):
        print("User: " + self.name + ", Balance: $" + str(self.account_balance))
        return self
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("User: " + self.name + ", Balance: $" + str(self.account_balance))
        print("User: " + other_user.name + ", Balance: $" + str(other_user.account_balance))

bob = User("Bob Banana", "bBanana@peel.com")
frank = User("Frank Flintstone", "flinty@vitamin.com")
earl = User("Earl Grey", "earl@crapTea.com")

bob.make_deposit(200).make_deposit(1000).make_withdrawal(100).make_deposit(50).display_user()

frank.make_deposit(328912).make_deposit(43234).make_withdrawal(2345).make_withdrawal(23893).display_user()

earl.make_deposit(12384).make_withdrawal(483).make_withdrawal(8413).make_withdrawal(21).display_user()

frank.transfer_money(bob, 21000)