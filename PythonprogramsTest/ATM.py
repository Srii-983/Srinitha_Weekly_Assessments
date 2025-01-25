def deposit(bal):
    dp=int(input("enter amount to deposit:"))
    bal=bal+dp
    print("after deposit amount is:",bal)
    return bal
def checkbalance(bal):
    if bal==0:
        print("your account has zero balance so please deposit")
    print("The balance in account is:",bal)
def withdraw(bal):
    drawamt=int(input("Enter money to withdraw:"))
    bal=bal-drawamt
    print("after withdraw amount is:",bal)
    return bal
def main():
    bal=0.0
    while(True):
        print("1.deposit")
        print("2.Check balance")
        print("3.Withdraw")    
        ch=int(input("Enter choice:"))
        if ch==1:
            bal=deposit(bal)
        if ch==2:
            checkbalance(bal)
        if ch==3:
            bal=withdraw(bal)
main()