
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector2):
        return Vector(self.x + vector2.x, self.y + vector2.y)

    def subtract(self, vector2):
        return Vector(self.x - vector2.y, self.y - vector2.y)

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

v = Vector(1,2)
v2 = Vector(3,4)

print "Vector 1 is %s" % v
print "Vector 2 is %s" % v2

print v.add(v2)

print v.subtract(v2)

print "A vector with floats %s" % Vector(1.0, 2.0)
