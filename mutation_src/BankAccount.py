class BankAccount:
    # MUT-BA-01
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.history = []

    # def __init__(self, owner: str, initial_balance: float = 0.0):
    #     self.owner = owner
    #     # МУТАЦИЯ: добавлена единица к начальному балансу
    #     self.balance = initial_balance + 1.0
    #     self.history = []

    # MUT-BA-02
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount
        self.history.append(f"Пополнение: +{amount}")

    # def deposit(self, amount: float):
    #     # МУТАЦИЯ: знак <= заменен на >=
    #     if amount >= 0:
    #         raise ValueError("Сумма пополнения должна быть положительной")
    #     self.balance += amount
    #     self.history.append(f"Пополнение: +{amount}")

    # MUT-BA-03
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        self.history.append(f"Снятие: -{amount}")

    # def withdraw(self, amount: float):
    #     if amount <= 0:
    #         raise ValueError("Сумма снятия должна быть положительной")
    #     if amount > self.balance:
    #         raise ValueError("Недостаточно средств")
    #     # МУТАЦИЯ: вместо списания происходит зачисление (+= вместо -=)
    #     self.balance += amount
    #     self.history.append(f"Снятие: -{amount}")

    # MUT-BA-04
    def transfer(self, amount: float, target_account: 'BankAccount'):
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount
        target_account.balance += amount
        self.history.append(f"Перевод: {amount} пользователю {target_account.owner}")
        target_account.history.append(f"Получен перевод: {amount} от {self.owner}")

    # def transfer(self, amount: float, target_account: 'BankAccount'):
    #     if amount <= 0:
    #         raise ValueError("Сумма перевода должна быть положительной")
    #     if amount > self.balance:
    #         raise ValueError("Недостаточно средств")
    #
    #     # МУТАЦИЯ: списание средств с текущего аккаунта пропущено
    #     target_account.balance += amount
    #
    #     self.history.append(f"Перевод: {amount} пользователю {target_account.owner}")
    #     target_account.history.append(f"Получен перевод: {amount} от {self.owner}")

    # MUT-BA-05
    # def get_balance(self) -> float:
    #     return self.balance

    def get_balance(self) -> float:
        # МУТАЦИЯ: возвращаемый баланс удваивается
        return self.balance * 2