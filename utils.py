from account import Create_Account

def save_account(create_account_obj,
                 file_name=r"C:\Users\anura_9posmze\OneDrive\Desktop\bank_app\Bank_App\database.txt"):
    with open(file_name, 'a') as file:
        line = f"{create_account_obj.account_number},{create_account_obj.name},{create_account_obj.balance}\n"
        file.write(line)

def load_accounts(file_name=r"C:\Users\anura_9posmze\OneDrive\Desktop\bank_app\Bank_App\database.txt"):
    accounts = []
    try:
        with open(file_name, "r") as file:
            for lineno, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    print(f"Skipping malformed line {lineno}: {line}")
                    continue
                account_number_s, name, balance_s = parts
                try:
                    account_number = int(account_number_s)
                    balance = int(balance_s)
                except ValueError:
                    print(f"Skipping line {lineno} with non-numeric fields: {line}")
                    continue
                acc = Create_Account(account_number, name, balance)
                accounts.append(acc)
    except FileNotFoundError:
        print("Unable to read data from database.txt")
    return accounts