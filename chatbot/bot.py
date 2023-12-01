import streamlit as st
from htmlTemplates import css


def handle_userinput(user_question):
    st.session_state["messages"].append({"role": "user", "content": user_question})
    st.session_state["messages"].append({"role": "assistant", "content": "Respuesta del chatbot"})
    
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])


def main():
    st.session_state["messages"] = []
    
    st.set_page_config(page_title="Mi Chatbot", page_icon="🤖")
    
    st.write(css, unsafe_allow_html=True)
    st.sidebar.markdown(
        """
        ### Información:
        1. Este es nuestro primer chatbot
        2. Estamos usando contenedores y streamlit
        """)
        
    st.header("Bienvenido a nuestro chatbot")
    
    user_question = st.chat_input("Qué quieres saber?")
    
    if user_question:
        handle_userinput(user_question)
        

if __name__ == "__main__":
    main()