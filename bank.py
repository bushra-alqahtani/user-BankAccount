class BankAccount:
        def __init__(self,int_rate,balance):
                self.int_rate=float(int_rate)
                self.balance=balance
                self.account_balance = 0
                    
        def deposit(self, amount):
                self.account_balance +=amount
                return self

        def withdraw(self, amount):
                if self.balance > amount:
                    self.account_balance -=amount 
                else:
                    print("Insufficient funds: Charging a $5 fee")  
                return self
            
        def display_account_info(self):
            print(f"Balance is: {self.balance}")
            return self
            
        def yield_interest(self):
                if self.int_rate>0:
                     self.balance=(self.balance*self.int_rate)
                return self

first_account=BankAccount(0.4,20000)
second_accoount=BankAccount(0.3,3000)

first_account.deposit(500).deposit(1000).deposit(90).withdraw(900).yield_interest().display_account_info()
second_accoount.deposit(2000).deposit(100).withdraw(100).withdraw(900).withdraw(800).withdraw(500).yield_interest().display_account_info()


     
