from abc import ABC, abstractmethod
class student(ABC):
    @abstractmethod
    def show1(self):
        print("HI")

class student2(student):
    def show1(self):
        pass
    def show(self):
        print("I am overridden")


s = student2()
s.show()
