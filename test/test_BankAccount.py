import pytest
from mutation_src.BankAccount import BankAccount


# TC-BA-01: Проверка корректной инициализации баланса и имени владельца
def test_initial_balance():
    acc = BankAccount("Alice", 1000.0)
    assert acc.get_balance() == 1000.0
    assert acc.owner == "Alice"


# TC-BA-02: Проверка пополнения счета
def test_deposit():
    acc = BankAccount("Bob", 0.0)
    acc.deposit(500.0)
    assert acc.get_balance() == 500.0


# TC-BA-03: Проверка валидации отрицательной суммы пополнения
def test_deposit_negative():
    acc = BankAccount("Bob", 100.0)
    with pytest.raises(ValueError, match="Сумма пополнения должна быть положительной"):
        acc.deposit(-50.0)


# TC-BA-04: Проверка успешного снятия средств
def test_withdraw():
    acc = BankAccount("Charlie", 1000.0)
    acc.withdraw(300.0)
    assert acc.get_balance() == 700.0


# TC-BA-05: Проверка валидации отрицательной суммы снятия
def test_withdraw_negative():
    acc = BankAccount("Charlie", 1000.0)
    with pytest.raises(ValueError, match="Сумма снятия должна быть положительной"):
        acc.withdraw(-50.0)


# TC-BA-06: Проверка снятия суммы при нехватке средств
def test_withdraw_insufficient_funds():
    acc = BankAccount("Charlie", 100.0)
    with pytest.raises(ValueError, match="Недостаточно средств"):
        acc.withdraw(500.0)


# TC-BA-07: Проверка межбанковского перевода (НАЙДЕТ БАГ УЧАСТНИКА 3)
def test_transfer():
    acc_sender = BankAccount("Alice", 1000.0)
    acc_receiver = BankAccount("Bob", 0.0)

    acc_sender.transfer(400.0, acc_receiver)

    assert acc_receiver.get_balance() == 400.0
    assert acc_sender.get_balance() == 600.0  # Упадет, так как списания не произошло