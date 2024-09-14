class Account:
   
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no       
        self.__account_bal = account_bal      
        self.__security_code = security_code  

  
    def display_account_info(self):
        print(f"Account No: {self.__account_no}")
        print(f"Account Balance: {self.__account_bal}")
        print(f"Security Code: {self.__security_code}")



account = Account(1236, 7000.0, 'XYZ1110')
account.display_account_info()
