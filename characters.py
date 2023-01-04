attack = 0
defense = 0
speed = 0
health = 0
element = ''
name = ''


class Person:
    def __init__(self,health,attack,defense,speed,name,element):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.name = name
        self.element = element


    def getAttack(self):
        return self.attack
    
    def getDefense(self):
        return self.defense
    
    def getSpeed(self):
        return self.speed

    def getName(self):
        return self.name
    
    def getElement(self):
        return self.element

    def getHealth(self):
        return self.health

    def setAttack(self,a):
        self.attack = a
        
    def setDefense(self,a):
        self.attack = a

    def SetSpeed(self,a):
        self.attack = a

    def SetName(self,a):
        self.attack = a
        
    def SetElement(self,a):
        self.attack = a

    def SetHealth(self,a):
        self.attack = a

#inheriting from person
class Demon(Person):
    def __init__ (self,health,attack,defense,speed,name,element):
        super().__init__(health,attack,defense,speed,name,element)

    def demon_cry(self):
        print("deals 100 damage to all enimies in a ten yard radius")

class Wizard(Person):
    def __init__ (self,health,attack,defense,speed,name,element):
        super().__init__(health,attack,defense,speed,name,element)

    def elemental_meteor(self):
        print('Deals 20 damage to all enimies in a 15 yard radius')
        
class Hunter(Person):
    def __init__ (self,health,attack,defense,speed,name,element):
        super().__init__(health,attack,defense,speed,name,element)

    def knife_throw(self):
        print("deals 150 damage to one enemy")



class Monsters():
    def __init__(self):
        self.attack = 10
        self.defense = 10
        self.speed = 10
        self.spawnrate = 10
        self.health = 40
        self.name = 'monster'


    def getAttack(self):
        return self.attack

    def getspawnrate(self):
        return self.attack
    
    def getDefense(self):
        return self.defense
    
    def getSpeed(self):
        return self.speed

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def setAttack(self,a):
        self.attack = a
        
    def setDefense(self,a):
        self.defense = a

    def SetSpeed(self,a):
        self.speed = a

    def SetName(self,a):
        self.name = a

    def setspawnrate(self,a):
        self.spawnrate = a

    def SetHealth(self,a):
        self.health = a


class lochness_monster(Monsters):
    def __init__ (self,health,attack,defense,speed,name):
        super().__init__(health,attack,defense,speed,name)

    def grab_player(self):
        print('deals 100 damage to character')

class Kraken(Monsters):
    def __init__ (self,health,attack,defense,speed,name):
        super().__init__(health,attack,defense,speed,name)

    def grab_ship(self):
        print('either abandon ship or die')

class knight(Monsters):
    def __init__ (self,health,attack,defense,speed,name,):
        super().__init__(health,attack,defense,speed,name,)

    def sword_jab(self):
        print('deals 25 damage unless you dodge')

class ork(Monsters): 
    def __init__ (self,health,attack,defense,speed,name,):
        super().__init__(health,attack,defense,speed,name,)

    def arm_break(self):
        print("only does 5 damage but makes attack arm unusable")

class merchant(Monsters):
    def __inti__ (self,health,attack,defense,speed,name,):
        super().__init__(health,attack,defense,speed,name,)

    def heal_player(self):
        print("adds 10 health to player")


