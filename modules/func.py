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


"""
fn: addItem2
input: data:str
global: todo:list
objective: aopend to the global variable todo:list, the new input data
returns: none
"""
def addItem2(data):
    todo.append(data.title())

def printItems():
    for i, x in enumerate(todo):
        print(f'{i+1}. {x}')

def editItem(item):
    if item >= len(todo) or item <= 0:
        print(f'Invalid Selection: {item+1}')
        return
    else:
        edit_item = input('Make the change: ').title()
        todo[item] = edit_item
        return

def removeItem(item):
    if item >= len(todo) or item < 0:
        print(f'Invalid selection: {item+1}')
    else:
        todo.pop(item)

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