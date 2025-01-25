def factorial(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    print(f"factorial of {n} is", a)
def main():
    n=int(input("Enter number:"))
    if n<=0:
        print("Enter valid number")
    else:
        factorial(n)
main()