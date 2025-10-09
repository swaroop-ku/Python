class book:
    def __init__(self,name,author):
        self.name = name
        self.author = author

    def show(self):
        print(f"The name of book is {self.name} and author is {self.author}")

name = input("Enter the name of the book:")
author = input("Enter name of author:")

b1 = book(name,author)
b1.show()