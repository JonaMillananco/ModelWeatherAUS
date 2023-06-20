import os
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 
import warnings
warnings.filterwarnings("ignore", message=".*deprecated.*")
st.set_option('deprecation.showPyplotGlobalUse', False)


st.set_page_config(
    page_title="Mi Aplicación",
    page_icon=":smiley:",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown('<style>div.stPlotlist>div.fullscreenFrame>div {max-width: 400px}</style>', unsafe_allow_html=True)

def main():
    st.title("Bienvenido a la predicción del clima en Australia🦘")
	
    def file_selector(folder_path='./datasets'):       
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Seleccionar un archivo",filenames)
        return os.path.join(folder_path,selected_filename)

    filename = file_selector()
    st.info("Ha seleccionado {}".format(filename))

	#  Leer datos
    df = pd.read_csv(filename)
	# Mostrar conjunto de datos
    if st.checkbox("Mostrar conjunto de datos"):
        age = st.slider('Número de filas a visualizar', 0, 100, 5)
        #number = st.number_input("Número de filas a visualizar")
        st.dataframe(df.head(age))
    
    # Mostrar columnas
    if st.button("Nombres de columnas"):
        st.write(df.columns)

	# Mostrar forma
    if st.checkbox("Forma del conjunto de datos"):
        data_dim = st.radio("Mostrar dimensión por: ",("Filas","Columnas"))
        if data_dim == 'Filas':
            st.text("Número de filas")
            st.write(df.shape[0])
        elif data_dim == 'Columnas':
            st.text("Número de columnas")
            st.write(df.shape[1])
        else:
            st.write(df.shape)
    
    # Seleccionar columnas
    if st.checkbox("Seleccionar columnas para mostrar"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Seleccionar",all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)
        
    # Mostrar valores
    if st.button("El valor cuenta"):
        st.text("Recuentos de valores por: ")
        st.write(df.iloc[:,-1].value_counts())
        
    # Mostrar tipos de datos
    if st.button("Tipos de datos"):
        st.write(df.dtypes)
    # Resumen
    if st.checkbox("Resumen"):
        st.write(df.describe().T)
        
    ## Plot and visualización

    st.subheader("Visualización de datos")
    # Correlation
    # Seaborn Plot
    if st.checkbox("Diagrama de correlación[Seaborn]"):
        st.success("Generando diagrama de correlación")
        fig, ax = plt.subplots(figsize=(8, 6))
        st.write(sns.heatmap(df[['MinTemp','WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm', 'MaxTemp', 'WindSpeed3pm', 'Temp9am']].corr(), annot=True))
        st.pyplot()

        
    # Pie Chart
    if st.checkbox("Pie Plot"):
        if st.button("Generar gráfico circular"):
            st.success("Generando un gráfico circular")
            pie_data = df["RainTomorrow"].value_counts()
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
            ax.set_aspect("equal") 
            ax.set_title("Distribución de RainTomorrow")  
            ax.legend(title="Leyenda", loc="upper right")
            st.pyplot(fig)
    
    # recuento Plot
    if st.checkbox("Plot de los recuentos de valor"):
        st.text("Recuentos de valor por objetivo")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox("Columna Primaria a GroupBy",all_columns_names)
        selected_columns_names = st.multiselect("Select Columns",all_columns_names)
        if st.button("Plot"):
            st.success("Generando un gráfico...")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()

	# Customizable Plot
    st.subheader("Plot personalizable")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Generar tipo de gráfico ",["area","bar","line","hist","box","kde"])
    selected_columns_names = st.multiselect("Seleccionar columnas para gráfico",all_columns_names)

    if st.button("Generar Plot"):
        st.success("Generando gráfico personalizable de {} paradetr5f4 {}".format(type_of_plot,selected_columns_names))

        # Plot By Streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

        # Custom Plot 
        elif type_of_plot:
            cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()

    if st.button("Muchas gracias por su atención"):
        st.balloons()

if __name__ == '__main__':
	main()