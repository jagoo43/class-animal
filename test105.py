from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass
class human(animal):
    def move(self):
        print("human can walk")
class dog(animal):
    def move(self):
        print("dog can run")
h=human()
h.move()
d=dog()
d.move()