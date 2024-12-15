import streamlit as st
import utilities.yamlparser as yp

def sidemenu():
    hoge = st.sidebar
    
    with hoge:
        st.write('hogehogehoge')
        yp.read_yaml()