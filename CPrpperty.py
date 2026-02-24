#property decorator to make sure the model attribute should be read only


class Car : 
    def __init__(self, brand , model):
        self.__brand = brand
        self.__model = model
       
    @staticmethod
    def making_static():
        return "This is static method"
    
    @property
    def moddel(self):
        return self.__model


      
      


    
my_car = Car("Toyota", "Corolla")
# my_car.moddel = "newModel" ---> this has no setter method
print(my_car.moddel)

