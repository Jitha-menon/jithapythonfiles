class Vehicle:
    def __init__(self,name,route,passengers):
        self.name=name
        self.route=route
        self.passengers=passengers

    def printv(self):
        print('vehicle name is :',self.name)
        print('bus route is :',self.route)
        print('no of passengers: ',self.passengers)


class Bus(Vehicle):
    def setv(self,speed):
        self.speed=speed
        print('bus speed is',self.speed)

obj=Bus('bus','ernakulam',55)
obj.printv()