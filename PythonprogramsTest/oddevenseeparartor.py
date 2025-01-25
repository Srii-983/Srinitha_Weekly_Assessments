def even(arr):
    return [num for num in arr if num%2==0]
def odd(arr):
    return [num for num in arr if num%2!=0]
def main():
    arr=list(map(int,input("Enter multiple values:").split()))
    ev=even(arr)
    print("even numbers are:",ev)
    od=odd(arr)
    print("odd numbers are:",od)
main()