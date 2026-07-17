class Circle:

    PI = 3.14

    def __init__(self,radius):
        self.radius = radius

    def Accept(self):
        self.radius = float(input("Enter radius: "))

    def calculateArea(self):
        return self.PI * self.radius * self.radius

    def calculateCircumference(self):
        variable = self.PI * self.radius * 2
        return variable

    def Display(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.calculateArea()}")
        print(f"Circumference: {self.calculateCircumference()}")

#creating multiple objects
obj1 = Circle(0)
obj2 = Circle(0)

#calling methods on objects
obj1.Accept()
obj2.Accept()

obj1.Display()
obj2.Display()
