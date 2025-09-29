class MyString:
    def __init__(self, text):
        self.value = text
        self.length = len(text)
        
        
    def find_substring(self, sub):
        return self.value.find(sub)   
    
    
    def insert_substring(self, sub, pos):
        if pos >= 0 and pos <= len(self.value):
            self.value = self.value[:pos] + sub + self.value[:pos]
            self.length = len(self.value)
            
            
    def replace_substring(self, old, new):
        self.value = self.value.replace(old, new)
        self.lenght = len(self.value)
        
        
    def display(self):
        return self.value