'''
Created on Oct 30, 2017

@author: rene
'''

class Singleton(object):
    '''
    classdocs
    '''

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance