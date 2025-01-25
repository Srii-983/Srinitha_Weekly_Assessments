def palindrome(a):
    if str(a)==str(a)[::-1]:
        print(a,"is palindrome")
    else:
        print(a,"is not palindrome")
def main():
    n=int(input("enter number of words to check:"))
    for i in range(n+1):
        a=input("entera number or string:")
        palindrome(a)
main()
    