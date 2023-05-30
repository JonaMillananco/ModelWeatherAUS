import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st


# Path del modelo preentrenado
MODEL_PATH = 'models/modelo_clima2.pkl'

# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds

def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    st.set_page_config(
        page_title="¿Llueve mañana?",
        page_icon="☂",
    )
    # Título
    st.title("Predicción lloverá mañana?")

    # Lecctura de datos
    N = st.text_input("Temperatura Minima:")
    P = st.text_input("Humedad 9 AM:")
    K = st.text_input("Temperatura 9 AM:")
    Temp = st.text_input("Velocidad Viento 9 AM:")
    MTemp = st.text_input("Temperatura Maxima:")
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        x_in = [np.float_(N.title()),
            np.float_(P.title()),
            np.float_(K.title()),
            np.float_(Temp.title()),
            np.float_(MTemp.title())]
        predictS = model_prediction(x_in, model)

        if predictS[0] == 1:
            st.success('¿Lloverá mañana?: Si')
        elif predictS[0] == 0:
            st.success('¿Lloverá mañana?: No')
            
if __name__ == '__main__':
    main()
