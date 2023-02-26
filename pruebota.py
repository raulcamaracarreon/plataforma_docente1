import streamlit as st
from cuestionario import cuestionario_page
from respuestas import respuestas_page
from Videoteca import videoteca_page
sudo locale-gen es_ES.UTF-8
export LC_ALL=es_ES.UTF-8
export LANG=es_ES.UTF-8
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
