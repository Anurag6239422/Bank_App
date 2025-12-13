from account import Create_Account

def save_account(create_account_obj,
                 file_name=r"C:\Users\anura_9posmze\OneDrive\Desktop\bank_app\Bank_App\database.txt"):
    with open(file_name, 'a') as file:
        line = f"{create_account_obj.account_number},{create_account_obj.name},{create_account_obj.balance}\n"
        file.write(line)

def load_accounts(file_name=r"C:\Users\anura_9posmze\OneDrive\Desktop\bank_app\Bank_App\database.txt"):
    acc = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # skip empty lines

                parts = line.split(",")

                if len(parts) != 3:
                    print("Skipping bad line:", line)
                    continue

                acc_no, name, balance = parts
                try:
                    acc.append(Create_Account(int(acc_no), name, int(balance)))
                except ValueError:
                    print("Skipping line with invalid numbers:", line)

    except FileNotFoundError:
        print("No account found. File does not exist")

    return acc
