# Create a class BankAccount with deposit and withdraw methods.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
acc = BankAccount()
acc.deposit(1000)
acc.withdraw(500)
print("Balance:", acc.balance)