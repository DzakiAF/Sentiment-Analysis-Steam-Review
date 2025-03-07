import streamlit as st
import numpy as np
import tensorflow as tf


def run():
    model = tf.keras.models.load_model("model_lstm_2.keras")

    st.title('Prediksi Sentiment Berdasarkan Game Review (dalam bahasa inggris)')
    with st.form('isi Form'):
        st.write('Form Review')
        review= st.text_input(label= "Review",
                                help= "Masukkan Review Anda",
                                placeholder="contoh : good game overall. but lacks character development")

        submit = st.form_submit_button('Submit')
    

    text_input = [review]
    text_tensor = tf.convert_to_tensor(text_input, dtype=tf.string)

    prediction = model.predict(text_tensor)
    result = np.argmax(prediction[0]) 
    print_result=""
    if result == 0:
        print_result= "Prediksi Sentimen: Negative Review (0)"
    else:
        print_result = "Prediksi Sentimen: Positive Review (1)"

    st.write("", print_result)