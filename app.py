import pandas as pd
import plotly.express as px
import streamlit as st

# encabezado de la aplicación
st.header("Análisis de anuncios de venta de coches")

# leer los datos
car_data = pd.read_csv("vehicles_us.csv")

# crear un botón
hist_button = st.button("Construir histograma")

# al hacer clic en el botón
if hist_button:

    # escribir un mensaje
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches"
    )

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)
    # botón gráfico de dispersión
scatter_button = st.button("Construir gráfico de dispersión")


# se pone el botón scatter
if scatter_button:

    st.write("Creación de un gráfico de dispersión")

    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig_scatter, use_container_width=True)
