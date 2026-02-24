## Single inheritance
class Father:
    money =1000
    def __init__(self):
        print("Father class constructor")
    def show(self):
        print("this is Parent method")
    
    @classmethod
    def show_money(self):
        print("Parent money : " , self.money)
        
class Son(Father):
    def disp(self):
        print("Child class method")
    
    def show_money(self): #Method overriding
        print("chidl money inheritaed from parent", Father.money)
        
s = Son()# will printFather class constructor

s.disp()
s.show()
s.show_money()
        
'''Constructor Lookup Order

When creating object, Python checks:

Does this class have __init__?

If not → check parent class

If not → check parent’s parent

Finally → uses object.__init__'''

'''
     object
       |
    Class
       |
    Instance
'''
    
    
#What happpeds when father class has one constructor and child class has one constructor
#constructor over riding -to modify behaviour of parent class
# will print what ever written in child class
class Building:
    def __init__(self):
        print("This is building")
        
class Room:
    def __init__(self):
        print("this is room")
        
R = Room() # will print "this is room"



#calling parent class constructor to child class

class Animal:
    def __init__(self):
        print("This is Animal class")

class Cat(Animal):
    def __init__(self): # will call parent class constructor
        super().__init__()
        print("This is Subclass of Cat")
        
new_pet = Cat()
#will pritn "This is Animal class \n This is Subclass of Cat"







## Multilevel inheritance

class Father:
    pass

class Son(Father):
    pass

class GrandSon(Son):
    pass


## Hierarical inheritance -- One parent class and multiple sub classes

class Father:
    pass

class Son(Father):
    pass

class Daughter(Father):
    pass


## Multiple inheritance -- when subclass is mix of more than one parent class
# MRO see OOP.md
class Father:
    def __init__(self):
        print("This is Father class Constructor")

class Mother:
    def __init__(self):
        print("This is Mother class Constructor")
        
class Son(Mother , Father):
    pass

s = Son()



# if we wants to show both parent classes constructor
class Father1:
    def __init__(self):
        super().__init__()
        print("This is Father class Constructor")

class Mother1:    
    def __init__(self):
        super().__init__()
        print("This is Mother class Constructor")
        
class Son(Father1, Mother1):
    pass

s = Son()
''' Father1 has super().__init__() inside his constructor so its parent object class's concstucto is called 
   Object  does not have any constructor so the search will continue dowright hand side class of object class so Mother class's constructor is called
 '''
