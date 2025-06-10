
from datetime import datetime

class Expenses:


    def __init__(self,user):

        self.user = user

        self.transactions = []

    def add_expense(self,**kwargs):

        self.transactions.append(kwargs)

        print("Transactions added....---")

    def delete_expense(self,id):

        for t in self.transactions:

            if (t.get("id")== id):

                self.transactions.remove(t)
                print("Transaction has been removed....---")


expenses_instance1 = Expenses("Sandra")

expenses_instance1.add_expense(Id = 1,title = "Car Oil",amount = 800 , category = "Oil", date = 2025-05-15 )
expenses_instance1.add_expense(Id = 2,title = "Car Tyre",amount = 4799 , category = "Tyre", date = "2025-05-15")
expenses_instance1.add_expense(Id = 3,title = "Car Fuel",amount = 7500 , category = "Fuel", date = "2025-05-15")
expenses_instance1.add_expense(Id = 4,title = "Car Nitro Gas",amount = 12500 , category = "Gas", date = "2025-05-15")
expenses_instance1.add_expense(Id = 5,title = "Car Spoiler",amount = 250000 , category = "spoiler", date = "2025-05-15")
print(expenses_instance1.transactions)

expenses_instance1.delete_expense(1)



