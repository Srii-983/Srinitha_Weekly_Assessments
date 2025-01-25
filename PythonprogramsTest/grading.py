def display(mar,name):
    if mar>=85:
        print(f"{name} got A garde")
    elif mar<85 and mar>=70:
        print(f"{name} got B garde")
    elif mar<70 and mar>=60:
        print(f"{name} got C garde")
    elif mar<60 and mar>=50:
        print(f"{name} got D garde")
    else:
        print(f"{name} failed")
def cal_marks(a,b,c,d,e):
    s=a+b+c+d+e
    return s
def percentage(s):
    mar=(s/500)*100
    return mar
def main():
    name=input("enter student name: ")
    a=int(input("Enter subject1 marks:"))
    b=int(input("Enter subject2 marks:"))
    c=int(input("Enter subject3 marks:"))
    d=int(input("Enter subject4 marks:"))
    e=int(input("Enter subject5 marks:"))
    s=cal_marks(a,b,c,d,e)
    p=percentage(s)
    display(p,name)
main()
    
    