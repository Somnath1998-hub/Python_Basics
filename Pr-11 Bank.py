"""
Make your own bank here

Here we make our bank

It will offer several functionalities such as creating account of different type (saving or current), 
Making transaction (withdrawal or deposit) and statement checking.

"""

class Account:
    def __init__(self, name, balance, mobile_no, min_balance):
        self.name = name
        self.balance = balance
        self.mobile_no = mobile_no
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance :
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("\n Account Balance :{} \n".format(self.balance))


class Current(Account):
    def __init__(self, name, mobile_no, balance):
        super().__init__(name, balance, mobile_no, min_balance= -1000)

    def __str__(self):
        return "\n Account_name :{}\n Mobile_no :{}\n Current Balance :{}\n".format(self.name, self.mobile_no, self.balance)

class Savings(Account):
    def __init__(self, name, mobile_no, balance):
        super().__init__(name, balance, mobile_no, min_balance= 0)

    def __str__(self):
        return "\n Account_name :{}\n Mobile_no :{}\n Current Balance :{}\n".format(self.name, self.mobile_no, self.balance)
        
    
