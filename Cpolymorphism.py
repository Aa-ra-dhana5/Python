# polyorphism 
#1. MEthod overridng  -child class changes parent class method 
#like in below example the super class Car has method fuel type and the subclass overrides that method 

#2.Method overloading -- pyhton doesnt support this directly 
# but it has default parameter sharing and *args to implement the concept of method loading 
# same method diffrent parameter


class Car : 
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand}{self.model}"
    
    def fuel_type(self):
        return "Petrol Fuel"

class ElectricCar(Car):
    def __init__(self, brand , model , battry_size):
      super().__init__(brand,model)
      self.battry_size = battry_size
      
    def fuel_type(self):
        return "Charge Fuel"
      
      
another_car = ElectricCar("tsla" , "teslaa", 5000)
# print(another_car.brand)  
print(another_car.fuel_type())

    
my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())

