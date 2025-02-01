class Product:
    def __init__(self):
        self.name=input("Enter item name:")
        self.price=int(input("Enter price of item:"))
        self.stock=int(input("Enter the stock of item:"))
        self.quantity=int(input("Enter quantity required:"))
    def check_availability(self):
        if self.stock>=self.quantity:
            print(f"The {self.name} quantity of {self.quantity} is available")
        else:
            print(f"The {self.name} is not available, the stock of {self.name} is {self.stock}")
o=Product()
o.check_availability()
        
        