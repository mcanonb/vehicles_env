# libreria
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# datos
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Titulo
st.header("Relacion entre variables de Vehicles US", divider="gray")

st.divider()

# crear un botón
hist_button = st.button('Construir histograma')

st.divider()

if hist_button:  # al hacer clic en el botón:
    try:
        # escribir un mensaje
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        # crear un histograma
        fig = px.histogram(car_data, x="odometer")
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.write("Faltan variables por seleccionar")
