def prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
def gen_primes(a,b):
    return [num for num in range(a,b+1) if prime(num)]
def main():
    a=int(input("Enter lower range:"))
    b=int(input("Enter upper range:"))
    res=gen_primes(a,b)
    print(f"Primes between {a} and {b} are:",res,end=" ")
main()