import pandas as pd
import plotly.express as px
import streamlit as st

df_cars = pd.read_csv('vehicles_us.csv')
st.header("Análisis Exploratorio de Datos")
# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')
# crear un botón
scatter_button = st.button("Construir un diagrama de dispersión")

if build_histogram:  # Al hacer clic en el botón
    # escribir un mensaje
    st.write(
        "Creacion de un histograma para el conjunto de datos de anuncios de venta de coches.")

    # crear un histograma
    fig = px.histogram(df_cars, x="odometer")

    # mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:  # Al hacer clic en el botón
    # escribir un mensaje
    st.write("Creacion de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches.")

    # crear un diagrama de dispersión
    fig = px.scatter(df_cars, x='odometer', y='price')

    # mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
