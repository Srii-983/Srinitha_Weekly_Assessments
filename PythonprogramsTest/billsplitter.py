def main():
    bill=int(input("Enter bill:"))
    nop=int(input("Enter no of people:"))
    bp=int(input("Enter tip percentage"))
    tip=(bill*bp)/100
    bill=bill+tip
    amt=bill/nop
    print("splitting amount for each person:",amt)
main()