class book:
    profession=""
    def __init__(self):
        self.profession = input("Enter the profession:")

class members(book):
    def borrow(self):
        self.total = int(input("Enter total number of books you want to borrow:"))
        if self.profession == "student" and self.total <= 3 and self.total > 0:
            print(f"{self.total} books borrowed successfully")
        elif self.profession == "faculty" and self.total <= 5 and self.total > 0:
            print(f"{self.total} books borrowed successfully")
        elif self.total == 0:
            print("books not issued")
        else:
            print("You cannot borrow that much books")
            self.total = 0

    def rt(self):
        print("Books returned successfully")

class library(members):
    def record(self):
        print("\n**Library Record**")
        print(f"Profession:{self.profession}")
        print(f"Number of books issued:{self.total}")
        if self.total != 0:
            self.rt()

l1 = library()
l1.borrow()
l1.record()