import random

import json

import os

#Bank Account System

#Create Account, SavingsAccount, CheckingAccount classes.

#Add deposit, withdraw, transfer, and balance tracking.

#Try adding overdraft rules and interest calculations.


class Account():

    
    def __init__(self, accountNumber, password, balance = 1000):
        self.accountNumber = accountNumber
        self.balance = balance
        self.password = password
        self.jsonUpload()

    @classmethod
    def account_number(cls):
        number = int(random.randrange(100000, 999999))

        return number
    
    @classmethod
    def accountPassword(cls):
        password = str(input("Enter Account Password: "))

        return password
    
    @classmethod
    def getAccount(cls):
        with open('pyMinProjs\Bank_Account_System\json.json') as file:
            # Load the contents of the file into a Python list
            data = json.load(file)

        passWord = input('Enter Account Password: ')

        for x in data:
            if x['accountPassword'] == passWord:
                return x
    

    def deposit(self):
        print("Deposit Amount:")
        amount = int(input())

        self.balance = self.getBalance()
        self.balance += amount
        print(f"Updated Balance: {self.balance}")

        self.balanceUpdate()

    def withdraw(self):
        print("Withdrawl Amount:")
        withdrawl = int(input())

        self.balance = self.getBalance()

        if self.balance > withdrawl:
            print('Withdrawl amount exceeds balance')
        else:
            self.balance = self.balance - withdrawl
        print(f"Updated Balance: {self.balance}")

        self.balanceUpdate()

    def transfer(self):
        #Transfer between Savings and Checking primarily, then add account to account routing
        while True:
            print("Input Transfer Acount Number:")
            accountNum = int(input())

            account = self.transferAlgo(accountNum)
            if not account:
                print("Account Does Not Exist")
                continue
            
            print("Enter Transfer Amount")

            try:
                amount = int(input(amount))
            except ValueError:
                print("Enter a valid data type")
                continue

            if amount < 0:
                print("Input Invalid")
                continue
            
            if self.balance < amount:
                print("Balance Too Low For Transfer")
                continue
            
            self.balance -= amount
            account.balance += amount

            print(f"Transferred {amount}, Remaing Balance: {self.balance}")

            break
        

    def transferAlgo(self, accountNum):
        """Check if account number exists and return account with that number. Different function for practice"""
        
        for account in Account.accounts:
            if account.accountNumber == accountNum:
                return account
            
        return None
    
    def jsonUpload(self):

        with open('pyMinProjs\Bank_Account_System\json.json') as file:
            # Load the contents of the file into a Python list
            data = json.load(file)

        accounts = {
            "accountNumber": self.accountNumber,
            "accountPassword": self.password,
            "accountBalance": self.balance
        }
        
        for x in data:
            if x['accountNumber'] == self.accountNumber:
                break
        
        else:
            data.append(accounts)

        json_str = json.dumps(data, indent=4)
        #file_size = os.path.getsize('json.json')

        if not os.path.exists('pyMinProjs\Bank_Account_System\json.json'):  # File doesn't exist
            with open('pyMinProjs\Bank_Account_System\json.json', 'w') as foo:
                json.dump(data, foo, indent=4)
        else:
            if os.path.getsize('pyMinProjs\Bank_Account_System\json.json') == 0:  # File exists but empty
                with open('pyMinProjs\Bank_Account_System\json.json', 'w') as foo:
                    json.dump(data, foo, indent=4)
            else:
                with open('pyMinProjs\Bank_Account_System\json.json', 'w') as foo:
                    json.dump(data, foo, indent=4)

        
    def balanceUpdate(self):
        with open('pyMinProjs\Bank_Account_System\json.json') as file:
            # Load the contents of the file into a Python list
            data = json.load(file)
        
        for x in data:
            if x['accountNumber'] == self.accountNumber:
                x['accountBalance'] = self.balance
        
        with open('pyMinProjs\Bank_Account_System\json.json', 'w') as foo:
                    json.dump(data, foo, indent=4)

    def getBalance(self):
        with open('pyMinProjs\Bank_Account_System\json.json') as file:
            # Load the contents of the file into a Python list
            data = json.load(file)
        
        for x in data:
            if x['accountNumber'] == self.accountNumber:
                return x['accountBalance']

        
    


def main():
    print("Welcome to the Bank Account System!")
    
    print("Create Account or Log In:")

    account = int(input("[1] or [2]"))

    if account == 1:
        accountNumber = Account.account_number()
        account_password = Account.accountPassword()

        userAccount = Account(accountNumber, account_password, 1000)

    elif account == 2:
        accountGetter = Account.getAccount()
        userAccount = Account(accountGetter['accountNumber'], accountGetter['accountPassword'], accountGetter['accountBalance'])

    option = int(input("Choose an action [1] Deposit, [2] Withdraw, [3] Transfer, [4] Balance Tracking"))

    if option == 1:
        userAccount.deposit()
    elif option == 2:
        userAccount.withdraw()
    elif option == 3:
        userAccount.transfer()
    elif option == 4:
        pass
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()