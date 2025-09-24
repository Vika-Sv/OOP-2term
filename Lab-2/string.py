class String:
    def __init__(self, text=''):
        self.text = text
        self.length = len(text)
    
    def search(self, sub):
        return sub in self.text
    
    def insert(self, sub, pos):
        if 0 <= pos <= self.length:
            self.value = self.value[:pos] + sub + self.value[pos:]
            self.length = len(self.value)

    def replace(self, old, new):
        self.value = self.value.replace(old, new)
        self.length = len(self.value)

    def display(self):
        print(self.value)