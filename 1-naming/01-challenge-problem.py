class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, top_left_point, width, height):
        self.top_left_point = top_left_point
        self.top_right_x = 0
        self.bottom_left_y = 0
        self.width = width
        self.height = height
        self.set_end_point()

    def get_area(self):
        return self.width * self.height

    def set_end_point(self):
        self.top_right_x = self.top_left_point.x + self.width
        self.bottom_left_y = self.top_left_point.y + self.height

    def print(self):
        print('Starting Point (X)): ' + str(self.top_left_point.x))
        print('Starting Point (Y)): ' + str(self.top_left_point.y))
        print('End Point X-Axis (Top Right): ' + str(self.top_right_x))
        print('End Point Y-Axis (Bottom Left): ' + str(self.bottom_left_y))
        print('Area : ' + str(self.get_area()))


def get_rectangle(top_left_x, top_left_y):
    top_left_point = Point(top_left_x, top_left_y)
    rectangle = Rectangle(top_left_point, 90, 10)

    return rectangle


user_rectangle = get_rectangle(50, 100)
user_rectangle.print()