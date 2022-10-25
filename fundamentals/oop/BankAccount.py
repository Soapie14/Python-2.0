class BankAccount:
    bank_name = "The Bank"
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
    
    
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

nico= BankAccount(0.02, 500)
sophie = BankAccount(0.03, 100)

# sophie.deposit(10)
# sophie.withdraw(5)
# sophie.display_account_info()
# sophie.yield_interest()


# sophie.deposit(10).deposit(3).deposit(1).withdraw(2).yield_interest().display_account_info()
# nico.deposit(10).deposit(5).withdraw(20).withdraw(10).withdraw(4).withdraw(3).yield_interest().display_account_info()

