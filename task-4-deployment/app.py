
import streamlit as st
import os
import configurations as config
from SessionState import get

def css():
    with open(os.path.dirname(__file__) + "/style.css") as file:
        content = file.read()
        #file style attrs
        for key, value in config.style_placeholders.items():
            content = content.replace(key, value)
        st.markdown(content, unsafe_allow_html = True)
state = get(button_pressed = None)
def get_state_handler(model):
    def state_handler():
        state.button_pressed = model['name']
        return model['name']
    return state_handler
def main():
    css()
    #render the models
    for index, model in enumerate(config.models):
        b = st.sidebar.button(model['name'], on_click=get_state_handler(model))
        if b or (~b and state.button_pressed == model['name']):
            title = st.text_input('Product Title:')
            if st.button('Recommend'):
                recommendations = model['handler'](title)
                st.write(recommendations)
if __name__=='__main__':
    main()
