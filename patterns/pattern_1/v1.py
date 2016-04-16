class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


p = Point(1, 2)
print(p)


# Good
# Looks and feels like Java

# Bad
# Very verbose
# Can easily pass the methods
# Python users will most likely access attributes directly
