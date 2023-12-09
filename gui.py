# import tkinter as tk
import PySimpleGUI as gui
from modules.func import *
import time

FILEPATH = 'todo.txt'

gui.theme('DarkBlue9')  #use for reference https://www.geeksforgeeks.org/themes-in-pysimplegui/

if __name__ == '__main__':
    loadfromFile(FILEPATH)

    lblDate = gui.Text('')
    lbl = gui.Text('Type in a ToDo:')
    in_box = gui.InputText(tooltip='Enter a to-do', key='todo')
    list_box = gui.Listbox(values=todo, key='todos', enable_events=True, 
                           size=[45,10])  #45 is X, num of chars, 10 is Y, num of rows
    btnAdd = gui.Button('Add', size=5)  #the size=5 implies 5 chars wide with height of 1
    btnExit = gui.Button('Exit')
    btnEdit = gui.Button('Edit')
    btnPrint = gui.Button('Print')
    btnComplete = gui.Button('Complete')


    win = gui.Window(f'ToDo App', 
                     layout=[[lblDate],
                             [lbl], 
                             [in_box, btnAdd], 
                             [list_box, btnEdit, btnComplete],
                             [btnExit]], 
                     font=('Helvetica',20))

    while True:
        event, value = win.read(timeout=800)
        # print(f'event: {event} | value: {value}')
        
        lblDate.update(value=time.strftime('%b %d, %Y %H:%M:%S'))

        try:
            match event:
                case 'Exit':
                    print(f'reached Exit event')
                    break
                case 'Add':
                    status = addItem2(value['todo'])
                    if status:
                        addToFile()
                        win['todos'].update(values=todo)
                        in_box.update('')
                    else:
                        gui.popup(f'Cant add empty string, write something first', font=('Helvetica', 20))
                case 'Edit':
                    todo_to_edit = value['todos'][0]
                    editItem2(todo_to_edit, value['todo'])
                    win['todos'].update(values=todo)
                    in_box.update('')
                case 'Complete':
                    status = removeItem2(in_box.get())
                    if status == True:
                        win['todos'].update(values=todo)
                        in_box.update('')
                    else:
                        gui.popup(f'Cant complete an empty string, select an item first', font=('Helvetica', 20))
                case 'todos':
                    item_select = value['todos'][0]
                    in_box.update(item_select)
                case 'Print':
                    printItems()
                case gui.WIN_CLOSED:    #this is the closed button (top-right)
                    exit()
                case _:
                    print(f'Invalid Command: {event}')
        except IndexError:
            gui.popup('Select an item first', font=('Helvetica',20))
    
    print(f'GUI Application closing...')
    win.close()