from bank import BankAccount

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account=[BankAccount(int_rate=0.02, balance=0)]

    def make_deposite(self,amount,account_num):
        if account_num < len(self.account):
            self.account[account_num].balance += amount
        elif account_num == len(self.account):
             self.account += [BankAccount(int_rate=0.02, balance=0)]
             self.account[account_num].balance += amount
        else:
             print("wrong account number")
        return self
   
    def make_withdrawal(self, amount,account_num):
        if account_num < len(self.account):
            self.account[account_num].balance -= amount
        else:
            print("wrong account number")
        return self

    def display_user_balance(self,account_num):
        print(f"User: {self.name}, Account Number:{account_num},")
        return self


    def transfer_money(self,account_num, other_user, user_account_num, amount):
        if account_num < len(self.account) and user_account_num < len(other_user.account):
            other_user.account[user_account_num].balance += amount
            self.account[account_num].balance -= amount
        else:
            print("wrong account number")
        return self
    

yahya=User("Yahya","Yahya@gmail.com")
bushra=User("Bushra","bushra@gmail.com")
talal=User("Talal","talal@gmail.com")

yahya.make_deposite(1000,1)
yahya.make_deposite(2000,1)
yahya.make_deposite(4000,2)
yahya.make_withdrawal(1000,1)
yahya.display_user_balance(1)


bushra.make_deposite(2000,2)
bushra.make_deposite(2500,1)
bushra.make_withdrawal(600,0)
bushra.make_withdrawal(150,1)
bushra.display_user_balance(2)


talal.make_deposite(5000,1)
talal.make_withdrawal(200,2)
talal.make_withdrawal(300,1)
talal.make_withdrawal(1000,1)
talal.display_user_balance(1)

yahya.transfer_money(0,talal,1,3000)
talal.display_user_balance(1)
yahya.display_user_balance(1)


