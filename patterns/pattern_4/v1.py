import math
import time

from patterns.pattern_1.v2 import Point


def timeit(contains):
    def wrapper(point):
        start = time.time()
        result = contains(point)
        duration = time.time() - start
        print(duration)
        return result
    return wrapper


def distance(p1, p2):
    if p1 is None or p2 is None:
        raise ValueError('None point')
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx * dx + dy * dy)


class Circle(object):
    def __init__(self, centre, radius):
        self._centre = None
        self._radius = None

        self.centre = centre
        self.radius = radius
        self.contains = timeit(self._contains)

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

    def _contains(self, point):
        return distance(self._centre, point) <= self._radius


circle = Circle(Point(0, 0), 6)
circle.contains(Point(1, 0))






