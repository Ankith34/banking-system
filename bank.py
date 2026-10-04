class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        if balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0
            print("Initial balance cannot be negative")
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
        else:
            print("deposit amount must be valid")
    def withdraw(self,amount):
        if amount>0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("withdraw amount must be valid and less than or equal to balance")
    def display(self):
        print("Account Holder: ",self.account_holder)
        print("Balance: ",self.__balance)
a1 = BankAccount("John",1000)
a1.display()
a1.deposit(500)
a1.display()
