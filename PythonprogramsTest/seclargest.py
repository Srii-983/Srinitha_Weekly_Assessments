def main():
    a=list(map(int,input("enter list of numbers:").split()))
    n=len(a)
    sorted(a)
    print(a[n-2])
main()