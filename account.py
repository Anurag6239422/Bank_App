import random


class Create_Account:
    def __init__(self, name, balance, account_number=None):
        self.name = name
        self.balance = int(balance)
        if account_number is None:
            self.account_number = self.create_account_number()
        else:
            self.account_number = str(account_number)

    def create_account_number(self):
        digits = [str(random.randint(1, 9))]
        for _ in range(15):
            d = str(random.randint(0, 9))
            while d == digits[-1]:
                d = str(random.randint(0, 9))
            digits.append(d)
        return ''.join(digits)

    def get_certainDetails(self):
        return self.name, self.balance
    
    def get_accountDetails(self):
        print(f"The Account Number : {self.account_number}")
        print(f"The Name of Account Holder is : {self.name}")
        print(f"The Balance is : {self.balance}")


class Account:
    def __init__(self, create_account_obj):
        self.account = create_account_obj

    def deposit(self, amount):
        self.account.balance += amount
        return self.account.balance

    def withdrawal(self, amount):
        if self.account.balance <= 0:
            print("Insufficient Funds!")
        else:
            self.account.balance = self.account.balance - amount
            print(f"Withdrawal Successfully")

    def check_balance(self):
        print(f"The Balance of Your Account is : {self.account.balance}")