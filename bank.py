from datetime import date, datetime

def log_transaction(acc_no, transaction_type, amount):
    today = datetime.today()

    with open(r"C:\Users\anura_9posmze\OneDrive\Desktop\bank_app\Bank_App\transaction.txt", "a") as file:
        file.write(f"{acc_no},{transaction_type},{amount},{today}\n")