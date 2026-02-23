# class defiantion

class Car : 
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand}{self.model}"
#iheritance
class ElectricCar(Car):
    def __init__(self, brand , model , battry_size):
      super().__init__(brand,model)
      self.battry_size = battry_size
      
      
another_car = ElectricCar("tsla" , "teslaa", 5000)
print(another_car.brand)  

print(isinstance(another_car, Car))

    
my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.fullname())


new_car = Car("Tata" , "Safari")
print(new_car.brand)
print(new_car.model)