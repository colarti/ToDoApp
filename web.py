import streamlit as st
import modules.func as func


if __name__ == '__main__':
    st.title('My Todo App')
    st.subheader('This is my todo app.')
    st.write('This app is to increase productivity')

    #add checkbox
    # st.checkbox('Buy grocery')

    func.loadfromFile()

    for x in func.todo:
        st.checkbox(x)
    
    #add text input
    st.text_input(label='Enter a todo:', placeholder='Add a todo...')