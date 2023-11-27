# import tkinter as tk
import PySimpleGUI as gui
from modules.func import *

FILEPATH = 'todo.txt'
   

if __name__ == '__main__':
    loadfromFile(FILEPATH)
    print(f'ToDo List: {todo}')

    lbl = gui.Text('Type in a ToDo:')
    in_box = gui.InputText(tooltip='Enter a to-do', key='todo')
    btnAdd = gui.Button('Add')
    btnExit = gui.Button('Exit')
    btnEdit = gui.Button('Edit')
    btnComplete = gui.Button('Complete')


    win = gui.Window(f'ToDo App', 
                     layout=[[lbl], 
                             [in_box, btnAdd], 
                             [btnExit]], 
                     font=('Helvetica',20))

    while True:
        event, value = win.read()
        print(f'event: {event} | value: {value}')
        

        match event:
            case 'Exit':
                print(f'reached Exit event')
                break
            case 'Add':
                addItem2(value['todo'])
                addToFile()
            
            case gui.WIN_CLOSED:
                break
            case _:
                print(f'Invalid Command: {event}')
    
    print(f'GUI Application closing...')
    win.close()