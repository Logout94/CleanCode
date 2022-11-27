class Point:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def end_points(self):
        top_right = self.top_left.coordX + self.width
        bottom_left = self.top_left.coordY + self.height
        print('Starting Point (X)): ' + str(self.top_left.coordX))
        print('Starting Point (Y)): ' + str(self.top_left.coordY))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_stuff():
    top_left = Point(50, 100)
    rect = Rectangle(top_left, 90, 10)

    return rect


my_rect = build_stuff()

print(my_rect.area())
my_rect.end_points()