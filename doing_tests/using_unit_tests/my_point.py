# from memory_profiler import profile # use as a decorator

# @profile
class Point():
    points = 0 # static property
    # restrict the properties to these slots
    __slots__ = ('__x', 'y')
    @staticmethod
    def how_many_points():
        return Point.points
    def __init__(self, x=0, y=0):
        self.x = x # uses the setter for __x
        self.y = y
        Point.points += 1
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x) == int:
            self.__x = new_x
        else:
            raise TypeError
    def move_by(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def where_am_i(self):
        print('Point instance at x:{0:.2f} y:{1:.2f}'.format(self.x, self.y))
    def display(self):
        return (self.x, self.y)
    def hypot(self):
        '''return the hypotenuse given x and y'''
        h = (self.x*self.x + self.y*self.y)**0.5
        return h
        
if __name__ == '__main__':
    p1 = Point(5, 7)
    p2 = Point(3, 4)
    p2.where_am_i()
    print(Point.how_many_points())
    p4 = Point()
    p4.where_am_i() # shoild be default 0,0
    p4.move_by(-3,-4)
    p4.where_am_i()
    # p4.otherProp = 'cant happen' # should fail
    # p3 = Point('3', 4) # rasies a typeError

    