import os
from account import Create_Account

def save_account(create_account_obj,
                 file_name=r"C:\Users\anura_9posmze\OneDrive\Desktop\bank_app\Bank_App\database.txt"):
    line = f"{create_account_obj.account_number},{create_account_obj.name},{create_account_obj.balance},{create_account_obj.account_type}\n"
    # ensure file ends with a newline so appended records always start on a new line
    prepend_newline = ''
    if os.path.exists(file_name):
        try:
            with open(file_name, 'rb') as f:
                f.seek(0, os.SEEK_END)
                if f.tell() > 0:
                    f.seek(-1, os.SEEK_END)
                    last = f.read(1)
                    if last != b"\n":
                        prepend_newline = "\n"
        except OSError:
            prepend_newline = ''

    with open(file_name, 'a', encoding='utf-8') as file:
        if prepend_newline:
            file.write(prepend_newline)
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
                if len(parts) != 4:
                    print(f"Skipping malformed line {lineno}: {line}")
                    continue
                account_number_s, name, balance_s, account_type = parts
                # validate balance is numeric; keep account number as string (may be large)
                if not balance_s.lstrip('-').isdigit():
                    print(f"Skipping line {lineno} with non-numeric balance: {line}")
                    continue
                balance = int(balance_s)
                # Create_Account signature is (name, balance, account_number)
                acc = Create_Account(name, balance, account_type, account_number=account_number_s)
                accounts.append(acc)
    except FileNotFoundError:
        print("Unable to read data from database.txt")
    return accounts

def update_balance(account_number, new_balance):
    path = r"C:\Users\anura_9posmze\OneDrive\Desktop\bank_app\Bank_App\database.txt"
    with open(path, "r") as file:
        lines = file.readlines()

    with open(path, "w") as file:
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) != 4:
                file.write(line)
                continue
            acc_no, name, balance, account_type = parts
            if acc_no == account_number:
                file.write(f"{acc_no},{name},{new_balance},{account_type}\n")
            else:
                file.write(line)

    