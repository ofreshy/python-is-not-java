from patterns.pattern_1.v5 import Point


class Circle(object):
    def __init__(self, centre, radius):
        self.set_centre(centre)
        self.set_radius(radius)

    def set_centre(self, centre):
        if not isinstance(centre, Point):
            raise TypeError
        self._centre = centre

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError
        self.radius = radius

# Good
# Easy to read

# Bad
# Client code access r directly



