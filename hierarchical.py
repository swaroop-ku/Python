class vechicle:
    def intro(self):
        print("I am vechicle")
class two_wheeler(vechicle):
    def show(self):
        super().intro()
        print("I am Two - Wheeler")
class four_wheeler(vechicle):
    def show(self):
        super().intro()
        print("I am four - Wheeler")
class truck(vechicle):
    def show(self):
        super().intro()
        print("I am truck i have more than 4 wheels")
t = two_wheeler()
t.show()
f = four_wheeler()
f.show()
T = truck()
T.show()