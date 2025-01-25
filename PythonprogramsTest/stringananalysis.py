def stringanalysing(s):
    vowels="aeiou"
    consonats="bcdfghjklmnpqrstvwxyz"
    digits="0123456789"
    vc=0
    cc=0
    dc=0
    sc=0
    s.lower()
    for i in s:
        if i in vowels:
            vc+=1
        elif i in consonats:
            cc+=1
        elif i in digits:
            dc+=1
        else:
            sc+=1
    revers=s[::-1]
    return (vc,cc,dc,sc,revers)
def main():
    stri=input("Enter a string:")
    a,b,c,d,e=stringanalysing(stri)
    print("Vowels:",a)
    print("Consonants:",b)
    print("Digits:",c)
    print("Special Characters:",d)
    print("Reverse of a string:",e)
main()
    
    
            
    