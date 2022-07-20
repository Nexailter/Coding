import PySimpleGUI as pg
from utils import*
from characters import*
from crossroads import*
close = 'Close'

done = 'Continue'



layout =[[pg.Text("choose your class now"),pg.InputText()],
        [pg.Text("pick an element..."),pg.InputText()],
        [pg.Text('pick a username...'),pg.InputText()],
        [pg.Button(close),pg.Button(done)]]
        

window = pg.Window("Graveyard of the six",layout)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED or event == close :
        break
    if event == done:
        break
        # values is a list of user inputs
        # character_class = values[0]
        # character_element = values[1]
        # character_username = values[2]
        # if check_class(character_class) == True and check_element(character_element) == check_username(character_username) == True:
        #     character = None
        #     if character_class == 'Demon':
        #         character = Demon(50,30,40,30,character_username,character_element )
        #     if character_class == 'Hunter':
        #         character = Hunter(50,30,40,30,character_username,character_element )
        #     if character_class == 'Wizard':
        #         character = Wizard(50,30,40,30,character_username,character_element )
        #     pg.popup('Your class is ' + values[0]+ '\n' + "your element is " + values[1] +'\n' + "your username is " + values[2])
        # else: