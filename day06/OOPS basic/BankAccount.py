class BankAccount :
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = float(balance)

    def deposite(self, amount):
        if amount <=0 :
            print("Deposite amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited: Rs. {amount: .2f}. New Balance: Rs. {self.balance: .2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(
                f"Declined: Insufficient balance. Available: Rs. {self.balance:.2f}"
            )
            return
        self.balance -= amount
        print(
            f"Withdrawn: Rs. {amount:.2f}. Remaining Balance: Rs. {self.balance:.2f}"
        )


account = BankAccount("Vikram", 1000)
account.deposite(500)
account.withdraw(1200)
account.withdraw(400)