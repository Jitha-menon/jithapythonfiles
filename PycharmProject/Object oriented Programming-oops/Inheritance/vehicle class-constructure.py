class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color

    def print(self):
        print(self.model,self.regno,self.color)
    def __str__(self):
        return self.model+self.color

obj=Vehicle('ktm',6757647,'black')
obj.print()
print(obj)