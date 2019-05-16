from abc import ABCMeta, abstractmethod
from random import randint, randrange, choice
import time


class Fighter(object, metaclass = ABCMeta):
    
    __slots__ = ('_name', '_hp')
    
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def hp(self):
        return self._hp
        
    @hp.setter
    def hp(self):
        self._hp = hp
        
    @abstractmethod
    def attack(self, other):
        
        pass