def pd_strength():
    pd=input("Enter passwrod: ")
    if len(pd)<8:
        print("Weak password")
    else:
        up=any(ch.isupper() for ch in pd)
        lw=any(ch.islower() for ch in pd)
        dt=any(ch.isdigit() for ch in pd)
        sl=any(not ch.isalnum() for ch in pd)
    if up and lw and dt and sl:
        print("Strong Password")
    else:
        print("Weak password")
pd_strength()
