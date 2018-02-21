'''
Created on Nov 18, 2017

@author: rene
'''
from _pyio import __metaclass__
from abc import ABCMeta, abstractmethod

class Subscriber(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass
    
    
class SMSSubscriber(Subscriber):
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
        
    def update(self):
        print(type(self).__name__, self.publisher.get_news())

class EmailSubscriber(Subscriber):
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber(Subscriber):
    
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
        
    def update(self):
        print(type(self).__name__, self.publisher.get_news())
        
        