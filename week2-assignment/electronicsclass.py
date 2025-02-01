class Electronics:
    def __init__(self,brand):
        self.brand=brand
    def show(self):
        return f"Brand : {self.brand}"
class MobileDevice(Electronics):
    def __init__(self,brand,screensize):
        super().__init__(brand)
        self.screensize = screensize
    def show(self):
        details=super().show()
        return f"{details}\nscreen size:{self.screensize} "
class SmartPhone(MobileDevice):
    def __init__(self,brand,screensize,camerapixel):
        super().__init__(brand,screensize)
        self.camerapixel = camerapixel
    def show(self):
        details=super().show()
        print(f"{details}\ncamera pixels:{self.camerapixel} ")
o=SmartPhone("Realme","5 inches","64 megapixels")
o.show()

        