
class Circle():

    def __init__(self, radius):
        self.radius = radius 
    
    def area(self):
        return self.radius * 3.14 
        
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
radius_input = float(input("Enter the radius of the circle: "))
circle = Circle(radius_input)

print("Area of the circle:", circle.area(),
"Perimeter of the circle:", circle.perimeter())


    
