from fighter import Fighter
from random import randint, randrange, choice
import time

class Monster(Fighter):
    
    __slots__ = ('_name', '_hp')
    
    def attack(self, other):
        
        probability_to_hit = choice([True, False])
        
        if probability_to_hit:
            attack_point = randint(30, 60) if self._hp <= 10 else randint(10, 50)
            
            if other._defense:
                half_point = 0.5*attack_point
                print('%s has shielded %d damange.'%(other._name, half_point))
                attack_point -= half_point
                other._defense = False
                
            other._hp -= attack_point if other._hp >= attack_point else other._hp
            print('%s has swinged %d damage to %s. %s lost %d hp.' %(
                self._name, 
                attack_point,
                other._name,
                other._name,
                attack_point))
            
        else:
            attack_point = 0            
            print('%s failed the attack.' % (self._name))
            if other._defense:
                other.defense = False

            recover_magic = 5
            other._mp += recover_magic
            print('%s has gained %d magic power.' % (other._name, recover_magic))

            
    
    def __str__(self):
        return '%s has %d hp.' % (self._name, self._hp)