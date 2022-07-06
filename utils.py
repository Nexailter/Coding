import random
import unittest




def check_class(character_class):
    if character_class == "Hunter" or character_class == "Demon" or character_class == 'Wizard':
        return True
    else:
        return False

def check_element(character_element):
    if character_element == 'Ice' or character_element == 'Lightning' or character_element == 'Fire' or character_element == 'Earth': 
        return True
    else:
        return False

def check_username(character_username):
    bad_words = ['fuck','fuck off',' ','shit','asshole','penis']
    if character_username not in bad_words:
        return True
    else:
        return False



def CriticalHit(damage):
    chance = random.randint(1,5)
    if(chance == 1):
        return damage *3
    else:
        return damage

def calculateDamage(offense,defender):
    damage = offense.getAttack() - defender.getDefense()
    defender.SetHealth(defender.getHealth() - damage)

def printStats(unit):
    print('Health: ' + str(unit.getHealth()))
    