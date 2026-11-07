class Car:
    def __init__(self, make, model, year,color) :
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started='False'
        self.speed=0
        self.maximum_speed=200
        self.showroom='NewAge'
    @classmethod
    def change_showroom(cls,new_showroom):
        cls.showroom = new_showroom
    def __str__(self):
        return f"{self.make}{self.model}{self.color|}{self.year}"

toyota_camry=Car('Toyota','Camry','2022','red')
ford_mustang=Car('Ford','Mustang','2022','black')
print(ford_mustang.make)
print(ford_mustang.model)
print(ford_mustang.year)
print(ford_mustang.speed)
print(ford_mustang.started)
print(ford_mustang.maximum_speed)
print(toyota_camry.make)
print(toyota_camry.model)
print(toyota_camry.year)
print(toyota_camry.color)
print(toyota_camry.speed)
print(toyota_camry.started)
print(toyota_camry.maximum_speed)
try:
    print(Car.make)
except AttributeError as e:
    print("Attribute Error",e)
print(Car.__dict__)
Car.change_showroom('OldAge')
print(Car.__dict__)#showroom value changed to the new one
print(toyota_camry.__dict__)
str(toyota_camry)
