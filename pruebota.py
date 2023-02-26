import streamlit as st
from cuestionario import cuestionario_page
from respuestas import respuestas_page
from Videoteca import videoteca_page
import locale
locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')

# Configuración de página
st.set_page_config(page_title="Cuestionario de autoevaluación de prácticas docentes", page_icon=":books:")

# Pestañas
tabs = ["Videoteca", "Cuestionario", "Administración de datos (Sección restringida con contraseña)"]
page = st.sidebar.radio("Elija una opción de la lista:", tabs)

# Contenido de la pestaña seleccionada
if page == "Videoteca":
    videoteca_page()
elif page == "Cuestionario":
    cuestionario_page()
else:
    respuestas_page()
