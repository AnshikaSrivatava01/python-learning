class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.__balance = float(initial_balance)  # Private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__balance:
            print("Transaction declined: Insufficient funds.")
            return False
        self.__balance -= amount
        return True


acc = BankAccount("Aditya", 5000)
print(f"Current Balance: Rs. {acc.get_balance():.2f}")
acc.deposit(1500)
acc.withdraw(7000) 
acc.withdraw(2000)
print(f"Final Balance: Rs. {acc.get_balance():.2f}")