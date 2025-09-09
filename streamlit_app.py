# import libraries
import streamlit as st
# import modules
import eda, predict

st.set_page_config(page_title='FIFA PLAYER RATING',
                   layout= 'centered',)

with st.sidebar:
    st.write("# Page Navigation")
    option = st.selectbox('Page', ['EDA', 'Model Demo'])

    st.write('# About')
    st.write('Page ini adalah informasi data dan demo dari model prediksi player rating')

if option == 'EDA':
    eda.run()
else:
    predict.run()