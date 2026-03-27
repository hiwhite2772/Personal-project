class Account:
    def __init__(self, id_account, full_name, balance):
        self.__id_account = id_account
        self.full_name = full_name
        self.__balance = balance
    def check_balance(self):
        return self.__balance
    def get_info(self):
        print("\n\t==========Thông tin tài khoản==========\n")
        print(f"Mã tài khoản: {self.__id_account}")
        print(f"Họ và tên: {self.full_name}")
        print(f"Số tiền dư: {self.__balance}")
my_account = Account("123456789", "Hi White", 1000000000)
print(my_account.get_info())

my_account.full_name = "Hi Lusic"
print(my_account.get_info())

print(my_account.check_balance())
