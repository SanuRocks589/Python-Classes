from abc import ABC, abstractmethod 

class Abcmethod(ABC):
    def print(self, x):
        print(f"Passed Value: {x}.")
    @abstractmethod
    def task(self):
        print("We are inside the abstract class.")

class subclass(Abcmethod):
    def task(self):
        print("We are inside the subclass, implementing the task")
    def inside(self):
        print("We are inside the subclass.")

obj = subclass()
obj.task()
obj.print(7)