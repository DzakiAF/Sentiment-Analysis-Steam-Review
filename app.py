import streamlit as st
import page
import Predict

with st.sidebar:
    st.title('Navigation')
    navigation = st.selectbox("Page", ["EDA", "Predict Review Sentiment"])

if navigation == "EDA":
    page.run()
else:
    Predict.run()