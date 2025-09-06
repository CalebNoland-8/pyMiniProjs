

#Bank Account System

#Create Account, SavingsAccount, CheckingAccount classes.

#Add deposit, withdraw, transfer, and balance tracking.

#Try adding overdraft rules and interest calculations.



def main():
    print("Welcome to the Bank Account System!")
    
    balance = 1000.0  # Initial balance
    print(f"Current Balance: {balance}")

    option = input("Choose an action [1] Deposit, [2] Withdraw, [3] Transfer, [4] Balance Tracking")

    if option == 1:
        print("Deposit Amount:")
        amount = input()

        balance += amount
        print(f"Updated Balance: {balance}")
    elif option == 2:
        print("Withdrawl Amount:")
        withdrawl = input()

        balance = balance - withdrawl
        print(f"Updated Balance: {balance}")
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        pass

if __name__ == "__main__":
    main()