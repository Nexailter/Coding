

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
        ['1a','1b'],
        ['2a','2b']
        ]

#print (map)
             
            
       
#Homework: Use len() of map to create boundaries that change according to the map size.
# in this coordinate system y axis is first x is last
pos = [0,0]

def nav():
        while True:
                row = pos[0]
                col = pos[1] #column
                print('you are currently at zone ' + map[row][col])
                direct = input('choose direction \na = east\nb = west\nc = north\nd = south\n')
                if direct == 'a' and col <1:
                        pos[1] = col + 1
                elif  direct == 'b' and col >0:
                        pos[1] = col - 1
                elif direct == 'c' and row >0:
                        pos[0] = row - 1
                elif direct == 'd' and row <1:
                        pos[0] = row + 1
                else:
                        print('Please Choose a Valdid Direction')

nav()