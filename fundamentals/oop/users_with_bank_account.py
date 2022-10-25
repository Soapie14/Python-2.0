class BankAccount:
    bank_name = "The Bank"
    all_accounts = ['Sophie', 'Nico']
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance:", self.balance)
        return self
        # your code here
    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough funds. You currently have $", (self.balance))
        else:
            self.balance = self.balance - amount
            print("Your current balance is", (self.balance))
        return self
    def display_account_info(self):
        print("Balance:", self.balance)
        print("Interest rate:", self.int_rate)
        return self
    def yield_interest(self):
        if self.balance < 0:
            print("Insufficient funds")
        else:
            self.balance = self.balance + (self.balance * self.int_rate)
            print("Balance:", self.balance)
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=100)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        # print(self.account.balance)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        # print(self.account.balance)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    def new_account(self, int_rate, balance):
        pass


Sophie = User('Sophie', 'Email@l.com')
Nico = User('Nico', 'n@s.com')

Sophie.make_deposit(10).make_withdrawal(2).display_user_balance()
Nico.make_deposit(10)