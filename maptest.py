worldFile = open('world.txt','r')
worldData = worldFile.readlines()
#print (worldData)
map = [
        ['1a','1b','1c','1d','1e','1f'],
        ['2a','2b','2c','2d','2e','2f'],
        ['3a','3b','3c','3d','3e','3f'],
        ['4a','4b','4c','4d','4e','4f'],
        ['5a','5b','5c','5d','5e','5f'],
        ['6a','6b','6c','6d','6e','6f']
        ]


#boolean A.K.A bool is true or false or 1's and 0's
#function that would take numerical coordinates as an input and the calculate the current cell name inport the region data associated with it
#1. get pos
#2. calculate coordinates to figure out the cell name and biome
#3. input data
def gridInfo(position):
    x = position[1]
    y = position[0]
    row = map[y]
    cell = row[x]
    print (cell)

gridInfo([5,3])

    








#codingBat
#def not_string(str):
#  return ('not ' + str)
    
