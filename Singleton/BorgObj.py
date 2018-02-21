'''
Created on Oct 30, 2017

@author: rene
'''

class BorgObj(object):
    '''
    classdocs
    '''
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(BorgObj, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj