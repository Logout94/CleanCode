class Point:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, top_left_point, width, height):
        self.top_left_point = top_left_point
        self.top_right_X = 0
        self.bottom_left_Y = 0
        self.width = width
        self.height = height
        self.set_end_point()

    def area(self):
        return self.width * self.height

    def set_end_point(self):
        self.top_right_X = self.top_left_point.coordX + self.width
        self.bottom_left_Y = self.top_left_point.coordY + self.height

    def print(self):
        print('Starting Point (X)): ' + str(self.top_left_point.coordX))
        print('Starting Point (Y)): ' + str(self.top_left_point.coordY))
        print('End Point X-Axis (Top Right): ' + str(self.top_right_X))
        print('End Point Y-Axis (Bottom Left): ' + str(self.bottom_left_Y))
        print('Area : ' + str(self.area()))


def get_rect(top_left_X, top_left_Y):
    top_left_point = Point(top_left_X, top_left_Y)
    rect = Rectangle(top_left_point, 90, 10)

    return rect


my_rect = get_rect(50, 100)
my_rect.print()