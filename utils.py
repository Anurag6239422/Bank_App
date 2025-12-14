from account import Create_Account

def save_account(create_account_obj,
                 file_name=r"C:\Users\anura_9posmze\OneDrive\Desktop\bank_app\Bank_App\database.txt"):
    with open(file_name, 'a') as file:
        line = f"{create_account_obj.account_number},{create_account_obj.name},{create_account_obj.balance}\n"
        file.write(line)

def load_accounts(file_name=r"C:\Users\anura_9posmze\OneDrive\Desktop\bank_app\Bank_App\database.txt"):
    try:
        with open(file_name, "r") as file:
            accounts = []
            for line in file:
                line = line.strip()
                if line:
                    account_number, name, balance = line.split(',')
                    acc = Create_Account(int(account_number), name, int(balance))
                    accounts.append(acc)
            return accounts
    except FileNotFoundError:
        print("Unable to read data from database.txt")
        return []