class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит: +${amount:.2f}. Новий баланс: ${self.balance:.2f}")
        else:
            print("Сума депозиту має бути позитивною.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Помилка: Недостатньо коштів. Ваш баланс: ${self.balance:.2f}")
        elif amount <= 0:
            print("Сума зняття має бути позитивною.")
        else:
            self.balance -= amount
            print(f"Зняття: -${amount:.2f}. Новий баланс: ${self.balance:.2f}")


account = BankAccount( 1000.0)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  