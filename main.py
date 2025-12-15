from account import Create_Account
from account import Account
from utils import save_account, load_accounts

if __name__ == "__main__" :
    try :
        flag = True

        while flag :
            print("1 means New User\n2 means Existing User")

            choice = int(input("Enter either 1 and 2 : "))

            if choice == 1 :
                name = input("Enter the Name : ")
                balance = int(input("Enter the Account Opening Balance : "))
                create_account = Create_Account(name, balance)
                save_account(create_account)
                print(f"Account created. Your account number is: {create_account.account_number}")
                create_account.get_accountDetails()

            elif choice == 2 :
                account_number = input("Enter the Account Number : ")
                accounts = load_accounts()
                create_account = None
                for acc in accounts:
                    if acc.account_number == account_number:
                        create_account = acc
                        break
                if create_account is None:
                    print("Account not found!")
                    continue
                print("1 means Withdrawal\n2 means Deposit\n3 means Check Balance\n4 means All Account Details\n5 means Exit")
                value = int(input("Enter Either 1,2,3,4 or 5: "))
                account = Account(create_account)
                if value == 1 :
                    amount_withdrawal = int(input("How much Amount you want to Withdraw : "))
                    account.withdrawal(amount_withdrawal)
                elif value == 2 :
                    amount_deposit = int(input("How much Amount you want to Deposit : "))
                    account.deposit(amount_deposit)
                elif value == 3 :
                    account.check_balance()
                elif value == 4 :
                    acc = load_accounts()
                    for i in acc:
                        i.get_accountDetails()
                        print()
                elif value == 5 :
                    flag = False
                else:
                    raise ValueError("Please Provide correct input either 1,2,3 or 4")
                
            else :
                raise ValueError("Please Provide correct input either 1 or 2")
            
    except Exception as e:
        print(e)

                
            


        
