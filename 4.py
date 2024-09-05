class Cup:
    def __init__(self, size, quanlity):
        self.size = size
        self.quanlity = quanlity
    
    def fill(self, mililitiers):
        if self.quanlity + mililitiers > self.size:
            self.quanlity = self.size
        else:
            self.quanlity += mililitiers
    def status(self):
        return self.size - self.quanlity

#Test code 
cup = Cup(100,50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())