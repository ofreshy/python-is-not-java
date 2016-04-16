# Add characteristics here

from characteristic import attributes


@attributes(["x", "y"])
class Point(object):
    pass

print(Point(x=1, y=2))


# Good
# concise
# informative


# Bad
# Its a mini DSL
# Features are not in your control


