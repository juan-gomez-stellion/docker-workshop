import streamlit as st
from htmlTemplates import css
import os
from langchain.vectorstores import Chroma
import chromadb
from chromadb.config import Settings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings


def handle_userinput(user_question):
    response = st.session_state.qa_chain({"query": user_question})
    st.session_state["messages"].append({"role": "user", "content": user_question})
    st.session_state["messages"].append({"role": "assistant", "content": response['result']})
    
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])


def get_vector():


    path = './db'

    settings = Settings(
    persist_directory=path,
    anonymized_telemetry=False
    )

    client = chromadb.PersistentClient(settings=settings, path=path)


    vectordb = Chroma(
                client=client,
                embedding_function=OpenAIEmbeddings(),
            )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(search_kwargs={'k':3}),
        return_source_documents=False,
        chain_type="stuff"
    )

    return qa_chain


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

    if "qa_chain" not in st.session_state:
        st.session_state["qa_chain"] = get_vector()
    
    if user_question:
        handle_userinput(user_question)
        

if __name__ == "__main__":
    main()