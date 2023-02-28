import streamlit as st
import csv
import pandas as pd
import locale
import re

locale.setlocale(locale.LC_ALL, '')

# Función para validar la entrada de la clave CCT
def validate_cct(cct):
    # Expresión regular para validar la clave CCT
    pattern = r'^[1-3][0-9][FEK][A-Z]{2}\d{4}[A-Z0-9]$'
    # Validar la entrada utilizando la expresión regular
    if re.match(pattern, cct):
        return True
    else:
        return False

# Definición de la función cuestionario_page
def cuestionario_page():
    # Título de la aplicación
    st.title("Cuestionario de autoevaluación de prácticas docentes")
    # Formulario de entrada

    # Interfaz de usuario para ingresar la clave CCT
    cct = st.text_input("Ingrese la clave CCT:")

    # Validar la entrada de la clave CCT
    if validate_cct(cct):
        st.success("La clave CCT es válida.")
    else:
        st.error("La clave CCT no es válida. Por favor, ingrese una clave CCT válida en el formato indicado.")

    st.write("Por favor ingrese la siguiente información:")
    apellido_paterno = st.text_input("Apellido paterno")
    apellido_materno = st.text_input("Apellido materno")
    nombres = st.text_input("Nombre(s)")
    st.write("Por favor ingrese la siguiente información:")
    st.write("1. ¿Considera que sus prácticas profesionales son efectivas?")
    pregunta_1 = st.selectbox("1. ¿Considera que sus prácticas profesionales son efectivas?", ['Totalmente de acuerdo', 'De acuerdo', 'En desacuerdo', 'Totalmente en desacuerdo'])
    st.write("2. ¿Por qué lo considera así? Justifique su respuesta.")
    pregunta_2 = st.text_input("2. ¿Por qué lo considera así? Justifique su respuesta.")
    st.write("3. ¿Considera que requiere de formación continua para mejorar sus prácticas profesionales?")
    pregunta_3 = st.selectbox("3. ¿Considera que requiere de formación continua para mejorar sus prácticas profesionales?", ['Totalmente de acuerdo', 'De acuerdo', 'En desacuerdo', 'Totalmente en desacuerdo'])
    st.write("4. ¿Por qué lo considera así? Justifique su respuesta.")
    pregunta_4 = st.text_input("4. ¿Por qué lo considera así? Justifique su respuesta.")

    # Botón para enviar respuestas
    if st.button("Enviar respuestas"):
        # Guardar respuestas en archivo CSV
        with open('respuestas.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([apellido_paterno, apellido_materno, nombres, cct, pregunta_1, pregunta_2, pregunta_3, pregunta_4])
        st.success("Sus respuestas han sido enviadas.")
