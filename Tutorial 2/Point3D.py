class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def print_point_info(self):
    print("(%d, %d, %d)" % (self.x, self.y, self.z))

my_point = Point3D(1, 2, 3)
my_point.print_point_info()
