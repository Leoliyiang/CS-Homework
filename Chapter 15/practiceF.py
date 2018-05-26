class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(2,4)  # Instantiate an object of type Point
q = Point(7,11)  # Make a second point
print(p.x, p.y)  # Each point object has its own x and y

print(p.x,p.y,q.x,q.y)
print("(x={0},y={1})".format(p.x,p.y))
distance_((self.x ** 2) + (self.y ** 2)) ** 0.5
pdist = p.distance_from_origin()
print()