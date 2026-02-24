#Instance Variable
''' Each Instance has seprate copy for each object'''

class Car:
    def __init__(self):
        self.brand = "Toyato"
        
NewCar = Car()
print(NewCar.brand)


#Class Variable / Static Variable
''' Single copy for each instatnce -- Change reflect to all'''

class Movie:
    favorite = 'yes'
    def __init__(self, name , duration):
        self.name = name
        self.duration = duration
        
    @classmethod
    def is_fav(cls):   #accessing variable in class
        cls.favorite

horror = Movie("vash" , 1.30 )
print(horror.name)
Movie.favorite = "no"
print(Movie.favorite)
        
comedy = Movie("Entertainment" , 1.50 )
print(comedy.name)
print(Movie.favorite)


