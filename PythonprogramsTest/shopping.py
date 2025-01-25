def additem(arr):
    itemname=input("Enter item name:")
    price=int(input("enter price:"))
    if price<=0:
        print("Price must be gretaer than zero")
    else:
        arr.append((itemname,price))
        print(f"{itemname} : {price}")
    return arr
def viewitems(arr):
    if not arr:
        print("cart is empty")
    else:
        print(arr)
def cal_price(arr):
    total=sum(price for _, price in arr)
    print("total price is:",total)
def main():
    arr=[]
    print("1.add items")
    print("2.view items")
    print("3.calculate price")
    while True:
        ch=int(input("enter choice:"))
        if ch==1:
            arr=additem(arr)
        if ch==2:
            viewitems(arr)
        if ch==3:
            arr=cal_price(arr)
main()
                
            
            

    
    