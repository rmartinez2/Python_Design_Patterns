'''
Created on Nov 2, 2017

@author: rene
'''

class HealthCheck(object):
    '''
    classdocs
    '''
    _instance = None

    def __new__(cls, *args, **kwargs):
        '''
        Constructor
        '''
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance
        
    def __init__(self):
        self._servers = []
        
    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
    
    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")
