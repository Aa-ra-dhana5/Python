#Static Methods:Static methods are meant to be called using the class, but Python allows calling them via instances too.
#Instance → Class → Parent Class (attribute lookup order)

class Car : 
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
       
    @staticmethod
    def making_static():
        return "This is static method"


      
      


    
my_car = Car("Toyota", "Corolla")
print(my_car.making_static())
print(Car.making_static())

