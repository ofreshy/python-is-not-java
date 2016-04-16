import time

from patterns.pattern_1.v2 import Point
from patterns.pattern_4 import Circle


class TimeContainCircle(object):
    def __init__(self, circle):
        self.circle = circle

    def contains(self, point):
        start = time.time()
        result = self.circle.contains(point)
        duration = time.time() - start
        print(duration)
        return result


a = TimeContainCircle(Circle(Point(1, 1), 5))
a.contains(Point(1, 1))

