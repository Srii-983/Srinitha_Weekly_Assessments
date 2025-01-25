def main():
    wt=float(input("Enter weight:"))
    ht=float(input("Enter height:"))
    bmi=(wt/ht**2)
    if bmi>=40:
        print("Obese")
    elif bmi<39.9 and bmi>25:
        print("Overweight")
    elif bmi<24.9 and bmi>18:
        print("Normal")
    else:
        print("Underweight")
main()