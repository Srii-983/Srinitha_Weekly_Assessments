class BankAccount:
    def deposit(self,bal):
        self.bal=bal
        self.a=int(input("Enter amount to deposit:"))
        self.bal+=self.a
        print("The money in account is",self.bal)
    def withdraw(self):
        self.wd=int(input("enter withdraw amount:"))
        if self.wd>self.bal:
            print("Insufficient balance or overdraft")
        else:
            self.bal-=self.wd
            print("Amount after withdrawing is",self.bal)
bal=0
o1=BankAccount()
o1.deposit(bal)
o1.withdraw()