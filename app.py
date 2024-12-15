import streamlit as st
import pandas as pd
import pages.test as test
import sidemenu.sidemenu as sidemenu

def app():

    st.write('hoge')
    test.hoge()
    sidemenu.sidemenu()


if __name__=='__main__':
    app()