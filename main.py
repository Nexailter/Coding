import utils
import characters
import random
worldFile = open('world.txt','r')
worldData = worldFile.readlines()


#desert,forest,coast,mountains,snowy,populated village,lake


map = [
        ['1a','1b','1c','1d','1e','1f'],
        ['2a','2b','2c','2d','2e','2f'],
        ['3a','3b','3c','3d','3e','3f'],
        ['4a','4b','4c','4d','4e','4f'],
        ['5a','5b','5c','5d','5e','5f'],
        ['6a','6b','6c','6d','6e','6f']
        ]

#print (map)
#1a 1b 2b 2c 2d 3d 3e 2e 1e
             
            
       
# in this coordinate system y axis is first x is last
pos = [0,0]
#health,attack,defense,speed,spawnrate,name
def nav():
        while True:
                whichMonster = random.randint(0,4)
                mon = characters.Monsters()
                if whichMonster == 0:
                        mon = (characters.Monsters())
                elif whichMonster == 1:
                        mon = (characters.Monsters())
                elif whichMonster == 2:
                        mon = (characters.Monsters())
                elif whichMonster == 3:
                        mon = (characters.Monsters())
                elif whichMonster == 4:
                        mon = (characters.Monsters())
                if utils.entitySpawning():
                       
                        print('you have come across a' + mon.getName())
                row = pos[0]
                col = pos[1] #column
                print('you are currently at zone ' + map[row][col])
                direct = input('choose direction \nw = north\na = west\ns = south\nd = east\n')
                if direct == 'd' and col < len(map) - 1:
                        pos[1] = col + 1
                elif  direct == 'a' and col > 0:
                        pos[1] = col - 1
                elif direct == 'w' and row > 0:
                        pos[0] = row - 1
                elif direct == 's' and row < len(map) - 1:
                        pos[0] = row + 1
                else:
                        print("You've reached the ocean, theres nothing exept dark shadows among the waters.")

nav()




#  if l1[0] == l2[0]:
#    return True