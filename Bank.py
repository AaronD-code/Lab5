class BankAccount:
    def __init__(self, acc_number, name, balance=0.0):
        self.acc_number = acc_number
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            return False
        if amount > self.balance:
            return False
        self.balance -= amount
        return True


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_number, name, balance=0.0):
        if acc_number in self.accounts:
            return False
        self.accounts[acc_number] = BankAccount(acc_number, name, balance)
        return True

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def transfer(self, from_acc, to_acc, amount):
        a = self.get_account(from_acc)
        b = self.get_account(to_acc)
        if a is None or b is None:
            return False
        if a.withdraw(amount):
            b.deposit(amount)
            return True
        return False


if __name__ == "__main__":
    bank = Bank()
    bank.create_account("1", "Alice", 100)
    bank.create_account("2", "Bob", 50)
    print(bank.transfer("1", "2", 25))
    print(bank.get_account("1").balance, bank.get_account("2").balance)