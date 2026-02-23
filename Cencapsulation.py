class Car:
    def __init__(self, brand , model):
        self.__brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.__brand}{self.model}"
    
    def get_brand(self):
        return self.__brand
    

my_car = Car("Toyato" , "tmmm")
# print(my_car.brand)
# __brand make this attribute private not accessable by object jolny class can access it
print(my_car.get_brand())