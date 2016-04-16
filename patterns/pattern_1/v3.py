from collections import namedtuple

Point = namedtuple('Point', 'x,y', verbose=False)

p = Point(x=1, y=2)
print(p)

House = namedtuple('Chromosome', 'x,y', verbose=False)

assert Point(x=1, y=3) == House(x=1, y=3)

p0 = Point(x=0, y=0)
print (p0.x)


# Good
# Concise
# Named parameters
# Use internally

# Bad
# Inherit problems with named tuple


