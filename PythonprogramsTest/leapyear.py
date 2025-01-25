def main():
    n=int(input("Enter number of years to check:"))
    for i in range(n):
        yr=int(input("enter year:"))
        if ((yr%4 and yr%100!=0) or yr%400==0):
            print(f"{yr} is not a leap year")
        else:
            print(f"{yr} is leap year")
main()
        
    