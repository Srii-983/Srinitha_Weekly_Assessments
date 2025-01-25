def multitable(n,s):
    for i in range(1,s+1):
        m=n*i
        print(n,"*" ,i,"=",m)
def main():
    n=int(input("enter number:"))
    s=int(input("enter range of table:"))
    multitable(n,s)
main()