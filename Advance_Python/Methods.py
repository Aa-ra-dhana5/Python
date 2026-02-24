# Instance Method

class Car:
    def __init__(self, name , brand):
        self.name = name
        self.brand = brand
    
    def fullName(self):
        return self.name + " "+ self.brand
    
    
Toyato = Car("Toyato" , "Marcy")
print(Toyato.fullName())

#Getter or Accesser / Setter or muter
''' Getter is to get or access data
    Setter to make change in data '''
    
    
class Mobile:
    def get_name(): #production method to define
        pass
    
    def set_name():
        pass
    
    
#class method --- used to work on class level variable
'''@classmethod is written above the method   and want parameter
   when we wan to access class variable in class '''
   
class Employee:
    company_name = "TechCorp"  # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_name):
        """Change the company name for all employees."""
        cls.company_name = new_name

    @classmethod
    def from_string(cls, emp_str):
        """Factory method to create Employee from a string."""
        name, salary = emp_str.split("-")
        return cls(name, int(salary))

# Using classmethod to modify class variable
Employee.change_company("CodeMasters")
print(Employee.company_name)  # Output: CodeMasters

# Using classmethod as a factory method
emp1 = Employee.from_string("Alice-50000")
print(emp1.name, emp1.salary)  # Output: Alice 50000

#static method -- make variable private --- USed when we wants helper method 

class Car1:
    def __init__(self, __name , __brand):
        self.name = __name
        self.brand = __brand
    
    @staticmethod
    def greeting():
        return "This is new car"
    
new_car = Car1("XUV", "700")
print(new_car.greeting())