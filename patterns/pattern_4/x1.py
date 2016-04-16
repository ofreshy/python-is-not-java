from patterns.pattern_1.v2 import Point
from patterns.pattern_4 import Circle

import time


class TimeContainCircle(Circle):
    def __init__(self, centre, radius):
        super(TimeContainCircle, self).__init__(centre, radius)

    def contains(self, point):
        start = time.time()
        result = super(TimeContainCircle, self).contains(point)
        duration = time.time() - start
        print(duration)
        return result


a = TimeContainCircle(Point(1, 1), 5)
a.contains(Point(1, 1))





