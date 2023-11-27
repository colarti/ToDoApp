# import tkinter as tk
import PySimpleGUI as gui
from modules.func import *

FILEPATH = 'todo.txt'
   

if __name__ == '__main__':
    loadfromFile(FILEPATH)

    lbl = gui.Text('Type in a ToDo:')
    in_box = gui.InputText(tooltip='Enter a to-do')
    btnAdd = gui.Button('Add', target=addItem2(in_box.get()))
    btnExit = gui.Button('Exit')


    win = gui.Window(f'ToDo App', layout=[[lbl], [in_box, btnAdd], [btnExit]])

    win.read()  #displays the window
    win.close()