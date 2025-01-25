def main():
    sal=int(input("Enter salary:"))
    age=int(input("enter age:"))
    cs=int(input("enter credit score:"))
    if age>18 and age<60:
        if sal>=15000:
            if cs>=700:
                print("Eligible to loan")
            else:
                print("Not eligible as credit score is less than 700")
        else:
            print("minimum salary should be 15000 to get loan")
    else:
        print("minimum and maximum age to get loan is 18 and 60 respectively")
main()