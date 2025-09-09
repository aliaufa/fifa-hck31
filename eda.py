# import
import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from PIL import Image

def run():

    # judul
    st.title('FIFA Data Exploration')
    
    # load gambar
    gambar_header = Image.open('mbappe.jpg')
    st.image(gambar_header)
    st.caption('source: google images')

    # tulisan latar belakang
    st.write("# Latar Belakang")
    st.write("""
             Menurut laporan 
             [FIFA 2022](https://publications.fifa.com/en/annual-report-2021/around-fifa/professional-football-2021/), 
             jumlah pemain sepakbola pada tahun 2021 kurang lebih sebanyak 130.000 pemain. Namun, dalam dataset yang 
             digunakan pada kali ini, hanya mencakup 20.000 pemain saja. Project kali ini bertujuan untuk memprediksi 
             rating pemain FIFA 2022 sehingga semua pemain sepak bola profesional dapat diketahui ratingnya dan tidak 
             menutup kemungkinan untuk lahirnya talenta/wonderkid baru.
             
             Project ini akan dibuat menggunakan algoritma Linear Regresison dan akan dievaluasi 
             dengan menggunakan metrics **MAE (Mean Absolute Error)**.
             """)
    
    # menampilkan dataset
    st.write('# Dataset')
    st.write('''
             Rating dan atribut pemain FIFA 2022 yang diambil dari web 
             [Sofifa.com](https://sofifa.com/?r=220069&set=true)
             ''')
    
    data = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(data)

    # visualisasi
    st.write('# Exploratory Data Analysis')

    st.write('## Player Rating Distribution')
    # matplotlib, histogram rating
    fig = plt.figure(figsize=(16, 5))
    sns.histplot(data['Overall'], kde=True, bins=30)
    plt.title('Histogram of Rating')
    st.pyplot(fig)

    # insight
    st.write('''
            **insight:** Terlihat dari Histogram Plot diatas bahwa `Rating` memiliki distribusi normal 
             dengan mayoritas data berada pada rentang `60` hingga `70`.
            ''')
    
    # visualisasi plotly
    st.write('## Weight vs Height Distribution')
    fig = px.scatter(data, x="Weight", y="Height", hover_name= "Name")
    st.plotly_chart(fig)
        # insight
    st.write('''
            **insight:** `Height` dan `Weight` mempunyai relasi yang searah. Artinya, 
             semakin besar nilai `Height` maka nilai `Weight` juga akan semakin besar. 
             Dapat disimpulkan bahwa mayoritas pemain sepak bola pada dataset ini memiliki 
             kondisi tubuh yang proporsional.
            ''')
    
    # form untuk menampilkan visualisasi pilihan
    st.write('## Player Stat Distribution')
    # select box
    option = st.selectbox('Pick a stat:',
                          ['PaceTotal', 'ShootingTotal', 'PassingTotal', 
                           'DribblingTotal', 'DefendingTotal', 'PhysicalityTotal'])
    # the histogram
    fig = plt.figure(figsize=(16, 5))
    sns.histplot(data[option], kde=True, bins=30)
    plt.title(f'Histogram of {option}')
    st.pyplot(fig)

if __name__ == '__main__':
    run()
