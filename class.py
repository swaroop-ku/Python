class myclass:
    def __init__(self):
        self.name = (input("Enter the name:"))
        self.age = int(input("Enter the age:"))

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

    def __del__(self):
        print("I am distructor")

s1 = myclass()
s2 = myclass()
s1.display()
s2.display()