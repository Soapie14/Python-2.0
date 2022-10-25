# attributes do not need the self before our variations, but we may still need to pass in (cls) when self is not used

class BankAccount:
    # Declaring a class attribute
    # Shared among all bank accounts
    bank_name = "First National Dojo"		
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        
adriensAccount = BankAccount(7, 10)
sadiesAccount = BankAccount(10, 2)

adriensAccount.bank_name = "Dojo Credit Union"
    
print(adriensAccount.bank_name)
# output: Dojo Credit Union
    
print(sadiesAccount.bank_name)
# output: First National Dojo

BankAccount.bank_name = "Bank of Dojo"
    
print(adriensAccount.bank_name)
# output: Bank of Dojo
    
print(sadiesAccount.bank_name)
# output: Bank of Dojo



#USING @classmethod- They belong to the class itself instead of the instance. Instead of implicitly passing self into the method, we pass cls. This is reference to the class. Class methods have no access to the instance attribute or any attribute that starts with self.


class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []
    
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    
    
#USING @staticmethod -They have no access on instance or class attributes, so if we need any existing values, they need to be passed in as arguments.

class BankAccount:
    # ... __init__ goes here
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True