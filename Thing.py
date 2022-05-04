from PIL import Image


class demon:
    def __init__ (self, attack, defense, speed, name, element):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        self.element = element


#FUNCTIONSAREFUN!!!
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

    def setAttack(self,a):
        self.attack = a

    #Dislplay Image
    def character_image(self):
        image = Image.open("Demon.png")
        image.show()





MathewIsOP = demon(100, 200, 300, 'Matthew', 'Earth')

# print (MathewIsOP.getAttack())

# print (MathewIsOP.getDefense())

# print (MathewIsOP.getSpeed())

# print (MathewIsOP.getName())

# print (MathewIsOP.getElement())

# MathewIsOP.setAttack(1000)
# print (MathewIsOP.getAttack())

# MathewIsOP.character_image()








class Wizard:
    def __init__ (self, attack, defense, speed, health, name, element):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        self.element = element
        self.health = health


#FUNCTIONSAREFUN!!!
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

    def gethealth(self):
        return self.health

    def setAttack(self,a):
        self.attack = a


    #Dislplay Image
    def character_image(self):
        image = Image.open("Wizard.png")
        image.show()

TreyIsNotOP = Wizard(99.99999, 199.99999, 299.99999, 399.99999, 'Trey', 'Fire')


TreyIsNotOP.setAttack(100)
print (TreyIsNotOP.getAttack())
TreyIsNotOP.character_image()