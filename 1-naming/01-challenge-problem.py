class Point:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.top_right = 0
        self.bottom_left = 0
        self.width = width
        self.height = height
        self.set_end_point()

    def area(self):
        return self.width * self.height

    def set_end_point(self):
        self.top_right = self.top_left.coordX + self.width
        self.bottom_left = self.top_left.coordY + self.height

    def print(self):
        print('Starting Point (X)): ' + str(self.top_left.coordX))
        print('Starting Point (Y)): ' + str(self.top_left.coordY))
        print('End Point X-Axis (Top Right): ' + str(self.top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(self.bottom_left))


def get_rect(coordX, coordY):
    top_left = Point(coordX, coordY)
    rect = Rectangle(top_left, 90, 10)

    return rect


my_rect = get_rect(50, 100)

print(my_rect.area())
my_rect.print()