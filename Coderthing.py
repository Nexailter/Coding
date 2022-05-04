#Pront the user to select a character class
#character classes: wizard, hunter, Demon
#change the image depending on user's imput
#print out a text file corresponding to the class of character
#once you have put in your username it will give you battle skills and controls.
#we will make a nickname restricter and multiple choise for class and elememts so people dont put non-real classes and elements
#Objective of the game is to protect the 6 dragons from the evil prince and his kights who are trying to ipress the fairest maiden of the land by slaying the dragons. once done and he is gone from the island you must visit HIS island to confront him and his knights and have a legendary battle. win or dont win. depends on your skill
#player has coins to purchase things from the shop

from PIL import Image


import turtle
screen = turtle.Screen()

choice = ['a','b','c']

classes = ['Hunter','Demon','Wizard']
Elements = ['Fire','Ice','Earth','Lightning']
bad_words = ['fuck','fuck off','shit','asshole','apple']  
shop = {'Speed' :50 , 'Damage' :50 , 'Health' :50 }

coins = 100

Class = ''
while Class not in choice:
  Class = input ("Class Choose:\n a = Hunter \n b = Demon \n c = Wizard \n")
  if Class == 'a':
    Class = 'Hunter'
  if Class == 'b':
    Class = 'Demon'
  if Class == 'c':
    Class = 'Wizard'
  if Class in classes:
    break
  
choice = ['a','b','c','d']

Element = ''
while Element not in choice:
  Element = input ('\nElement Choose:\na = Fire\nb = Ice\nc = Earth\nd = Lightning\n')
  if Element == 'a':
    Element = 'Fire'
  if Element == 'b':
    Element = 'Ice' 
  if Element == 'c':
    Element = 'Earth'
  if Element == 'd':
    Element = 'Lightning'
  if Element in Elements:
    break




Username = ''
valid_name = True
while valid_name == True:
  Username = input ("Make An Appropriate User Name:")
  for words in bad_words:
    if words in Username:
      Usernames = input('choose a more apropriate name')
  valid_name = False

print
print ("Username: "+   Username)

print ('You Have ' + str(coins) + ' Coins')


#hahahahahahahahahaha funny number




  
  
  
#Dislplay Image
def character_image(image):
  image = Image.open(image+ ".png")
  image.show()


character_image(Class)

#Class Skills
def class_name(name):
  f = open(name  + ".txt", 'r')
  print ('\nclass bio:\n')
  print(f.read())

#Element Skills
def element_name(name):
  f = open(name + ".txt", 'r')
  print ("\n\nElement Bio:\n")
  print(f.read())


print (Class)
# # #Calltofunction
# character_image(Class)
class_name(Class)
element_name(Element)


#Questions
#Class and element

for key in shop:
  print("\n"+key + ' ' + "¢" + str(shop[key])) 

(upgrade) = input('What upgrade do you want?????????????\n')

if (upgrade) == ('Health'):
  (coins)-=(50)
  print('¢' + str(coins) + ' left' )

if (upgrade) == ('Damage'):
  (coins)-=(50)
  print('¢' + str(coins) + ' left' )

if (upgrade) == ('Speed'):
  (coins)-=(50)
  print('¢' + str(coins) + ' left' )