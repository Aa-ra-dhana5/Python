# Namespace represents a memory block where names are mapped to objects

# class Namespace -- Names are mapped to class variables
# Instance Namespace - Names are mapped to instance variables


''' Change in Class variable reflects to all other static variable 
      but change in instatnce stick to that specific variable value '''

class Movie:
    favorite ="yes"
    
Comedy = Movie()
print("Comedy movies ? " , Comedy.favorite)

Horror = Movie()
Horror.favorite = "no"
print("Horror movies? ", Horror.favorite)
print("All other movies ?  " , Movie.favorite)

sci_fi = Movie()
print("sci-fi moveies? " , sci_fi.favorite)