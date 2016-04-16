from patterns.pattern_1.v2 import Point


class Circle(object):
    def __init__(self, args):
        if len(args) == 1:
            circle = args[0]
            self.centre, self.point = circle.centre, circle.point
        elif len(args) == 2:
            centre, radius = args
            self.centre, self.radius = centre, radius
        elif len(args) == 3:
            x, y, radius = args
            self.centre, self.radius = Point(x, y), radius
        else:
            raise ValueError

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError
        self._radius = radius

    @property
    def centre(self):
        return self._centre

    @centre.setter
    def centre(self, centre):
        if not isinstance(centre, Point):
            raise TypeError
        self._centre = centre
