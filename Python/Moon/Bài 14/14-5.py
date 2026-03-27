from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Gâu Gâu!"

class Cat(Animal):
    def make_sound(self):
        return "Meow Meow!"

dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound())