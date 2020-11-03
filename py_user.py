class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
        print('User: ', self.name, ', Balance: ', self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print('User 1: ', self.name, ', Balance: ', self.account_balance)
        print('User 2: ', other_user.name, ', Balance: ', other_user.account_balance)
        

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
johni = User("Johni Than", "jonithan@python.com")
print(johni.name)

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(25)
guido.make_withdrawl(350)  
guido.display_user_balance()


monty.make_deposit(150)
monty.make_deposit(375)
monty.make_withdrawl(400)
monty.display_user_balance()

johni.make_deposit(825)
johni.make_withdrawl(175)
johni.make_withdrawl(300)
johni.make_withdrawl(65)
johni.display_user_balance()


johni.transfer_money(guido, 100)


# =================