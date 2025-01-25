def pattern(n):
    for i in range(1,n+1):
        print("*"*i)
def revpattern(n):
    for i in range(n,0,-1):
        print("*"*i)
def main():
    n=int(input("Enter no of rows:"))
    pattern(n)
    revpattern(n)
main()