class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user(self):
        print("User: " + self.name + ", Balance: $" + str(self.account_balance))
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("User: " + self.name + ", Balance: $" + str(self.account_balance))
        print("User: " + other_user.name + ", Balance: $" + str(other_user.account_balance))

bob = User("Bob Banana", "bBanana@peel.com")
frank = User("Frank Flintstone", "flinty@vitamin.com")
earl = User("Earl Grey", "earl@crapTea.com")

bob.make_deposit(200)
bob.make_deposit(1000)
bob.make_withdrawal(100)
bob.make_deposit(50)
bob.display_user()

frank.make_deposit(328912)
frank.make_deposit(43234)
frank.make_withdrawal(2345)
frank.make_withdrawal(23893)
frank.display_user()

earl.make_deposit(12384)
earl.make_withdrawal(483)
earl.make_withdrawal(8413)
earl.make_withdrawal(21)
earl.display_user()

frank.transfer_money(bob, 21000)
frank.display_user()
bob.display_user()