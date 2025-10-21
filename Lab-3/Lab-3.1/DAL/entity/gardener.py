from DAL.entity.person import Person

class Gardener(Person):
    def __init__(self, first_name, last_name, gender, garden_name):
        super().__init__(last_name, first_name, gender)
        self.garden_name = garden_name
        
    def info(self):
        return f'Gardener: {self.first_name} {self.last_name}, Garden: {self.garden_name}'
    
    def growing_fl(self):
        print(f'{self.first_name} {self.last_name} works in the garden {self.garden_name} all day.')   
    
    def sleep_standing(self):
        print(f'{self.first_name} {self.last_name} can sleep while standing in {self.garden_name}.')   
