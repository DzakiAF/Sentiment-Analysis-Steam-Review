import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.title('Steam Game Review')

    st.image('https://cdn.fastly.steamstatic.com/store/home/store_home_share.jpg')

    st.markdown('''
                # About
    Page ini berisi EDA untuk Game Review pada Steam dari 3 bulan terakhir.
                ''')
    st.write('# Dataset')
    df = pd.read_csv('Train.csv')
    df.drop(columns=['Review', 'Cleaned_Review', 'Game'], axis=1,inplace=True)
    st.dataframe(df, hide_index=True)

    st.write('# Exploratory Data Analysis')

    fig = plt.figure(figsize=(10,5))
    sns.countplot(data=df, x='Sentiment', palette='viridis')
    st.pyplot(fig)

    st.markdown('''
                Persebaran data di awal tidak balance. Sebelum ditrain baru akan seimbangkan.
                ''')