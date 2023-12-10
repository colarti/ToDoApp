import streamlit as st
import modules.func as func

def remove_todo():
    for k, x in st.session_state.items():
        if x == True:
            func.removeItem2(k)

def add_todo():
    new_todo = st.session_state['add_new_todo']
    func.addItem2(new_todo)
    st.session_state['add_new_todo'] = ''

if __name__ == '__main__':
    st.set_page_config(layout='wide')   #change fonts as browser shrinks/expands
    st.title('My Todo App')
    st.subheader('This is my todo app.')
    st.write('This app is to increase <b>productivity</b>', unsafe_allow_html=True) #allows html tags

    func.loadfromFile()

    for x in func.todo:
        #add checkbox
        st.checkbox(x, key=f'{x}', on_change=remove_todo)
        

    #add text input
    st.text_input(label='Enter a todo:', placeholder='Add a todo...', 
                on_change=add_todo, key='add_new_todo')
    
    
            

