from functools import lru_cache, wraps
import math
import sys
import time

from patterns.pattern_1.v2 import Point


def write_time_to(writer):
    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            writer.write(str(duration) + "\n")
            return result
        return wrapper
    return timeit


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

    @write_time_to(writer=sys.stdout)
    @lru_cache(maxsize=32)
    def contains(self, point):
        return distance(self._centre, point) <= self._radius


circle = Circle(Point(0, 0), 6)
circle.contains(Point(0, 0))



