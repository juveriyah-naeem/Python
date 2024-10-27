class BalanceExeption(Exception):
    pass
class BankAccount:
    def __init__(self,initialAmount,accountName):
        self.balance=initialAmount
        self.name=accountName
        print(f"\nAccount '{self.name}' created.\n")
       
    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance =${self.balance:.2f}")
    def deposit(self,amount):
        self.balance +=amount
        print("\nDeposit Complete.")
        self.getBalance()
    def viableTransaction(self,amount):
        if self.balance >=amount:
            return
        else:
            raise BalanceExeption(
                f"\nSorry.Insufficient Balance.Your request can't be proceed."
            )
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance-=amount
            print("\n Withdraw complete.")
            self.getBalance()
        except BalanceExeption as error:
            print(f"Withdraw interrupted:{error}")

    def transfer(self,amount,account):
        try:
            print("\n\t\t\t\t*********** \n\nProcessing Transfer....")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete!\n\n\t\t\t\t************")
        except BalanceExeption as error:
            print(f"\nTransfer interuppted.! {error}")

class IntrestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance+=(amount*1.05)
        print("Deposit Complete")
        self.getBalance()
    
user1=BankAccount(100,'Javeria Naeem')
user2=BankAccount(500,'John Doe')
user3=BankAccount(1000,'Angela Yu')
user3.transfer(200,user2)
user4=IntrestRewardAccount(1000,"Jim")
user4.deposit(100)
user4.transfer(200,user1)