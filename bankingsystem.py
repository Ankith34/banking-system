# Problem statement
# Design a bank account management system using Python OOPs.

# You must create a parent class called BankAccount and two child classes called SavingsAccount and CurrentAccount.

# Your program must satisfy the following requirements.

# 1. Parent class: BankAccount
# - Store the account holder's name as a public attribute.
# - Store the account number as a protected attribute.
# - Store the balance as a private attribute.
# - Initialize these attributes using __init__().
# - Implement a deposit(amount) method that accepts only positive amounts.
# - Implement a get_balance() method to return the current balance.
# - Implement an abstract method called calculate_interest().
# 2. Child class: SavingsAccount
# - Inherit from BankAccount.
# - Use super() to initialize the parent attributes.
# - Add a savings interest rate of 5%.
# - Implement calculate_interest() to calculate 5% of the current balance.
# - Add a withdraw(amount) method that doesn't allow withdrawing more than the balance.
# 3. Child class: CurrentAccount
# - Inherit from BankAccount.
# - Use super() to initialize the parent attributes.
# - Implement calculate_interest() to return zero.
# - Allow withdrawals up to a specified overdraft limit.


from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self._account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("New balance:", self.__balance)
        else:
            print("Deposit amount must be positive")

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount):
        self.__balance += amount

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance, interest_rate=5):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.get_balance() * self.interest_rate / 100

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self.get_balance():
            self._update_balance(-amount)
            print("Withdrawn amount:", amount)
            print("New balance:", self.get_balance())
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance, overdraft_limit):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):
        return 0

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount <= self.get_balance() + self.overdraft_limit:
            self._update_balance(-amount)
            print("Withdrawn amount:", amount)
            print("New balance:", self.get_balance())
        else:
            print("Exceeded overdraft limit")


savings = SavingsAccount("Ankith", 101, 10000)
current = CurrentAccount("Rahul", 102, 5000, 2000)

print("Savings interest:", savings.calculate_interest())
print("Current interest:", current.calculate_interest())

savings.withdraw(2000)
current.withdraw(6000)
