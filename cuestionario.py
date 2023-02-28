import streamlit as st
import csv
import pandas as pd
import locale
import re

# Tabla de entidades federativas
entidades = {
    "01": "Aguascalientes",
    "02": "Baja California",
    "03": "Baja California Sur",
    "04": "Campeche",
    "05": "Coahuila",
    "06": "Colima",
    "07": "Chiapas",
    "08": "Chihuahua",
    "09": "Ciudad de México",
    "10": "Durango",
    "11": "Guanajuato",
    "12": "Guerrero",
    "13": "Hidalgo",
    "14": "Jalisco",
    "15": "Estado de México",
    "16": "Michoacán",
    "17": "Morelos",
    "18": "Nayarit",
    "19": "Nuevo León",
    "20": "Oaxaca",
    "21": "Puebla",
    "22": "Querétaro",
    "23": "Quintana Roo",
    "24": "San Luis Potosí",
    "25": "Sinaloa",
    "26": "Sonora",
    "27": "Tabasco",
    "28": "Tamaulipas",
    "29": "Tlaxcala",
    "30": "Veracruz",
    "31": "Yucatán",
    "32": "Zacatecas"
}

# Tabla de identificadores
identificadores = {
    "CC": "Escuela de Educación Preescolar Indígena",
    "JN": "Escuela de Educación Preescolar",
    "PB": "Escuela de Educación Primaria Indígena",
    "PR": "Escuela de Educación Primaria",
    "ES": "Escuela de Educación Secundaria General",
    "ST": "Escuela de Educación Secundaria Técnica",
    "TV": "Telesecundaria"
}

def validate_cct(cct):
    # Expresión regular para validar la clave CCT
    pattern = r'^[1-3][0-9][FEK][A-Z]{2}\d{4}[A-Z0-9]$'
    # Validar la entrada utilizando la expresión regular
    if re.match(pattern, cct):
        return True
    else:
        return False

def get_entidad_federativa(cct):
    entidad_code = cct[:2]
    entidad = entidades.get(entidad_code, None)
    return entidad

def get_identificador(cct):
    identificador_code = cct[4:6]
    identificador = identificadores.get(identificador_code, None)
    return identificador

def cuestionario_page():
    # Título de la aplicación
    st.title("Cuestionario de autoevaluación de prácticas docentes")
    # Formulario de entrada
    
    st.write("Por favor ingrese la siguiente información:")
    apellido_paterno = st.text_input("Apellido paterno")
    apellido_materno = st.text_input("Apellido materno")
    nombres = st.text_input("Nombre(s)")
    
    # Interfaz de usuario para ingresar la clave CCT
    cct = st.text_input("Ingrese la clave CCT:")

    # Validar la entrada de la clave CCT
    if validate_cct(cct):
        # Desglosar información de la clave CCT
        entidad_federativa = cct[0:2]
        clasificador = cct[2]
        identificador = cct[3:5]
        num_progresivo = cct[5:9]
        elemento_verificador = cct[9]
        
        # Mostrar información desglosada de la clave CCT
        st.success("La clave CCT es válida.")
        st.write(f"Entidad federativa: {ENTIDADES_FEDERATIVAS[entidad_federativa]}")
        st.write(f"Clasificador: {CLASIFICADORES[clasificador]}")
        st.write(f"Identificador: {IDENTIFICADORES[identificador]}")
        st.write(f"Número progresivo: {num_progresivo}")
        st.write(f"Elemento verificador: {elemento_verificador}")
        
        # Preguntas del cuestionario
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
    else:
        st.error("La clave CCT no es válida. Por favor, ingrese una clave CCT válida en el formato indicado.")



