'''
Created on Nov 3, 2017

@author: rene
'''

import ast

from Factory.AbstractFactory import PizzaStore
from Factory.SimpleFactory import ForestFactory


if __name__ == '__main__':
    ff = ForestFactory()
    
    animal = raw_input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
    
#     profile_type = raw_input("Which Profile would you like to create? [LinkedIn or Facebook]")
#     profile = ProfileFactory().create_profile(profile_type)
#     print("Creating Profile...", type(profile).__name__)
#     print("Profile has sections --", profile.get_sections())

    pizza = PizzaStore()
    pizza.make_pizzas()