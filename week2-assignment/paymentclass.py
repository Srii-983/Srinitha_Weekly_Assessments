class Payment:
    def process_payment(self):
        print("Payment via different ways")
class CreditcardPayment(Payment):
    def __init__(self,credit):
        self.credit=credit
    def process_payment(self):
        print(f"{self.credit} Payment is done using credit card")
class PayPalPayment(Payment):
    def  __init__(self,upi):
        self.upi=upi    
    def process_payment(self):
        print(f"{self.upi} Payment is done uisng PayPal")
class BitcoinPayment(Payment):
    def __init__(self,bitcoin):
        self.bitcoin=bitcoin
    def process_payment(self):
        print(f"{self.bitcoin} Payment  is done using Bitcoin")
a=CreditcardPayment(3000)
a.process_payment()
b=BitcoinPayment(400000)
b.process_payment()
c=PayPalPayment(45890)
c.process_payment()



        