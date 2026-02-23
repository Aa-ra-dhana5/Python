# Class Variable -- count total car created by Car class


class Car : 
    
    total_car = 0
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    
    def fullname(self):
        return f"{self.brand}{self.model}"
    
    def fuel_type(self):
        return "Petrol Fuel"

class ElectricCar(Car): #2
    def __init__(self, brand , model , battry_size):
      super().__init__(brand,model)
      self.battry_size = battry_size
      
    def fuel_type(self):
        return "Charge Fuel"
      
      
# another_car = ElectricCar("tsla" , "teslaa", 5000)
# # print(another_car.brand)  
# print(another_car.fuel_type())

    
my_car = Car("Toyota", "Corolla") #1
print(my_car.fuel_type())

print(Car.total_car) # answer is 2

