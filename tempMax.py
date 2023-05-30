import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st


# Path del modelo preentrenado
MODEL_PATH = 'models/modelo_clima.pkl'

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
        page_title="Temperatura máxima",
        page_icon="🌞",
    )

    st.title("Predicción T° Máxima en Australia")
    #st.sidebar.success("Select a page about")

    # Lectura de datos
    N = st.text_input("Temperatura Minima:")
    P = st.text_input("Humedad 9am:")
    K = st.text_input("Temperatura 9am:")
    Temp = st.text_input("Velocidad 9am:")
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        x_in =[np.float_(N.title()),
                    np.float_(P.title()),
                    np.float_(K.title()),
                    np.float_(Temp.title())]
        predictS = model_prediction(x_in, model)
        
        # Redondear el valor
        temperatura_maxima = round(predictS[0], 1)
        
        st.success(f'La temperatura máxima es: {temperatura_maxima}  °C'.upper())

if __name__ == '__main__':
    main()
