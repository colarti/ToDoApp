from modules.func import *
from datetime import datetime as dt
import time
from filedialogs import open_file_dialog, save_file_dialog

if __name__ == '__main__':
    file = 'todo.txt'

    print(f"It is now: {dt.now().strftime('%Y.%m.%d >%A< %H:%M:%S')}")
    print(f'It is now: {time.strftime("%Y-%m-%d <%A> %H:%M:%S")}')

    loadfromFile(file)

    while True:
        action = input(f'Want to <add,edit,show,complete,exit>: ').strip()
        action = action.split(' ')

        # Option 1 using Match/Case
        # match action:
        #     case 'add':
        #         addItem()
        #         addToFile(file)
        #     case 'show' | 'display':
        #         printItems()
        #     case 'exit':
        #         break
        #     case 'edit':
        #         printItems()
        #         in_data = int(input('Select which item to edit: '))
        #         editItem(in_data-1)
        #         addToFile(file)
        #     case 'complete':
        #         printItems()
        #         in_data = int(input('Select which item is completed: '))
        #         removeItem(in_data-1)
        #         addToFile(file)
        #     case 'save':
        #         addToFile(file)
        #         print(f'File: {file} saved')
        #     case _:
        #         print(f'Invalid Action: {action}')


        # Option 2 using if/elif/else with the in function
        if 'add' in action or 'new' in action:
            if len(action) > 1:
                addItem2(' '.join(action[1:]))
                addToFile(file)
            else:
                print(f'Invalid syntax: add <cmd>')
        elif 'show' in action:
            printItems()
        elif 'exit' in action:
            break
        elif 'edit' in action or 'mod' in action:
            printItems()
            in_data = int(input('Select which item to edit: '))
            editItem(in_data-1)
            addToFile(file)
        elif 'complete' in action or 'finish' in action:
            # printItems()  #Option 1
            # in_data = int(input('Select which item is completed: ')) #Option 1
            # removeItem(in_data-1) #Option 1
            
            if len(action) > 1:
                try:
                    removeItem(int(action[1])-1)
                    addToFile(file)
                except:
                    print(f'expected integer for selection, received: {" ".join(action[1:])}, ignored command')
                    continue
            else:
                print(f'Invalid syntax: complete <num>')
        elif 'save' in action:
            addToFile(file)
            print(f' File: {file} saved')
        else:
            print(f'Invalid Action Command: {action}')