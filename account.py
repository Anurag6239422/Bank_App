try :
        class Create_Account:
            def __init__(self, account_number, name, balance):
                self.account_number = account_number
                self.name = name
                self.balance = balance

            def get_accountDetails(self):
                print(f"The Account Number is : {self.account_number}")
                print(f"The Name of Account Holder is : {self.name}")
                print(f"The Opening Account Balance is : {self.balance}")
            
        class Account:
            def __init__(self, create_account_obj):
                self.account = create_account_obj

            def deposit(self, amount) :
                self.account.balance += amount
                print(f"Deposited Successfully")
            
            def withdrawal(self, amount) :
                if self.account.balance <= 0 :
                    print("Insufficient Funds!")
                else :
                    self.account.balance = self.account.balance - amount
                    print(f"Withdrawal Successfully")
            
            def check_balance(self) :
                 print(f"The Balance of Your Account is : {self.account.balance}")


except Exception as e:
     print(e)