from fighter import Fighter
from player import Player
from monster import Monster
from random import randint, randrange, choice
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


def main():
    player_name = input('Please put your name: ')
    print('\n')
    

    #monster_names = ['SocksBeast', 'DJ', 'FoxKill', 'Chameleon', 'Chupacapra', 'Kappa', 'Kaiju']
    monster_names = ['Chupacapra', 'Kappa']
    monsters = {}
    for name in monster_names:
        monsters[name] = Monster(name, randint(50, 150))
    
    monster_choice = choice(list(monsters.keys()))
    monster = monsters[monster_choice]
    protential_hp_gain = int(0.3 * monster._hp)
    #monster_Kaiju = Monster('Kaiju', randint(50, 150))
    player = Player(player_name, 60, 30+(monster.hp)*0.25, False)

    
    # welcome speech
    
    delay_print('%s Prepare to die~~~' % player._name)
    print('\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(player)
    print(monster)
    #print(monster_Kaiju)
    median_delay_print('There are %d monsters in this universe.' % len(monsters))
    print('\n')
    
    code_name = True
    need_new_monster = False
    #while player._hp > 0 and monster_Kaiju._hp > 0 and code_name:
    
    while len(monsters) > 0 and player._hp > 0 and code_name:
        
        # create new monster
        if need_new_monster:
            
            print('A new monster is chosen...')
            monster_choice = choice(list(monsters.keys()))
            monster = monsters[monster_choice]
            time.sleep(2)
            print('%s just jumps on you!' % (monster._name))
            print(monster)
            protential_hp_gain = int(0.3 * monster._hp)
        
        while monster._hp > 0 and player._hp > 0 and code_name:
        #game start
    
            # player turn
            print('\n')
            median_delay_print('%s is planning...' % (player._name))
            while True:
                action = input('Choose an action: f: fight, s: spell, d: defend, q: quit: ')
                if action not in ['f', 's', 'd', 'q']:
                    print('Please enter valid command.')
                else:
                    break
                
            print('\n')
        
            print('*******************************', '\n')
            if action == 'f':
                #time.sleep(2)
                player.attack(monster)
        
            if action =='s':
                #time.sleep(2)
                player.magic_attack(monster)
        
            if action == 'q':
                code_name = False
                break
        
            if action == 'd':
                #time.sleep(2)
                player.defense = True
                player.defend()
        
            print('*******************************', '\n')
            median_delay_print('Current Status: ')
            print('\n')
            print(player)
            print(monster)
            
            # monster is dead
            if monster.hp <= 0:
                
                delay_print('%s is dead.' % (monster._name))
                delay_print('%s gets %d hp.' % (player._name, protential_hp_gain))
                player._hp += protential_hp_gain
                del monsters[monster._name]
                need_new_monster = True

                delay_print('%s wins the battle!' % (player._name))
            
            else:
            # monster turn
                time.sleep(5)
                print('\n')
                delay_print('%s turn.' % (monster._name))
                #time.sleep(2)
                print('\n')
            
                print('*******************************', '\n')
                monster.attack(player)
                print('*******************************', '\n')      
                time.sleep(3)
                print('Current Status: ', '\n')
                print(player)
                print(monster)
        

            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    if len(monsters) > 0:
        delay_print('Moster wins! It is destiny!')
        
    else:
        delay_print('%s wins the all battle! You are the real winner!' % player._name)

if __name__ == '__main__':
    main()