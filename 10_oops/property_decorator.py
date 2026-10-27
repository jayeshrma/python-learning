class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # Getter
    @property
    def balance(self):
        return self._balance

    # Setter
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            raise ValueError("Balance cannot be negative")


account = BankAccount(1000)

# Getter
print(account.balance)      # 1000

# Setter
account.balance = 1500
print(account.balance)      # 1500

# Invalid value
account.balance = -500      # ValueError