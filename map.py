

# grid = [[,,,,,,,,,,],
#         [,,,,,,,,,,],
#         [,,,,,,,,,,],
#         [,,,,,,,,,,],
#         [,,,,,,,,,,],
#         [,,,,,,,,,,],
#         [,,,,,,,,,,],
#         [,,,,,,,,,,],
#         [,,,,,,,,,,],
#         [,,,,,,,,,,]]


#desert,plains,ocean,mountains,restricted wilderness,snowy,deserted village,populated village


map = [
        ['1a','1b','1c','1d','1e','1f'],
        ['2a','2b','2c','2d','2e','2f'],
        ['3a','3b','3c','3d','3e','3f'],
        ['4a','4b','4c','4d','4e','4f'],
        ['5a','5b','5c','5d','5e','5f']
        ['6a','6b','6c','6d','6e','6f']
        ]

#print (map)
             
            
       
#Homework: Use len() of map to create boundaries that change according to the map size.
# in this coordinate system y axis is first x is last
#still only able to travel to 4 different spaces instead of all 36
pos = [0,0]

def nav():
        while True:
                row = pos[0]
                col = pos[1] #column
                print('you are currently at zone ' + map[row][col])
                direct = input('choose direction \na = east\nb = west\nc = north\nd = south\n')
                if direct == 'a' and col < len(map) - 1:
                        pos[1] = col + 1
                elif  direct == 'b' and col > 0:
                        pos[1] = col - 1
                elif direct == 'c' and row > 0:
                        pos[0] = row - 1
                elif direct == 'd' and row < len(map) - 1:
                        pos[0] = row + 1
                else:
                        print('Please Choose a Valdid Direction')

nav()