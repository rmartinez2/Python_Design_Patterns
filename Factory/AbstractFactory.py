'''
Created on Nov 4, 2017

@author: rene
'''
from _pyio import __metaclass__
from abc import ABCMeta, abstractmethod

class PizzaFactory(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def create_veg_pizza(self):
        pass
    
    @abstractmethod
    def create_non_veg_pizza(self):
        pass
    

class IndianPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return DeluxeVeggiePizza()
    
    def create_non_veg_pizza(self):
        return ChickenPizza()
    

class USPizzaFactory(PizzaFactory):
    
    def create_veg_pizza(self):
        return MexicanVegPizza()
    
    def create_non_veg_pizza(self):
        return HamPizza()
    
    
class VegPizza(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def prepare(self, VegPizza):
        pass
    
class NonVegPizza(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def serve(self, VegPizza):
        pass
    
class DeluxeVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)
        
class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with chicken on ", type(VegPizza).__name__)
        
class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)
        
class PizzaStore:
    def __init__(self):
        pass
    
    def make_pizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)
            
                
    
    
        