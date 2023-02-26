import pandas as pd
import streamlit as st
import altair as alt
from io import BytesIO
import requests
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def videoteca_page():
    
    st.title("Videoteca")
    
    archivo = "base2.xlsx"
    df = pd.read_excel(archivo)

    niveles = df["Nivel"].unique()
    nivel_seleccionado = st.selectbox("Seleccione un nivel", niveles)

    df_nivel = df[df["Nivel"] == nivel_seleccionado]

    if not df_nivel.empty:
        videos = df_nivel["Nombre Clave"]
        video_seleccionado = st.selectbox("Seleccione un video", videos)

        df_video = df_nivel[df_nivel["Nombre Clave"] == video_seleccionado]

        st.subheader("Video")
        video_url = df_video["Liga"].values[0]
        st.video(video_url)

        st.subheader("Información del video")
        st.write(f"**País:** {df_video['País'].values[0]}")
        st.write(f"**Institución:** {df_video['Institución'].values[0]}")
        st.write(f"**Nivel:** {df_video['Nivel'].values[0]}")
        st.write(f"**Tipo de contexto:** {df_video['Tipo de contexto'].values[0]}")
        st.write(f"**Tipo de organización de la escuela:** {df_video['Tipo de organización de la escuela'].values[0]}")

    else:
        st.warning("No hay videos disponibles para el nivel seleccionado")

def get_video_bytes(video_url):
    video_bytes = None
    try:
        content = requests.get(video_url).content
        video_bytes = BytesIO(content)
    except:
        pass
    return video_bytes

