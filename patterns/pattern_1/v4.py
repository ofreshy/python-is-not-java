
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point(x={x}, y={y})>".format(**self.__dict__)

print(Point(x=1, y=2))
