import datetime

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

class DepositService:
    def execute(account, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        account.balance += amount

class WithdrawalService:
    def execute(account, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > account.balance:
            raise ValueError("Insufficient funds.")
        account.balance -= amount

class Logger:
    @staticmethod
    def log_transaction(account_number, action, amount):
        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{datetime.datetime.now()}: {action} {amount} for account {account_number}\n"
            )

class NotificationService:
    @staticmethod
    def send_notification(message):
        print(f"Sending notification: {message}")

class StatementService:
    @staticmethod
    def generate_statement(account):
        statement = f"Statement for Account: {account.account_number}\nBalance: {account.balance}\n"
        print(statement)
        with open("statements.log", "a") as stmt_file:
            stmt_file.write(
                f"{datetime.datetime.now()}: Generated statement for {account.account_number}\n"
            )
        NotificationService.send_notification(f"Statement generated for account {account.account_number}.")

