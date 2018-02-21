'''
Created on Nov 4, 2017

@author: rene
'''
from _pyio import __metaclass__
from abc import ABCMeta, abstractmethod

#Section is the Product Interface
class Section(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def describe(self, params):
        pass
    
#Next Sections are Concrete Product Classes
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")
        
class AlbumSection(Section):
    def describe(self):
        print("Album Section")
        
        
class PatentSection(Section):
    def describe(self):
        print("Patent Section")
        

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")
        

#Profile is the Creator class        
class Profile(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.sections= []
        self.create_profile()
        
    @abstractmethod
    def create_profile(self):
        pass
    
    def get_sections(self):
        return self.sections
    
    def add_sections(self, section):
        self.sections.append(section)
        
#Next two classes are Concrete Creators        
class linkedin(Profile):

    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())

class facebook(Profile):
    
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())    

#class ProfileFactory(object):
#    def create_profile(self, profile_type):
#        return eval(profile_type.lower())()

if __name__ == '__main__':
    profile_type = raw_input("Which Profile would you like to create? [LinkedIn or Facebook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile...", type(profile).__name__)
    print("Profile has sections --", profile.get_sections())