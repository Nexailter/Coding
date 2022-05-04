import PySimpleGUI as pg

close = 'Leave through here'

done = 'Continue through the stages of life'



layout =[[pg.Text("choose your class now"),pg.InputText()],
        [pg.Text("pick an element..."),pg.InputText()],
        [pg.Text('pick a username...'),pg.InputText()],
        [pg.Button(close),pg.Button(done)]]
        

window = pg.Window("Dis Is A Game",layout)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED or event == close :
        break
    if event == done:
        # values is a list of user inputs
        pg.popup('Your class is ' + values[0]+ '\n' + "your element is " + values[1] +'\n' + "your username is " + values[2])


window.close()

