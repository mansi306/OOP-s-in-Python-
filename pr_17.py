class Cart:
    def __init__(self,basket1,basket2,basket3):# constructor
        self.clothes=basket1
        self.grocery=basket2
        self.electronics=basket3
    def __len__(self): # magic method
        print("Total number of items in cart :")
        return len(self.clothes)+len(self.electronics)+len(self.grocery)
Mansi = Cart(["crop_top","Hoodie","jeans","jumpsuit"],["sugar","moongdal","oil","oats"],["headphone","Alexa","smartwatch"])
print(len(Mansi))