# import tkinter as tk
import PySimpleGUI as gui
from modules.func import *

FILEPATH = 'todo.txt'
   

if __name__ == '__main__':
    loadfromFile(FILEPATH)
    # print(f'ToDo List: {todo}')

    lbl = gui.Text('Type in a ToDo:')
    in_box = gui.InputText(tooltip='Enter a to-do', key='todo')
    list_box = gui.Listbox(values=todo, key='todos', enable_events=True, size=[45,10])
    btnAdd = gui.Button('Add')
    btnExit = gui.Button('Exit')
    btnEdit = gui.Button('Edit')
    btnPrint = gui.Button('Print')
    btnComplete = gui.Button('Complete')


    win = gui.Window(f'ToDo App', 
                     layout=[[lbl], 
                             [in_box, btnAdd], 
                             [list_box, btnEdit, btnComplete],
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
                win['todos'].update(values=todo)
                in_box.update('')
            case 'Edit':
                todo_to_edit = value['todos'][0]
                editItem2(todo_to_edit, value['todo'])
                win['todos'].update(values=todo)
                in_box.update('')
            case 'Complete':
                removeItem2(in_box.get())
                win['todos'].update(values=todo)
                in_box.update('')
            case 'todos':
                item_select = value['todos'][0]
                in_box.update(item_select)
            case 'Print':
                printItems()
            case gui.WIN_CLOSED:    #this is the closed button (top-right)
                break
            case _:
                print(f'Invalid Command: {event}')
    
    print(f'GUI Application closing...')
    win.close()