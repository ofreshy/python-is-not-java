from patterns.pattern_1.v4 import Point


class Circle(object):
    def __init__(self, centre, radius):
        self._centre = None
        self._radius = None

        self.centre = centre
        self.radius = radius

    @property
    def centre(self):
        return self.centre

    @centre.setter
    def centre(self, centre):
        if not isinstance(centre, Point):
            raise TypeError
        self._centre = centre

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError
        self._radius = radius


c = Circle(Point(1,2), 5)
print(c)
print(c.radius)
print(c._radius)
c.radius = -10

