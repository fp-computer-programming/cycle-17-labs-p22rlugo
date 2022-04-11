# Ryan Lugo: RJL 4/11/22
import math

class Circle:
    """ Circle class represents a circle """

    def __init__(self):
        """ Create a new circle with radius 1 """
        self.radius = 3

    def get_diameter(self):
        """ Calculate diameter of circle"""
        return self.radius * 2

    def get_area(self):
        """ Calculate area of circle"""
        return math.pi * self.radius **2

    def get_perimeter(self):
        """ Calculate perimeter of circle """
        return 2 * math.pi * self.radius

my_circle = Circle()
print(my_circle.get_perimeter())