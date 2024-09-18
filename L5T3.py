class Account:
    def __init__(self):
        self.__account_no = None
        self.__account_bal = None
        self.__security_code = None
    def initialize_account(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code
    def print_account_data(self):
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: ${self.__account_bal}")
        print(f"Security Code: {self.__security_code}")

my_account = Account()
my_account.initialize_account("24680", 10000.0, "ABC_123")
my_account.print_account_data()
