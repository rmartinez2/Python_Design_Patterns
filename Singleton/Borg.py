'''
Created on Oct 30, 2017

@author: rene
'''

class Borg:
    '''
    classdocs
    '''

    __shared_state = {"1": "2"}
    
    def __init__(self):
        '''
        Constructor
        '''
        self.x = 1
        self.__dict__ = self.__shared_state
        pass