import random

import json

import os

import random

#Bank Account System

#Create Account, SavingsAccount, CheckingAccount classes.

#Add deposit, withdraw, transfer, and balance tracking.

#Try adding overdraft rules and interest calculations.


class Account():

    
    def __init__(self, accountNumber, password, balance):
        self.accountNumber = accountNumber
        self.balance = balance
        self.password = password

    @classmethod
    def account_number(cls):
        number = int(random.randrange(100000, 999999))

        return number
    
    @classmethod
    def accountPassword(cls):
        password = str(input("Enter Account Password: "))

        return password
    

    def deposit(self):
        if isinstance(self, Checking):
            print("Deposit Amount:")
            amount = int(input())

            self.balance = self.balance
            self.balance += amount
            print(f"Updated Balance: {self.balance}")
        else:
            print('Can Only Deposit to Checking')


    def withdraw(self):
        print("Withdrawl Amount:")
        withdrawl = int(input())

        self.balance = self.balance

        if self.balance > withdrawl:
            print('Withdrawl amount exceeds balance')
        else:
            self.balance = self.balance - withdrawl
        print(f"Updated Balance: {self.balance}")


    def transfer(self, transfer_accounts):

        while True:
            print("Input Account to Transfer To:")

            for i,x in enumerate(transfer_accounts):
                print(f"[{i}] {transfer_accounts[x].name}")

            transfer_account = int(input())
            #idx_map = {key: i for i, key in enumerate(transfer_accounts)}
            foo = list(transfer_accounts.keys())

            '''account = self.transferAlgo(accountNum)
            if not account:
                print("Account Does Not Exist")
                continue'''
            
            print("Enter Transfer Amount")

    
            amount = int(input())
        

            if amount < 0:
                print("Input Invalid")
                continue
            
            if self.balance < amount:
                print("Balance Too Low For Transfer")
                continue
            
            self.balance -= amount
            transfer_accounts[foo[transfer_account]].balance += amount

            print(f"Transferred {amount}, Remaing Balance: {self.balance}")

            break
        
    
        
class Checking(Account):

    name = 'Checking'
    
    def __init__(self, accountNumber, password, balance = 1000, fee = .02, maintenance = 50):
        self.fee = fee
        self.maintenance = maintenance
        super().__init__(accountNumber, password, balance)

    def withdraw(self):

        print("Withdrawl Amount:")
        withdrawl = int(input())

        fee = self.balance * self.fee
        self.balance = self.balance - fee

        if self.balance > withdrawl:
            print('Withdrawl amount exceeds balance')
            self.balance = self.balance / self.fee
        else:
            self.balance = self.balance - withdrawl
        print(f"Updated Balance: {self.balance}")

class Savings(Account):

    name = 'Savings'
    
    def __init__(self, accountNumber, password, balance = 0, interest = .05):
        self.interest = interest
        self.withdrawls = 0
        super().__init__(accountNumber, password, balance)


    def withdraw(self):
        print("Withdrawl Amount:")
        withdrawl = int(input())

        interest = self.balance * self.interest
        self.balance = self.balance + interest

        if self.balance > withdrawl:
            print('Withdrawl amount exceeds balance')
        else:
            self.balance = self.balance - withdrawl
        print(f"Updated Balance: {self.balance}")
    
class Investment(Account):

    name = 'Investment'

    def __init__(self, accountNumber, password, riskFactor, balance = 0):
        self.riskFactor = riskFactor
        super().__init__(accountNumber, password, balance)

    def withdraw(self):
        print("Withdrawl Amount:")
        withdrawl = int(input())

        growth = {
            "low" : random.uniform(.99, 1.05),
            "medium" : random.uniform(.95, 1.10),
            "high" : random.uniform(.89, 1.15)
        }

        self.balance = self.balance * growth[self.riskFactor]

        if self.balance > withdrawl:
            print('Withdrawl amount exceeds balance')
        else:
            self.balance = self.balance - withdrawl
        print(f"Updated Balance: {self.balance}")
    


def create_user_accounts():

    account_number = Account.account_number()
    account_password = Account.accountPassword()


    # Attach sub-accounts (they will update the JSON entry)
    checking = Checking(account_number, account_password)
    savings = Savings(account_number, account_password)
    investment = Investment(account_number, account_password, 'medium')

    accounts = {
        'checking':checking,
        'savings':savings,
        'investment':investment
        }
    

    return accounts

def switch_accounts(account_swap):

        print("Switch Active Account To: ")

        for i, x in enumerate(account_swap):
                print(f"[{i}] {account_swap[x].name}")

        swap = int(input())
        foo = list(account_swap.keys())

        return foo[swap]

def main():
    print("Welcome to the Bank Account System!")
    

    userAccount = create_user_accounts()
    default = 'checking'

    while True:
        option = int(input("Choose an action\n[1] Deposit\n[2] Withdraw\n[3] Transfer\n[4] Switch Accounts\n[5]Quit\n"))

        if option == 1:
            userAccount[default].deposit()
        elif option == 2:
            userAccount[default].withdraw()
        elif option == 3:
            userAccount[default].transfer(userAccount)
        elif option == 4:
            default = switch_accounts(userAccount)
        elif option == 5:
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()