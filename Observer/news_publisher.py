'''
Created on Nov 15, 2017

@author: rene
'''

class NewsPublsher(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__subscribers = []
        self.__latest_news = None
        
    def attach(self, subscriber):
        return self.__subscribers.append(subscriber)
    
    def detach(self):
        return self.__subscribers.pop()
    
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]
    
    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()
            
    def add_news(self, news):
        self.__latest_news = news
        
    def get_news(self):
        return "Got News: ", self.__latest_news
    
    
        