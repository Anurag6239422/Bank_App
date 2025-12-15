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
                # account_number may be a numeric string; keep as string to preserve digits
                if not account_number_s.isdigit():
                    print(f"Skipping line {lineno} with non-numeric account number: {line}")
                    continue
                try:
                    balance = int(balance_s)
                except ValueError:
                    print(f"Skipping line {lineno} with non-numeric balance: {line}")
                    continue
                acc = Create_Account(name, balance, account_number=account_number_s)
                accounts.append(acc)
    except FileNotFoundError:
        print("Unable to read data from database.txt")
    return accounts