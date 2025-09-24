from person import Person 

class Gardener(Person):
    def __init__(self, FirstName, LastName, GardenName):
        super().__init__(FirsName, LastName)
        self.GardenName = GardenName
        
    def info (self):
        return f'Gardener: {self.FirstName} {self.LastName}, Garden: {self.GardenName}'
    
    
    def GrowingFl(self):
        print(f'{self.FirstName} {self.LastName} have {self.GardenName}. {self.FirstName} works there all day')   
        
    
    def SleepStnding(self):
        print(f'{self.FirstName} {self.LastName} can sleep while standing in {GardenName}.')   
    