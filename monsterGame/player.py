from random import randint, randrange, choice
from fighter import Fighter
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

def median_delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Player(Fighter):
    
    
    __slots__ = ('_name', '_hp', '_mp', '_defense')
    
    def __init__(self, name, hp, mp, defense = False):
        super().__init__(name, hp)
        self._mp = mp
        self._defense = defense
        
    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, mp):
        self._mp = mp
        
    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, defense):
        self._defense = defense
        
    def attack(self, other):
        delay_print('%s swinged the sword.'% self._name)
        attack_point = randint(15, 25)
        other._hp -= attack_point if other._hp > attack_point else other._hp
        median_delay_print('%s has lost %d hp.'% (other._name, attack_point))
        
    def magic_attack(self, other):
        print('%s cast the spell.' %self._name)
        if self._mp >= 10:
            magic_point = randint(10, 50) if self._hp > 10 else randint(30, 60)
            other._hp -= magic_point if other._hp >= magic_point else other._hp
            median_delay_print('%s has lost %d hp.'% (other._name, magic_point))
            self._mp -= 10
            median_delay_print('%s consumed %d magic points.'% (self._name, 10))

        else:
            median_delay_print('Not enough mp. Use physical attack.')
            self.attack(other)
                
    def defend(self):
        self._hp += 20

        
    def __str__(self):
        return '%s has %d hp and %d mp.' %(self._name, self._hp, self._mp)
