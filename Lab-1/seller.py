from person import Person 

class Seller(Person):
    def __init__ (self, FirstName, LastName, ShopName):
        super().__init__(FirstName, LastName)
        self.ShopName = ShopName
        
    def info(self):
        return f'Seller: {self.FirstName} {self.LastName}, Shop: {ShopName}'
    
    
    def SellingItem(self):
        print(f'{self.FirstName} {LastName} sells item in {ShopName}.')   
        
    
    def SleepStnding(self):
        print(f'{self.FirstName} {LastName} can sleep while standing in {ShopName}.')   
        