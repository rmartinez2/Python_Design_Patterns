'''
Created on Nov 3, 2017

@author: rene
'''
from _pyio import __metaclass__
from abc import ABCMeta, abstractmethod
import ast


class Animal(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_say(self):
        pass
    
class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")
        

class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")
        

class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()
