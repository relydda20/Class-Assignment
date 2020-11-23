import math

class Circle:
    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = float(radius)
        self.__color = str(color)

    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        self.__radius = radius
    
    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def toString(self):
        return f"Radius is {self.setRadius()} and color is {self.setColor()}."

    def getArea(self):
        return math.pi * self.getRadius()**2

class Cylinder(Circle):
    def __init__(self, color, radius, height = 1.0):
        self.__height = float(height)
        super().__init__(radius, color)
    
    def getHeight(self):
        return self.__height
    
    def setHeight(self, height):
        self.__height = height

    def toString(self):
        return f"The Height is {self.setHeight()}, the radius is {self.setRolor()}, and the color is {self.setColor()}."
        
    def getVolume(self):
        return self.getArea() * self.setHeight()