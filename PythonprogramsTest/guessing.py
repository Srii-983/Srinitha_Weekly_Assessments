import random
def main():
    m=random.randint(1,100)
    while True:
        n=int(input("Guess the number:"))
        if n>m:
            print("Too High")
        elif n<m:
            print("Too Low")
        else:
            print("You guess is right")    
main()