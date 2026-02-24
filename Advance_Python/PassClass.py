#Passing methods and varibles of one class to another class -- using static method

'''I use inheritance when there is an IS-A relationship and I need polymorphism or shared behavior.
   I use static methods when I need utility functions that don’t depend on object or class state.'''
   

#inheritance

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

d = Dog()
d.eat()   # inherited
d.bark()


#static

class Helper:
    @staticmethod
    def greet():
        print("Hello")

class Person:
    def say(self):
        Helper.greet()
        
new_man = Person()
new_man.say()