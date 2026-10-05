class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.history = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount
        self.history.append(f"Пополнение: +{amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        self.history.append(f"Снятие: -{amount}")

    # def transfer(self, amount: float, target_account: 'BankAccount'):
    #     if amount <= 0:
    #         raise ValueError("Сумма перевода должна быть положительной")
    #     if amount > self.balance:
    #         raise ValueError("Недостаточно средств")
    #
    #     # БАГ: Деньги зачисляются целевому аккаунту, но не списываются с текущего (self.balance -= amount пропущено)
    #     target_account.balance += amount
    #
    #     self.history.append(f"Перевод: {amount} пользователю {target_account.owner}")
    #     target_account.history.append(f"Получен перевод: {amount} от {self.owner}")

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")

        # ИСПРАВЛЕНО: Списание средств с текущего аккаунта перед зачислением
        self.balance -= amount
        target_account.balance += amount

        self.history.append(f"Перевод: {amount} пользователю {target_account.owner}")
        target_account.history.append(f"Получен перевод: {amount} от {self.owner}")

    def get_balance(self) -> float:
        return self.balance