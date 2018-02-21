'''
Created on Nov 18, 2017

@author: rene
'''
from Observer.news_publisher import NewsPublsher
from Observer.subscriber import SMSSubscriber, EmailSubscriber,\
    AnyOtherSubscriber

if __name__ == '__main__':
    news_publisher = NewsPublsher()
    
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print("Subscribers: ", news_publisher.subscribers())
    
    news_publisher.add_news("Hello World")
    news_publisher.notify_subscribers()
    
    print("Detached: ", type(news_publisher.detach()).__name__)
    print("Subscribers ", news_publisher.subscribers())
    
    news_publisher.add_news("My Second News")
    news_publisher.notify_subscribers()