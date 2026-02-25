## Abstract Class
--A class that cannot be instantiated and is meant to be inherited by other classes.
-- can not careate direct object from abasratct calss

It usually contains:
1.One or more abstract methods (methods without implementation)
2.Can also contain concrete methods (normal methods)

## How to create abstract class
--ABC is a special base class from Python’s built-in abc module that allows a class to contain abstract methods and prevents it from being instantiated.

exa: 
'''
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
'''


without abc
exa:
''' 
class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement this method")
'''

# When do we use it
--We Want to Define a Common Structure
Example: All animals must have sound().

--When We Want to Force Rules
Suppose you are building a payment system.
Every payment method must implement pay().




'''Abstract class = Blueprint
Abstract method = Rule that must be followed
Concrete method = Ready-made implementation'''





## Interface
-- wehn the abstract class has only the abstarct methods then its called interface

-- when to use
-- all features need to be implented

