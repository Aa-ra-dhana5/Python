from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name   # attribute

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("bark")


pet = Dog("Tommy")
pet.sound()
print(pet.name)

# new_pet = Animal()
#TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'sound'