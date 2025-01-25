def cel_fah(t):
    return (t*(9/5))+32
def cel_kel(t):
    return t+273.15
def fah_cel(t):
    return (t-32)*5/9
def fah_kel(t):
    return fah_cel(t)+273.15
def kel_cel(t):
    return t-273.15
def kel_fah(t):
    return cel_fah(kel_cel(t))
def main():
    print("1.celsius to fahrenheit")
    print("2.celsius to kelvin")
    print("3.fahrenheit to celsius")
    print("4.fahrenheit to kelvin")
    print("5.kelvin to celsius")
    print("6.kelvin to fahrenheit")
    t=int(input("enter temperature"))
    while True:
        ch=int(input("enter choice to convert different temp"))
        if ch==1:
            s=cel_fah(t)
            print(f"{s}F is for {t}celsius")
        if ch==2:
            s=cel_kel(t)
            print(f"{s}K is for {t}celsius")
        if ch==3:
            s=fah_cel(t)
            print(f"{s}C is for {t}F")
        if ch==4:
            s=fah_kel(t)
            print(f"{s}K is for {t}F")
        if ch==5:
            s=kel_cel(t)
            print(f"{s}C is for {t}K")
        if ch==6:
            s=kel_fah(t)
            print(f"{s}F is for {t}K")
main()
        
            
        