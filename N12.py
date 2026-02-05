class BankAccount:
    def __init__(self, owner, account_number, balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        print("Ім'я власника:", self.owner, "\nРахунок:",self.account_number)


class Bank:
    def deposit(self, account, amount):
        if amount > 0:
            account.balance += amount
            print(f"Депозит: +${amount:.2f}. Новий баланс: ${account.balance:.2f}")
        else:
            print("Сума депозиту має бути позитивною.")

    def withdraw(self, account, amount):
        if amount > account.balance:
            print(f"Помилка: Недостатньо коштів. Ваш баланс: ${account.balance:.2f}")
        elif amount <= 0:
            print("Сума зняття має бути позитивною.")
        else:
            account.balance -= amount
            print(f"Зняття: -${amount:.2f}. Новий баланс: ${account.balance:.2f}")


account = BankAccount("Ivan", "12345", 1000.0)
bank = Bank()

bank.deposit(account, 500)
bank.withdraw(account, 200)
bank.withdraw(account, 1500)
