class BankAccount:
    def __init__(self, acc_num, balance=0):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return "Deposit successful"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return "Withdrawal successful"
        return "Insufficient funds or invalid amount"

    def display(self):
        return f"Account Number: {self.acc_num}, Balance: {self.balance}"

acc = BankAccount(123456, 500)
print(acc.deposit(200))
print(acc.withdraw(100))
print(acc.display())
    