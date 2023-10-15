import streamlit as st
import requests
from io import BytesIO
from PIL import Image

from html_templates import css, bot_template, user_template
from translator import hinglish_translator, telugish_translator, thanglish_translator

url = "https://cdn-icons-png.flaticon.com/512/888/888878.png"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
page_title = 'Polyglot Chat Translator'
page_icon = image
layout = 'centered'

def main():
    st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout
                   )

    hide_style = '''
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                <style>
                
                '''
    header_style = '''
                <style>
                .navbar {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    z-index: 1;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 80px;
                    background-color: #646D7E;
                    box-sizing: border-box;
                }
                
                .navbar-brand {
                    color: white !important;
                    font-size: 23px;
                    text-decoration: none;
                    margin-right: auto;
                    margin-left: 50px;
                }
                
                .navbar-brand img {
                    margin-bottom: 6px;
                    margin-right: 1px;
                    width: 40px;
                    height: 40px;
                    justify-content: center;
                }
                
                /* Add the following CSS to change the color of the text */
                .navbar-brand span {
                    color: #EF6E04;
                    justify-content: center;
                }
                
                </style>
                
                <nav class="navbar">
                    <div class="navbar-brand">
                    <img src="https://cdn-icons-png.flaticon.com/512/888/888878.png" alt="Logo">
                        Polyglot Chat Translator
                    </div>
                </nav>
                '''
    st.markdown(hide_style, unsafe_allow_html=True)
    st.markdown(header_style, unsafe_allow_html=True)
    st.write(css, unsafe_allow_html=True)
    
    api_key = st.sidebar.text_input(label="Enter OpenAPI Key", type='password')
    options = st.sidebar.selectbox(label="Select the language", options=['Hinglish', 'Telugish', 'Thanglish'])
    query = st.chat_input(placeholder="Enter english text to translate")
    
    if query:
        if options == 'Hinglish':
            response = hinglish_translator(api_key=api_key, user_imput=query)
            st.write(user_template.replace("{{MSG}}", query), unsafe_allow_html=True)
            st.write(bot_template.replace("{{MSG}}", response), unsafe_allow_html=True)
        
        elif options == 'Telugish':
            response = telugish_translator(api_key=api_key, user_imput=query)
            st.write(user_template.replace("{{MSG}}", query), unsafe_allow_html=True)
            st.write(bot_template.replace("{{MSG}}", response), unsafe_allow_html=True)
            
        elif options == 'Thanglish':
            response = thanglish_translator(api_key=api_key, user_imput=query)
            st.write(user_template.replace("{{MSG}}", query), unsafe_allow_html=True)
            st.write(bot_template.replace("{{MSG}}", response), unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()