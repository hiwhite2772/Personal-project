class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
rect = Rectangle(12, 12)
cir = Circle(5)
print(f"Diện tích hình chữ nhật: {rect.area()}")
print(f"Diện tích hình tròn: {cir.area()}")