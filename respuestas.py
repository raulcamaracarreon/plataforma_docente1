import streamlit as st
import pandas as pd
import base64

# Acceder a los secretos
DB_PASSWORD = st.secrets["pruebota_password"]["password"]

def respuestas_page():
    st.title("Administración de datos")

    # Verificar contraseña
    if "password" not in st.session_state:
        st.session_state.password = ""
    if not st.session_state.password:
        st.write("Ingrese la contraseña para ver las respuestas acumuladas:")
        st.text_input("Contraseña:", type="password", key="password")
    if st.session_state.password != DB_PASSWORD:
        st.stop()

    # Leer el archivo CSV con las respuestas
    df = pd.read_csv('respuestas.csv', encoding='utf-8')
    
    # Mostrar las respuestas
    st.dataframe(df.style.set_properties(**{'font-size': '8pt'}), height=400)
    
    # Agregar botón para descargar archivo CSV
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="respuestas.csv">Descargar respuestas</a>'
    st.markdown(href, unsafe_allow_html=True)

   
    
    


