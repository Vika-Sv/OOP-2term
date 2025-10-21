from DAL.entity.person import Person

class Seller(Person):
    def __init__(self, first_name, last_name, gender, shop_name):
        super().__init__(last_name, first_name, gender)
        self.shop_name = shop_name
        
    def info(self):
        return f'Seller: {self.first_name} {self.last_name}, Shop: {self.shop_name}'
    
    def selling_item(self):
        print(f'{self.first_name} {self.last_name} sells items in {self.shop_name}.')   
    
    def sleep_standing(self):
        print(f'{self.first_name} {self.last_name} can sleep while standing in {self.shop_name}.')   
