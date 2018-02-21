'''
Created on Oct 30, 2017

@author: rene
'''

class LazySingleton(object):
    '''
    classdocs
    '''

    __instance = None
    def __init__(self):
        '''
        Constructor
        '''
        if not LazySingleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.getInstance())
            
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance
        