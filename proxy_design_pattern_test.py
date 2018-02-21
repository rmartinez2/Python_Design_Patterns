'''
Created on Nov 5, 2017

@author: rene
'''
from Proxy.Proxy import Agent, You


if __name__ == '__main__':
    r = Agent()
    r.work()
    
    me = You()
    me.make_payment()