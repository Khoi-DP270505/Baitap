class Employee:
    def __init__(self, id, frist_name, last_name, salary):
        self.id = id
        self.frist_name = frist_name
        self.last_name = last_name
        self.salary = salary
    
    def get_full_name(self):
        
        return f"{self.frist_name}{self.last_name}"
    
    def get_annual_salary(self):
        
        return self.salary * 12 #luong 12 thang
    
    def raise_salary(self,amount):
        self.salary += amount
        return self.salary
        
#Test code         
employee = Employee(744423129, "John", "Smith", 1000)

print(employee.get_full_name())

print(employee.raise_salary(500))

print(employee.get_annual_salary())
        

    