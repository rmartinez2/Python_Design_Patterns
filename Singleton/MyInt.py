from _pyio import __metaclass__
class MyInt(type):
    def __call__(self, *args, **kwds):
        print("Here's my int", args)
        print("Now do whatever you want with these objs")
        return type.__call__(self, *args, **kwds)
    
class int(object):
    __metaclass__ = MyInt
    def __init__(self, x, y):
        self.x = x
        self.y = y
    