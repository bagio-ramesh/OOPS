from datetime import datetime

class Bank:
    
    def create_account(self,acc_num,acc_name,acc_type,acc_balance):
        self.acc_num= acc_num
        self.acc_name= acc_name
        self.acc_type= acc_type
        self.acc_balance= acc_balance

    def deposit(self,amount):
        self.acc_balance+=amount
        print(f"Your account number {self.acc_num} is credited with amount {amount} balance is {self.acc_balance} {datetime.now()}")

    def withdraw(self,amount):
        if amount > self.acc_balance:
            raise Exception("Insufficient Fund Broo")
        
        
        else:
            self.acc_balance-=amount
            print(f"Your account number {self.acc_num} is debited with amount {amount} balance is {self.acc_balance} {datetime.now()}")

    def get_balance(self):
        print(f"Your current balance is {self.acc_balance} on {datetime.now()}")


bank_instance1 = Bank()

bank_instance1.create_account(837483874,"Bagio","Current",30000)

bank_instance1.deposit(15000)

bank_instance1.withdraw(2500)

bank_instance1.get_balance()



    
