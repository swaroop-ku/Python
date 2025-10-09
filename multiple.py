# multiple Inheritance
class grandfather:
    def call(self):
        print("I am the grand parent")

class father:
    def call1(self):
        print("I am parent")

class boy(grandfather, father):
    def call2(self):
        print("I am the child")

b = boy()
b.call()  
b.call1()  
b.call2()  
