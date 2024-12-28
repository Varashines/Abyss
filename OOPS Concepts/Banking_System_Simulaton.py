from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account creation has been successful. Your account number is ", self.accountNumber)

    def authenticate(self,name,accountNo):
        if accountNo in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNo][0] == name:
                print("Authentication Successful")
                self.accountNo = accountNo
                return True
            else:
                print("Authentication Failed")
                return False

        else:
            print("Authentication Failed")
            return False

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingsAccounts[self.accountNo][1]:
            print("Insuffecient balance")
        else:
            self.savingsAccounts[self.accountNo][1] -= withdrawAmount
            print("Withdrawal was succesful, Available balance: ",self.savingsAccounts[self.accountNo][1])

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNo][1] += depositAmount
        print("Deposit was succesful, Available balance: ",self.savingsAccounts[self.accountNo][1])
        self.displayBalance()

    def displayBalance(self):
        print("Available Balance: ",self.savingsAccounts[self.accountNo][1])

savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to Create a Savings Account")
    print("Enter 2 to Access an Existing Account")
    print("Enter 3 to exit")
    userchoice = int(input())
    if userchoice == 1:
        print("Please enter your Name")
        name = input()
        print("Please enter your initial Deposit")
        initialdeposit = input()
        savingsAccount.createAccount(name, initialdeposit)
    elif userchoice == 2:
        print("Please enter your Name")
        name = input()
        print("Please enter your Account No.")
        accountNo = int(input())
        auth = savingsAccount.authenticate(name,accountNo)
        if auth == True:
            print("Enter 1 to check your Savings account Balance")
            print("Enter 2 for withdrawal")
            print("Enter 3 for Deposit")
            print("Enter 4 to go back to the previous menu")
            userChoice = int(input())
            if userChoice == 1:
                savingsAccount.displayBalance()
            elif userChoice == 2:
                print("Please enter withdrawal Amount")
                withdrawamount = input()
                savingsAccount.withdraw(withdrawamount)
            elif userChoice == 3:
                print("Please enter deposit Amount")
                depositamount = input()
                savingsAccount.deposit(depositamount)
            elif useChoice == 4:
                break

    elif userchoice == 3:
        quit()
