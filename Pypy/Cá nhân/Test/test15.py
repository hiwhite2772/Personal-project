class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Đã thêm tiền: {amount}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Không đủ tiền. Vui lòng nhập đúng số tiền dư hiện tại!")
        else:
            self.balance -= amount
            print(f"Đã rút tiền: {amount}.")

    def showBalance(self):
        print(f"Tên: {self.name}")
        print(f"Hiện dư: {self.balance}")
        
account1 = BankAccount("White", 100000000)
account1.deposit(6000000)
account1.withdraw(200000)
account1.showBalance()
print()

account2 = BankAccount("Atus", 1500000)
account2.deposit(400000)
account2.withdraw(250000)
account2.showBalance()