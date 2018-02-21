'''
Created on Oct 31, 2017

@author: rene
'''
from _pyio import __metaclass__
from IPython.core.history import sqlite3

class MetaSingleton(type):
    '''
    classdocs
    '''
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self._instances[self]
        
class Logger(object):
    __metaclass__ = MetaSingleton
    pass


class Database(object):
    __metaclass__ = MetaSingleton
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj