"""global variable todo:list"""
todo = list() 

"""
fn: addItem
input: none
global: todo:list
objective: get input data from user of a new todo action, then aopend to the global 
            variable todo:list
returns: none
"""
def addItem():
    in_data = input('Enter a ToDo: ')
    todo.append(in_data.title())
    addToFile()

"""
fn: addItem2
input: data:str
global: todo:list
objective: aopend to the global variable todo:list, the new input data
returns: none
"""
def addItem2(data):
    todo.append(data.title())
    addToFile()

def printItems():
    for i, x in enumerate(todo):
        print(f'{i+1}. {x}')

def editItem(item):
    if item >= len(todo) or item <= 0:
        print(f'Invalid Selection: {item+1}')
    else:
        edit_item = input('Make the change: ').title()
        todo[item] = edit_item
        addToFile()

def editItem2(item_orig, item_new):
    if item_orig in todo:
        idx = 0
        # for i, x in enumerate(todo):
        #     if x == item_orig:
        #         idx = i
        #         break
        # todo[i] = item_new

        idx = todo.index(item_orig)
        todo[idx] = item_new
        addToFile()

    else:
        print(f'Invalid Original Item: {item_orig}, No Changes')

def removeItem(item):
    if item >= len(todo) or item < 0:
        print(f'Invalid selection: {item+1}')
    else:
        todo.pop(item)
        addToFile()

def removeItem2(item):
    if item in todo:
        idx = 0
        idx = todo.index(item)
        todo.pop(idx)
        addToFile()
    else:
        print(f'Invalid Item: {item}, No Changes')

def addToFile(file='todo.txt'):
    with open(f'.\\App1-ToDoList\\{file}', 'w') as f:
        for x in todo:
            f.write(f'{x}\n')
    f.close()

def loadfromFile(file='todo.txt'):
    with open(f'.\\App1-ToDoList\\{file}', 'r') as f:
        for line in f.readlines():
            todo.append(line.strip())
    f.close()