class vehicle:
    def intro(self):
        print("I am a vehicle")

class two_wheeler(vehicle):
    def wheels(self):
        print("I have 2 wheels")

class four_wheeler(vehicle):
    def wheels(self):
        print("I have 4 wheels")

class hybrid_vehicle(two_wheeler, four_wheeler):
    def type(self):
        print("I am a hybrid vehicle")

h = hybrid_vehicle()
h.intro()   
h.wheels()  
h.type()     
