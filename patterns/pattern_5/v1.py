from patterns.pattern_1.v3 import Point


class Circle(object):
    def __init__(self, centre, radius):
        self._centre = None
        self._radius = None

        self.centre = centre
        self.radius = radius

    @classmethod
    def from_circle(cls, circle):
        if not isinstance(circle, Circle):
            raise TypeError
        cls(circle.centre, circle.radius)

    @classmethod
    def from_centre_and_radius(cls, centre, radius):
        if not isinstance(centre, Point):
            raise TypeError
        if radius < 0:
            raise ValueError
        cls(centre, radius)

    @classmethod
    def from_coordinates_and_radius(cls, x, y, radius):
        if radius < 0:
            raise ValueError
        return cls(Point(x, y), radius)

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

# Yes, this is a singleton
unit = Circle(Point(0, 0), 1)
